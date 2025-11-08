# 📝 SCRIPT DE PRESENTACIÓN - MoodKeeper
## (Versión Corta - 10 minutos)

---

## 🎬 APERTURA (30 segundos)

**[Sonrisa, contacto visual]**

"Buenos días/tardes compañeros. Soy Carlos Cano y hoy presentaré **MoodKeeper**, una plataforma web para monitorear la salud mental en jóvenes."

**[Pausa 2 segundos]**

"Según la OMS, 1 de cada 7 jóvenes sufre trastornos mentales. MoodKeeper ayuda a detectarlos tempranamente."

---

## 💻 DEMOSTRACIÓN EN VIVO (4 minutos)

### Paso 1: Registro (30 seg)
**[Abrir: localhost:8000/register.html]**

"Primero, un usuario se registra. Es simple: usuario, email, contraseña."

**[Llenar formulario rápidamente]**
- Usuario: `demo_user`
- Email: `demo@example.com`
- Contraseña: `demo123456`

**[Clic en Crear]**

"La app usa JWT para autenticación segura y bcrypt para encriptar contraseñas."

**[Esperar redirección al login]**

---

### Paso 2: Login (20 seg)
**[En login.html]**

"El sistema me redirige automáticamente al login."

**[Ingresar credenciales y entrar]**

"Y ahora accedo al dashboard."

---

### Paso 3: Dashboard (2 min)
**[En dashboard.html]**

"Aquí vemos tres secciones principales:"

**[Señalar con el mouse]**

"Arriba: mis estadísticas. Formulario para registrar mi estado diario. Y abajo: mi historial."

**[Scroll al formulario]**

"Ahora voy a registrar cómo me siento hoy:"

**[Llenar EN VIVO mientras narras]**
- Mood: Deslizar a **3** → "Me siento un poco bajo hoy"
- Comentario: "Estuve estresado con el proyecto"
- Horas sueño: **5 horas** → "Dormí poco"
- Actividad física: **2/10**
- Alimentación: **4/10**
- Socialización: **3/10**

**[Pausa dramática]**

"Observen que todos estos valores son bajos. El sistema detectará esto como riesgo."

**[Clic en Guardar]**

"Al guardar, la entrada aparece en mi historial inmediatamente."

**[Señalar la nueva fila en la tabla]**

"El badge rojo indica mood bajo."

---

### Paso 4: Recursos (1 min)
**[Navegar a resources.html]**

"Si alguien está en riesgo, la app ofrece recursos de apoyo inmediato:"

**[Scroll mostrando secciones]**
- "Líneas de emergencia 24/7"
- "Servicios gratuitos de salud mental"
- "Ejercicios de respiración"

"Esto conecta al usuario con ayuda real."

---

### Paso 5: API Backend (30 seg)
**[Abrir: 127.0.0.1:8001/docs]**

"El backend es una API REST documentada automáticamente."

**[Expandir /api/insights/alerts]**

"Este endpoint detecta usuarios en riesgo usando un algoritmo de 0-100 puntos."

**[Clic en Try it out → Execute]**

"Aquí está el JSON de respuesta con el risk score que calculé."

---

## 🏗️ ARQUITECTURA (2 minutos)

**[Tono seguro y claro]**

"La arquitectura tiene tres capas:"

**1. Frontend** - Puerto 8000
- HTML, CSS, JavaScript, Bootstrap
- 6 páginas web

**2. Backend** - Puerto 8001
- Python + FastAPI
- 11 endpoints API
- Módulos: seguridad, persistencia, análisis

**3. Base de Datos**
- SQLite con SQLAlchemy ORM
- 2 tablas: accounts y entries

**[Pausa]**

"El frontend se comunica con el backend por HTTP, intercambiando JSON."

---

## 🔬 ALGORITMO DE RIESGO (1 minuto)

**[Mostrar seguridad técnica]**

"Desarrollé un algoritmo multi-factorial de risk scoring:"

**[Contar con los dedos]**

- Mood bajo (≤3): **40 puntos**
- Sueño insuficiente (<6h): **20 puntos**
- Baja actividad física: **15 puntos**
- Mala alimentación: **15 puntos**
- Aislamiento social: **10 puntos**

"La suma da el risk score de 0 a 100. Esto permite detectar patrones antes de que empeoren."

---

## 💻 TECNOLOGÍAS (30 segundos)

**[Hablar con confianza]**

"Tecnologías usadas:"

**Backend:**
- Python 3.13
- FastAPI (moderno y rápido)
- SQLAlchemy (ORM)
- Pandas (análisis de datos)
- pytest (25 tests)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5

---

## ✅ CUMPLIMIENTO (1 minuto)

**[Mostrar orgullo del trabajo]**

"El proyecto cumple **100%** con todos los requisitos:"

**Primera Entrega: ✅**
- GitHub con control de versiones
- Scripts de Python funcionales

**Segunda Entrega: ✅**
- Base de datos SQLite
- Análisis con Pandas
- Informe técnico 21 páginas

**Tercera Entrega: ✅**
- Dashboard funcional
- Sistema de alertas
- Informe técnico 25 páginas

**[Pausa para efecto]**

"Además agregué funcionalidades extra:"
- Sistema de hábitos (4 campos)
- Risk scoring (0-100)
- 25 tests automatizados
- 120+ páginas de documentación

---

## 📊 MÉTRICAS (20 segundos)

**[Datos rápidos y contundentes]**

"En números:"
- **3,100+** líneas de código
- **11** endpoints API
- **6** páginas web
- **25** tests automatizados
- **9** commits en GitHub

---

## 🎓 CONCLUSIÓN (1 minuto)

**[Mirar a la audiencia, sonreír]**

"MoodKeeper cumple su objetivo: proporcionar una herramienta accesible para monitorear salud mental, detectar riesgo tempranamente y conectar con recursos de apoyo."

**[Pausa]**

"Este proyecto me permitió aplicar Python en un contexto real, trabajar con APIs REST, análisis de datos y desarrollo full-stack."

**[Mirada al futuro]**

"A futuro se podría agregar:"
- Machine Learning para predicción
- App móvil
- Chat con profesionales
- Integración con wearables

**[Cerrar con seguridad]**

"Gracias por su atención. ¿Hay alguna pregunta?"

**[Sonreír y esperar]**

---

## 🎯 PUNTOS CLAVE PARA RECORDAR

### Durante toda la presentación:

✅ **Hablar claro y pausado** - No apresurarse  
✅ **Mantener contacto visual** - Mirar a diferentes personas  
✅ **Usar las manos** - Señalar, contar, gesticular  
✅ **Mostrar entusiasmo** - El proyecto es bueno, demuéstralo  
✅ **Pausar estratégicamente** - Dar tiempo para procesar  
✅ **Narrar mientras haces** - No dejar silencios incómodos  
✅ **Si algo falla, mantener calma** - Explicar el proceso  

### Frases poderosas para usar:

- "Como pueden observar..."
- "Esto es importante porque..."
- "Aquí vemos cómo..."
- "El sistema detecta automáticamente..."
- "Implementé esto para..."

### Lo que NO hacer:

❌ Disculparse innecesariamente  
❌ Decir "no sé" sin agregar nada  
❌ Leer textualmente  
❌ Dar la espalda a la audiencia  
❌ Hablar demasiado rápido  
❌ Usar muletillas ("eh", "este", "entonces")  

---

## 🔥 RESPUESTAS RÁPIDAS A PREGUNTAS

**P: ¿Por qué FastAPI?**
> "Moderno, rápido, validación automática y documentación auto-generada."

**P: ¿Es seguro?**
> "Sí: JWT + bcrypt + validación + ORM previene SQL injection."

**P: ¿Por qué SQLite?**
> "Para desarrollo es perfecto. En producción se migra fácilmente a PostgreSQL."

**P: ¿Tiene tests?**
> "Sí, 25 tests con pytest cubriendo seguridad, persistencia y análisis."

**P: ¿Es escalable?**
> "Sí, arquitectura API REST se escala con servidores cloud y balanceadores."

**P: ¿Cómo funciona el algoritmo de riesgo?**
> "Sistema de puntuación 0-100 considerando mood, sueño, ejercicio, alimentación y socialización."

---

## ⏰ TIMING IDEAL

| Sección | Tiempo | Acumulado |
|---------|--------|-----------|
| Apertura | 0:30 | 0:30 |
| Demo - Registro | 0:30 | 1:00 |
| Demo - Login | 0:20 | 1:20 |
| Demo - Dashboard | 2:00 | 3:20 |
| Demo - Recursos | 1:00 | 4:20 |
| Demo - API | 0:30 | 4:50 |
| Arquitectura | 2:00 | 6:50 |
| Algoritmo | 1:00 | 7:50 |
| Tecnologías | 0:30 | 8:20 |
| Cumplimiento | 1:00 | 9:20 |
| Métricas | 0:20 | 9:40 |
| Conclusión | 1:00 | 10:40 |
| **Buffer para preguntas** | 4:20 | 15:00 |

---

## 🎬 ÚLTIMO CHECKLIST

**30 minutos antes:**
- [ ] Servidores corriendo
- [ ] Pestañas abiertas
- [ ] VS Code con código
- [ ] Agua cerca
- [ ] Respirar profundo

**5 minutos antes:**
- [ ] Crear usuario de prueba limpio
- [ ] Verificar conexión a proyector
- [ ] Cerrar notificaciones
- [ ] Poner teléfono en silencio

**Al empezar:**
- [ ] Sonreír
- [ ] Mirar a la audiencia
- [ ] Hablar con claridad
- [ ] ¡Disfrutar!

---

## 💪 AFIRMACIÓN FINAL

**"Has construido un proyecto completo y funcional."**

**"Conoces cada línea de código."**

**"Cumples 100% de requisitos."**

**"Estás preparado para brillar."**

**¡ADELANTE! 🚀**

---

**Tiempo total:** 10-15 minutos  
**Nivel de dificultad:** ⭐⭐⭐⭐⭐  
**Tu preparación:** ⭐⭐⭐⭐⭐  
**Resultado esperado:** ⭐⭐⭐⭐⭐
