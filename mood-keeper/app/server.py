from fastapi import FastAPI, HTTPException, status, Depends, Header, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import Tuple
from .dto import AccountCreate, SessionCreate, AccountOut, EntryCreate, EntryOut
from .storage_db import AccountStoreDB, EntryStoreDB
from .security import hash_secret, verify_secret, make_token, read_token
from . import insights
from fastapi import Response

app = FastAPI(title='MoodKeeper', description='Service for mood entries', version='0.1')

# Allow the frontend (served e.g. at http://127.0.0.1:5500 or http://localhost:8000) to call the API during development
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:5501",
    "http://localhost:5501",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

account_store = AccountStoreDB()
entry_store = EntryStoreDB()


def _current_user(authorization: str = Header(..., alias='Authorization')) -> Tuple:
    # Accept standard 'Authorization: Bearer <token>' header
    auth = authorization
    if not isinstance(auth, str) or not auth.startswith('Bearer '):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid auth scheme')
    token = auth.split(' ', 1)[1]
    handle = read_token(token)
    if not handle:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or expired token')
    account = account_store.find_by_handle(handle)
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Account not found')
    return account, token


@app.post('/api/accounts', response_model=AccountOut, status_code=status.HTTP_201_CREATED)
def create_account(acc: AccountCreate):
    if account_store.find_by_handle(acc.handle):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Handle already exists')
    h = hash_secret(acc.secret)
    a = account_store.create(acc.handle, acc.email, h)
    return AccountOut(id=a.id, handle=a.handle, email=a.email, created=a.created)


@app.post('/api/sessions')
def create_session(s: SessionCreate):
    a = account_store.find_by_handle(s.handle)
    if not a or not verify_secret(s.secret, a.hashed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    t = make_token(a.handle)
    return {'access_token': t, 'token_type': 'bearer'}


@app.post('/api/sessions/logout')
def logout(user_and_token = Depends(_current_user)):
    # stateless token: logout is client-side removal; for real revocation implement storage
    user, token = user_and_token
    return {'message': f'Logged out {user.handle}'}


@app.post('/api/entries', response_model=EntryOut, status_code=status.HTTP_201_CREATED)
def create_entry(entry: EntryCreate, authorization: str = Header(None, alias='Authorization')):
    # Allow anonymous submissions if Authorization is not provided or invalid
    acct = None
    if authorization and isinstance(authorization, str) and authorization.startswith('Bearer '):
        token = authorization.split(' ', 1)[1]
        handle = read_token(token)
        if handle:
            acct = account_store.find_by_handle(handle)

    # fallback anonymous account
    if not acct:
        class _Anon: id = 0; handle = 'anonymous'
        acct = _Anon()

    if not (1 <= entry.mood <= 10):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mood must be 1-10')
    
    # Validar campos de hábitos si están presentes
    if entry.actividad_fisica is not None and not (0 <= entry.actividad_fisica <= 10):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='actividad_fisica must be 0-10')
    if entry.calidad_alimentacion is not None and not (0 <= entry.calidad_alimentacion <= 10):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='calidad_alimentacion must be 0-10')
    if entry.nivel_socializacion is not None and not (0 <= entry.nivel_socializacion <= 10):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='nivel_socializacion must be 0-10')
    if entry.horas_sueno is not None and not (0 <= entry.horas_sueno <= 24):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='horas_sueno must be 0-24')
    
    e = entry_store.create(
        acct.id, acct.handle, entry.mood, entry.comment,
        entry.horas_sueno, entry.actividad_fisica,
        entry.calidad_alimentacion, entry.nivel_socializacion
    )
    return EntryOut(
        id=e.id, account_id=e.account_id, handle=e.handle, 
        mood=e.mood, comment=e.comment,
        horas_sueno=e.horas_sueno, actividad_fisica=e.actividad_fisica,
        calidad_alimentacion=e.calidad_alimentacion, nivel_socializacion=e.nivel_socializacion,
        created=e.created
    )


@app.get('/api/entries')
def list_entries():
    items = []
    for e in entry_store.list_all():
        items.append({
            'id': e.id, 'account_id': e.account_id, 'handle': e.handle, 
            'mood': e.mood, 'comment': e.comment,
            'horas_sueno': e.horas_sueno, 'actividad_fisica': e.actividad_fisica,
            'calidad_alimentacion': e.calidad_alimentacion, 'nivel_socializacion': e.nivel_socializacion,
            'created': e.created
        })
    return items


@app.get('/api/insights/summary')
def insights_summary():
    return insights.summary()


@app.get('/api/insights/average')
def insights_avg():
    return insights.avg_by()


@app.get('/api/insights/alerts')
def insights_alerts(threshold: float = 3.0, days: int = 30):
    return insights.alerts(threshold=threshold, days=days)


@app.get('/api/insights/plot/{plot_name}')
def insights_plot(plot_name: str, type: str = None):
    png = insights.plot_png(plot_name, plot_type=type)
    if png is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Plot not available')
    return Response(content=png, media_type='image/png')


@app.get('/api/resources')
def get_resources(user_and_token = Depends(_current_user)):
    """Get personalized resources based on user's recent mood"""
    user, _ = user_and_token
    
    # Get user's recent entries
    recent_entries = [e for e in entry_store.list_all() if e.handle == user.handle][:10]
    
    # Calculate average mood
    avg_mood = sum(e.mood for e in recent_entries) / len(recent_entries) if recent_entries else 5
    
    resources = {
        'emergency': [
            {
                'title': 'Línea de Prevención del Suicidio',
                'description': 'Disponible 24/7 para apoyo inmediato',
                'contact': '106',
                'url': 'https://www.minsalud.gov.co'
            },
            {
                'title': 'Línea Amiga',
                'description': 'Apoyo psicológico gratuito',
                'contact': '106',
                'url': '#'
            }
        ],
        'recommended': []
    }
    
    # Personalized recommendations based on mood
    if avg_mood <= 4:
        resources['recommended'].extend([
            {
                'title': 'Ejercicios de Respiración',
                'description': 'Técnicas de respiración para reducir la ansiedad',
                'type': 'exercise',
                'url': '#breathing'
            },
            {
                'title': 'Mindfulness para Principiantes',
                'description': 'Meditaciones guiadas de 5 minutos',
                'type': 'meditation',
                'url': '#mindfulness'
            },
            {
                'title': 'Habla con un Profesional',
                'description': 'Agenda una cita con un psicólogo',
                'type': 'professional',
                'url': '#therapy'
            }
        ])
    elif avg_mood <= 7:
        resources['recommended'].extend([
            {
                'title': 'Rutina de Ejercicio',
                'description': 'Actividades físicas para mejorar el ánimo',
                'type': 'exercise',
                'url': '#exercise'
            },
            {
                'title': 'Journaling Emocional',
                'description': 'Guía para expresar tus emociones por escrito',
                'type': 'activity',
                'url': '#journaling'
            }
        ])
    else:
        resources['recommended'].extend([
            {
                'title': 'Mantén tus Hábitos Saludables',
                'description': 'Consejos para mantener tu bienestar',
                'type': 'wellness',
                'url': '#wellness'
            },
            {
                'title': 'Comparte tu Experiencia',
                'description': 'Ayuda a otros compartiendo lo que te ha funcionado',
                'type': 'community',
                'url': '#community'
            }
        ])
    
    # Add habit-specific recommendations
    if recent_entries:
        latest = recent_entries[0]
        if latest.horas_sueno and latest.horas_sueno < 6:
            resources['recommended'].insert(0, {
                'title': 'Mejora tu Higiene del Sueño',
                'description': 'Técnicas para dormir mejor',
                'type': 'sleep',
                'url': '#sleep'
            })
        if latest.actividad_fisica and latest.actividad_fisica < 3:
            resources['recommended'].insert(0, {
                'title': 'Comienza con Ejercicio Ligero',
                'description': 'Rutinas de 10 minutos para empezar',
                'type': 'exercise',
                'url': '#light-exercise'
            })
    
    return resources
