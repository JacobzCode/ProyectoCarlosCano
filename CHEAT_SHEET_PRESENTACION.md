# 📋 CHEAT SHEET - SUSTENTACIÓN MOODKEEPER
## (Para imprimir y tener a mano)

---

## 🎯 ESTRUCTURA (10-15 min)
1. Introducción (2 min)
2. Demo en vivo (5 min)
3. Arquitectura (3 min)
4. Funcionalidades (2 min)
5. Tecnologías (1 min)
6. Conclusiones (1 min)

---

## 🔑 DATOS CLAVE

### URLs
- Frontend: `http://localhost:8000`
- Backend: `http://127.0.0.1:8001`
- API Docs: `http://127.0.0.1:8001/docs`
- GitHub: `github.com/JacobzCode/ProyectoCarlosCano`

### Credenciales Demo
- Usuario: `demo_user`
- Email: `demo@example.com`
- Password: `demo123456`

### Valores para entrada de prueba
- Mood: **3** (bajo, para mostrar detección de riesgo)
- Comentario: "Estresado con el proyecto"
- Sueño: **5 horas**
- Actividad: **2/10**
- Alimentación: **4/10**
- Socialización: **3/10**

---

## 💻 COMANDOS IMPORTANTES

```bash
# Iniciar Backend
cd mood-keeper
.venv\Scripts\python.exe main.py

# Iniciar Frontend
cd frontend
python -m http.server 8000

# Ver tests (opcional)
pytest -v
```

---

## 📊 ALGORITMO DE RIESGO (0-100)

| Factor | Condición | Puntos |
|--------|-----------|--------|
| Mood bajo | ≤3 | +40 |
| Sueño | <6h | +20 |
| Actividad física | <3 | +15 |
| Alimentación | <3 | +15 |
| Socialización | <3 | +10 |

---

## 🏗️ ARQUITECTURA

```
FRONTEND (8000)
    ↓ HTTP/JSON
BACKEND API (8001)
    ↓ SQLAlchemy
SQLite DATABASE
```

**11 Endpoints:**
- `/api/accounts` - Registro
- `/api/sessions` - Login
- `/api/entries` - Mood entries
- `/api/insights/*` - Análisis
- `/api/resources` - Apoyo

---

## 💻 TECNOLOGÍAS

**Backend:**
- Python 3.13.9
- FastAPI 0.104.1
- SQLAlchemy 2.0.44
- Pandas 2.3.3
- pytest 8.4.2 (25 tests)

**Frontend:**
- HTML5 + CSS3 + JS
- Bootstrap 5.3.2

**BD:** SQLite 3.x

---

## ✅ CUMPLIMIENTO

| Entrega | % |
|---------|---|
| Primera | 100% |
| Segunda | 100% |
| Tercera | 100% |

**Extras:**
- Sistema de hábitos (4 campos)
- Risk scoring (0-100)
- 25 tests automatizados
- 120+ págs documentación

---

## 📈 MÉTRICAS

- 3,100+ líneas código
- 11 endpoints API
- 6 páginas web
- 25 tests
- 9 commits GitHub

---

## 🎤 FRASES CLAVE

**Inicio:**
> "1 de cada 7 jóvenes sufre trastornos mentales. MoodKeeper ayuda a detectarlos tempranamente."

**Durante demo:**
> "Observen que todos estos valores son bajos. El sistema detectará esto como riesgo."

**Arquitectura:**
> "El frontend se comunica con el backend por HTTP, intercambiando JSON."

**Algoritmo:**
> "Desarrollé un algoritmo multi-factorial de risk scoring de 0 a 100 puntos."

**Cierre:**
> "MoodKeeper cumple su objetivo: detectar riesgo tempranamente y conectar con recursos de apoyo."

---

## ❓ RESPUESTAS RÁPIDAS

**¿Por qué FastAPI?**
→ Moderno, rápido, validación automática

**¿Es seguro?**
→ JWT + bcrypt + validación + ORM

**¿Por qué SQLite?**
→ Perfecto para desarrollo, migra fácil a PostgreSQL

**¿Tiene tests?**
→ Sí, 25 tests con pytest

**¿Es escalable?**
→ Sí, arquitectura API REST estándar

---

## ⚠️ SI ALGO FALLA

1. **Mantener calma**
2. **Explicar el proceso**: "En este punto, el sistema haría..."
3. **Mostrar código** como alternativa
4. **Continuar con confianza**

---

## ✅ CHECKLIST FINAL

- [ ] Ambos servidores corriendo
- [ ] Navegador con pestañas listas
- [ ] VS Code abierto
- [ ] Esta hoja impresa
- [ ] Agua cerca
- [ ] Respirar profundo
- [ ] ¡CONFIANZA! 💪

---

## 💪 RECUERDA

✅ Hablar claro y pausado  
✅ Mantener contacto visual  
✅ Mostrar entusiasmo  
✅ Narrar mientras haces  
✅ Pausar estratégicamente  

❌ No disculparse innecesariamente  
❌ No hablar muy rápido  
❌ No dar la espalda  

---

## 🎬 SECUENCIA DEMO

1. Registro → mostrar formulario
2. Login → ver redirección
3. Dashboard → estadísticas
4. Nueva entrada → valores bajos
5. Historial → ver entrada
6. Recursos → líneas de ayuda
7. API Docs → endpoint alerts

**Tiempo:** 5 minutos exactos

---

## 🔥 AFIRMACIÓN

**"Proyecto completo ✅"**  
**"100% requisitos ✅"**  
**"Estoy preparado ✅"**  
**"¡Voy a brillar! ⭐"**

---

**¡MUCHA SUERTE! 🚀**

---

_Imprime esta hoja y tenla cerca durante la presentación_
