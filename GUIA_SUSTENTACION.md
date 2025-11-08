# 🎤 GUÍA DE SUSTENTACIÓN - MoodKeeper

## 📋 Información General
**Proyecto:** MoodKeeper - Sistema de Monitoreo de Salud Mental  
**Estudiante:** Carlos Cano  
**Duración sugerida:** 10-15 minutos  
**Fecha:** Noviembre 2025

---

## 🎯 ESTRUCTURA DE LA PRESENTACIÓN (10-15 min)

### 1️⃣ INTRODUCCIÓN (2 minutos)

**Saludo y presentación:**
> "Buenos días/tardes compañeros. Mi nombre es Carlos Cano y hoy les presentaré MoodKeeper, una plataforma web para el monitoreo de salud mental en jóvenes."

**Contexto del problema:**
> "Según la OMS, 1 de cada 7 jóvenes entre 10-19 años experimenta trastornos mentales. La mayoría no recibe atención adecuada. MoodKeeper surge como una herramienta de prevención y detección temprana."

**Objetivo del proyecto:**
> "El objetivo es crear una plataforma que permita a los jóvenes registrar su estado emocional diariamente, identificar patrones de riesgo y conectarlos con recursos de apoyo."

---

### 2️⃣ DEMOSTRACIÓN EN VIVO (5 minutos)

**A. Registro de Usuario (30 seg)**
1. Abrir: `http://localhost:8000/register.html`
2. Crear cuenta: `usuario_demo` / `demo@example.com` / `password123`
3. Mostrar redirección automática al login

**B. Inicio de Sesión (30 seg)**
1. Ingresar credenciales
2. Mostrar autenticación con JWT
3. Acceso al dashboard

**C. Dashboard Principal (2 min)**
1. Mostrar estadísticas del usuario:
   - Mood promedio
   - Total de entradas
   - Última entrada

2. **Crear nueva entrada en vivo:**
   - Mood: Deslizar a 3 (bajo)
   - Comentario: "Me siento un poco triste hoy"
   - Horas sueño: 5 horas
   - Actividad física: 2/10
   - Alimentación: 4/10
   - Socialización: 3/10

3. Hacer clic en "Guardar entrada"
4. Mostrar cómo aparece en el historial

**D. Recursos de Apoyo (1 min)**
1. Navegar a: `http://localhost:8000/resources.html`
2. Mostrar:
   - Líneas de emergencia (911)
   - Línea de Prevención del Suicidio
   - Ejercicios de respiración
   - Recursos gratuitos

**E. Backend API (1 min)**
1. Abrir: `http://127.0.0.1:8001/docs`
2. Mostrar documentación interactiva de FastAPI
3. Expandir endpoint `/api/insights/alerts`
4. Ejecutar y mostrar JSON de respuesta con risk scoring

---

### 3️⃣ ARQUITECTURA TÉCNICA (3 minutos)

**Diagrama mental mientras explicas:**

```
┌─────────────────────────────────────────┐
│           FRONTEND (Cliente)            │
│  HTML5 + CSS3 + JavaScript + Bootstrap  │
│          Puerto: 8000                   │
└─────────────┬───────────────────────────┘
              │ HTTP Requests (Fetch API)
              │ JSON
              ▼
┌─────────────────────────────────────────┐
│        BACKEND (Servidor API)           │
│     Python 3.13 + FastAPI               │
│          Puerto: 8001                   │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │  Endpoints (11 total)           │  │
│  │  • /api/accounts (registro)     │  │
│  │  • /api/sessions (login)        │  │
│  │  • /api/entries (mood entries)  │  │
│  │  • /api/insights/* (análisis)   │  │
│  │  • /api/resources (apoyo)       │  │
│  └─────────────────────────────────┘  │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │  Módulos de Lógica              │  │
│  │  • security.py (JWT + bcrypt)   │  │
│  │  • storage_db.py (CRUD)         │  │
│  │  • insights.py (análisis datos) │  │
│  └─────────────────────────────────┘  │
└─────────────┬───────────────────────────┘
              │ SQLAlchemy ORM
              ▼
┌─────────────────────────────────────────┐
│         BASE DE DATOS                   │
│         SQLite 3.x                      │
│                                         │
│  Tabla: accounts                        │
│  • id, handle, email, hashed, created  │
│                                         │
│  Tabla: entries                         │
│  • id, account_id, mood, comment,      │
│    horas_sueno, actividad_fisica,      │
│    calidad_alimentacion, etc.          │
└─────────────────────────────────────────┘
```

**Explicación oral:**

> "La arquitectura sigue el patrón cliente-servidor. El frontend corre en el puerto 8000 usando un servidor HTTP simple de Python. El backend es una API REST construida con FastAPI en el puerto 8001."

> "El frontend se comunica con el backend mediante peticiones HTTP usando Fetch API, intercambiando datos en formato JSON."

> "El backend tiene 11 endpoints organizados por funcionalidad: autenticación, gestión de entradas y análisis de datos."

> "La persistencia se maneja con SQLite mediante SQLAlchemy ORM, con dos tablas principales: accounts y entries."

> "Para seguridad, implementé autenticación JWT con tokens de 24 horas y hashing de contraseñas con bcrypt."

---

### 4️⃣ FUNCIONALIDADES PRINCIPALES (2 minutos)

**Mencionar con claridad:**

✅ **1. Registro y Autenticación Segura**
- JWT tokens con expiración
- Hashing bcrypt de contraseñas
- Validación de datos con Pydantic

✅ **2. Registro de Estado Emocional**
- Escala de mood 1-10
- Tracking de hábitos (sueño, ejercicio, alimentación, socialización)
- Comentarios libres

✅ **3. Análisis de Datos con Python**
- Pandas para procesamiento
- Estadísticas descriptivas
- Promedios y agregaciones

✅ **4. Sistema de Detección de Riesgo**
> "Desarrollé un algoritmo de risk scoring de 0-100 puntos que considera múltiples factores:
> - Mood bajo (≤3): +40 puntos
> - Sueño insuficiente (<6h): +20 puntos
> - Baja actividad física (<3): +15 puntos
> - Mala alimentación (<3): +15 puntos
> - Baja socialización (<3): +10 puntos"

✅ **5. Recursos de Apoyo Personalizados**
- Líneas de emergencia
- Servicios gratuitos de salud mental
- Ejercicios de mindfulness
- Enlaces a grupos de apoyo

---

### 5️⃣ TECNOLOGÍAS UTILIZADAS (1 minuto)

**Backend:**
- 🐍 **Python 3.13.9**
- ⚡ **FastAPI 0.104.1** - Framework web moderno y rápido
- 🗄️ **SQLAlchemy 2.0.44** - ORM para base de datos
- 📊 **Pandas 2.3.3** - Análisis de datos
- 🔐 **JWT + bcrypt** - Seguridad

**Frontend:**
- 🌐 **HTML5 + CSS3 + JavaScript ES6+**
- 🎨 **Bootstrap 5.3.2** - Framework CSS

**Base de Datos:**
- 💾 **SQLite 3.x** - Base de datos relacional

**Testing:**
- 🧪 **pytest 8.4.2** - 25 tests automatizados

---

### 6️⃣ CUMPLIMIENTO DE REQUISITOS (1 minuto)

**Mostrar confianza al decir:**

> "El proyecto cumple al 100% con todos los requisitos del integrador:"

**Primera Entrega:** ✅ 100%
- Repositorio en GitHub con control de versiones
- Scripts de Python funcionales
- Estructura organizada

**Segunda Entrega:** ✅ 100%
- Base de datos SQLite con SQLAlchemy
- Análisis de datos con Pandas
- Visualizaciones implementadas
- Informe técnico de 21 páginas

**Tercera Entrega:** ✅ 100%
- Dashboard funcional
- Sistema de alertas de riesgo
- Evolución temporal de datos
- Informe técnico de 25 páginas

**Extras implementados:**
- ✨ Sistema de tracking de hábitos (4 campos adicionales)
- ✨ Algoritmo de risk scoring (0-100)
- ✨ 25 tests automatizados con pytest
- ✨ 120+ páginas de documentación técnica

---

### 7️⃣ CÓDIGO EN VIVO (1-2 minutos - OPCIONAL)

**Si hay tiempo, mostrar código relevante:**

**A. Algoritmo de Risk Scoring** (`mood-keeper/app/insights.py`)

```python
# Calcular score de riesgo (0-100)
risk_score = 0
if row.get('mood', 5) <= threshold:
    risk_score += 40  # Mood bajo es el factor más importante
if row.get('horas_sueno', 8) < 6:
    risk_score += 20  # Sueño insuficiente
if row.get('actividad_fisica', 5) < 3:
    risk_score += 15  # Baja actividad física
if row.get('calidad_alimentacion', 5) < 3:
    risk_score += 15  # Mala alimentación
if row.get('nivel_socializacion', 5) < 3:
    risk_score += 10  # Aislamiento social
```

> "Este algoritmo multi-factorial detecta riesgo considerando no solo el mood, sino también hábitos de vida que impactan la salud mental."

**B. Endpoint de Registro** (`mood-keeper/app/server.py`)

```python
@app.post('/api/accounts', response_model=AccountOut, 
          status_code=status.HTTP_201_CREATED)
def create_account(acc: AccountCreate):
    if account_store.find_by_handle(acc.handle):
        raise HTTPException(status_code=400, 
                          detail='Handle already exists')
    h = hash_secret(acc.secret)  # Hashing con bcrypt
    a = account_store.create(acc.handle, acc.email, h)
    return AccountOut(id=a.id, handle=a.handle, 
                     email=a.email, created=a.created)
```

> "Aquí vemos la validación de usuario duplicado y el hashing seguro de la contraseña antes de guardarla."

---

### 8️⃣ RETOS Y SOLUCIONES (1 minuto)

**Ser honesto y mostrar aprendizaje:**

**Reto 1: Redirección después de registro**
> "Inicialmente, el alert() bloqueaba la redirección al login. Lo solucioné usando `window.location.replace()` que reemplaza la entrada en el historial."

**Reto 2: CORS en desarrollo**
> "El frontend y backend corrían en puertos diferentes. Configuré CORS en FastAPI para permitir peticiones desde localhost:8000."

**Reto 3: Manejo de datos temporales**
> "Implementé SQLite con SQLAlchemy para persistencia robusta, migrando desde archivos CSV."

---

### 9️⃣ MÉTRICAS DEL PROYECTO (30 seg)

**Datos concretos impresionan:**

📊 **Estadísticas:**
- 3,100+ líneas de código
- 11 endpoints API funcionales
- 6 páginas web completas
- 25 tests automatizados
- 120+ páginas de documentación técnica
- 9 commits en GitHub

---

### 🔟 CONCLUSIONES Y TRABAJO FUTURO (1 minuto)

**Cerrar con impacto:**

**Logros:**
> "MoodKeeper cumple su objetivo de proporcionar una herramienta accesible para el monitoreo de salud mental. Implementa detección temprana de riesgo, análisis de datos y conexión con recursos de apoyo."

**Aprendizajes:**
> "Este proyecto me permitió aplicar Python en un contexto real, trabajar con APIs REST, implementar análisis de datos con Pandas y desarrollar una aplicación full-stack completa."

**Trabajo Futuro:**
> "Para escalar el proyecto, se podrían implementar:
> - Notificaciones push cuando se detecta riesgo alto
> - Machine Learning para predicción de patrones
> - App móvil con React Native
> - Integración con wearables (Fitbit, Apple Watch)
> - Chat con profesionales de salud mental"

**Cierre:**
> "Gracias por su atención. Estoy disponible para responder cualquier pregunta."

---

## 🎤 CONSEJOS PARA LA PRESENTACIÓN

### ✅ ANTES DE PRESENTAR

1. **Practicar el flujo completo 2-3 veces**
2. **Verificar que ambos servidores estén corriendo:**
   ```bash
   # Terminal 1: Backend
   cd mood-keeper
   .venv\Scripts\python.exe main.py
   
   # Terminal 2: Frontend
   cd frontend
   python -m http.server 8000
   ```
3. **Tener las URLs abiertas en pestañas:**
   - Dashboard: `http://localhost:8000/dashboard.html`
   - Recursos: `http://localhost:8000/resources.html`
   - API Docs: `http://127.0.0.1:8001/docs`
4. **Cerrar aplicaciones innecesarias**
5. **Tener el código abierto en VS Code**

### ✅ DURANTE LA PRESENTACIÓN

**Lenguaje corporal:**
- Mantener contacto visual con la audiencia
- Hablar con claridad y pausadamente
- Usar las manos para enfatizar puntos importantes
- Mostrar confianza y entusiasmo

**Manejo de la demo:**
- Narrar lo que estás haciendo mientras lo haces
- Si algo falla, mantener la calma y explicar el proceso
- Tener un plan B (screenshots o video grabado)

**Interacción:**
- Pausar para preguntas breves
- Agradecer comentarios constructivos
- Relacionar el proyecto con situaciones reales

### ✅ RESPUESTAS A PREGUNTAS COMUNES

**P: ¿Por qué elegiste FastAPI en lugar de Flask o Django?**
> R: "FastAPI es más moderno, incluye validación automática con Pydantic, genera documentación interactiva automáticamente y es significativamente más rápido que Flask."

**P: ¿Cómo garantizas la seguridad de los datos de salud mental?**
> R: "Implementé JWT para autenticación, bcrypt para hashing de contraseñas, validación de inputs con Pydantic, y SQLite que evita SQL injection al usar ORM. Para producción, se agregaría HTTPS y cifrado de base de datos."

**P: ¿Por qué SQLite y no PostgreSQL o MySQL?**
> R: "Para desarrollo y demostración, SQLite es ideal por su simplicidad (no requiere servidor separado). En producción, migrar a PostgreSQL es trivial gracias a SQLAlchemy ORM."

**P: ¿Cómo funciona el algoritmo de detección de riesgo?**
> R: "Es un sistema de puntuación multi-factorial de 0-100 que considera mood bajo (40pts), sueño insuficiente (20pts), baja actividad física (15pts), mala alimentación (15pts) y aislamiento social (10pts). Los valores están basados en investigación de factores de riesgo en salud mental."

**P: ¿Tiene testing?**
> R: "Sí, implementé 25 tests automatizados con pytest cubriendo seguridad (JWT, hashing), persistencia (CRUD operations) y análisis de datos (insights, alertas)."

**P: ¿Es escalable el proyecto?**
> R: "La arquitectura cliente-servidor con API REST es inherentemente escalable. Se podría desplegar el backend en un servidor cloud, usar PostgreSQL en lugar de SQLite, implementar caché con Redis y agregar balanceadores de carga."

---

## 📊 MATERIAL DE APOYO

### Diapositivas Sugeridas (si se requieren):

1. **Portada**: Título, nombre, fecha
2. **Contexto**: Estadísticas de salud mental juvenil
3. **Objetivo**: Qué problema resuelve MoodKeeper
4. **Arquitectura**: Diagrama cliente-servidor
5. **Funcionalidades**: Lista con screenshots
6. **Tecnologías**: Logos de Python, FastAPI, SQLite, etc.
7. **Demo**: Video o screenshots del flujo completo
8. **Código destacado**: Algoritmo de risk scoring
9. **Métricas**: Números del proyecto
10. **Conclusiones**: Logros y trabajo futuro
11. **Agradecimientos y preguntas**

### Recursos para mostrar:

- ✅ Repositorio GitHub: `https://github.com/JacobzCode/ProyectoCarlosCano`
- ✅ Documentación: Mostrar archivos `.md` en VS Code
- ✅ Tests: Ejecutar `pytest -v` en vivo si hay tiempo
- ✅ Base de datos: Mostrar con SQLite Browser (opcional)

---

## 🎯 CHECKLIST FINAL PRE-PRESENTACIÓN

- [ ] Ambos servidores corriendo sin errores
- [ ] Base de datos con datos de prueba
- [ ] Navegador con pestañas preparadas
- [ ] VS Code abierto con código relevante
- [ ] Guía de sustentación impresa o en segunda pantalla
- [ ] Plan B preparado (screenshots, video)
- [ ] Agua cerca para hidratarse
- [ ] Respirar profundo y relajarse 😊

---

## 💪 MENSAJE FINAL

**Recuerda:** Has construido un proyecto completo, funcional y bien documentado. Cumples 100% con los requisitos y agregaste funcionalidades extra. Tienes todas las herramientas para una excelente presentación.

**¡Confía en tu trabajo y demuestra tu conocimiento!**

**¡Mucha suerte en tu sustentación! 🚀**

---

**Preparado por:** GitHub Copilot  
**Fecha:** 8 de noviembre de 2025  
**Versión:** 1.0
