# 🚀 GUÍA RÁPIDA DE INSTALACIÓN

## Requisitos Previos

- Python 3.8 o superior
- Git instalado
- Navegador web moderno

---

## 📥 Instalación en 5 Pasos

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/JacobzCode/ProyectoCarlosCano.git
cd ProyectoCarlosCano
```

### 2️⃣ Instalar Dependencias Python

```bash
cd mood-keeper
pip install -r requirements.txt
```

**Dependencias que se instalarán:**
- FastAPI (framework web)
- SQLAlchemy (ORM)
- Pandas (análisis de datos)
- Matplotlib & Seaborn (visualizaciones)
- pytest (testing)
- Y más...

### 3️⃣ Inicializar Base de Datos

**Opción A:** Si tienes datos CSV legacy
```bash
python migrate_to_db.py
```

**Opción B:** Si es instalación nueva
```bash
python -c "from app.database import init_db; init_db(); print('✅ DB inicializada')"
```

### 4️⃣ Ejecutar el Backend

```bash
python main.py
```

**Salida esperada:**
```
Starting MoodKeeper...
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

✅ Backend corriendo en: **http://127.0.0.1:8001**

### 5️⃣ Ejecutar el Frontend

**En otra terminal:**

```bash
cd ../frontend
python -m http.server 8000
```

**Salida esperada:**
```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

✅ Frontend corriendo en: **http://localhost:8000**

---

## 🎯 Acceder a la Aplicación

1. Abrir navegador en: **http://localhost:8000**
2. Hacer clic en "Registrarse"
3. Crear una cuenta con:
   - Handle (nombre de usuario)
   - Email
   - Contraseña
4. Iniciar sesión
5. ¡Empezar a usar Mood Keeper!

---

## 🧪 Ejecutar Tests (Opcional)

```bash
cd mood-keeper
pytest tests/ -v
```

**Salida esperada:**
```
tests/test_security.py::test_hash_secret PASSED
tests/test_security.py::test_verify_secret PASSED
tests/test_storage_db.py::test_create_account PASSED
...
======================== 25 passed in 2.34s ========================
```

---

## 📊 Probar Funcionalidades

### ✅ Crear Primera Entrada

1. Ir a Dashboard
2. Hacer clic en el botón flotante "+" (esquina inferior derecha)
3. Completar formulario:
   - **Mood:** Deslizar de 1 a 10
   - **Notas:** Comentario opcional
   - **Horas de sueño:** Ej: 7.5
   - **Actividad física:** 0-10
   - **Calidad de alimentación:** 0-10
   - **Nivel de socialización:** 0-10
4. Hacer clic en "Enviar"
5. ✅ Ver entrada en el dashboard

### ✅ Ver Visualizaciones

Después de crear varias entradas:
- **Gráfico de barras:** Promedio por usuario
- **Histograma:** Distribución de mood
- **Tabla de alertas:** Entradas de riesgo

### ✅ Acceder a Recursos

1. Ir a "Recursos" en el menú
2. Ver recursos de emergencia
3. Ver recomendaciones personalizadas según tu mood

---

## 🔧 Solución de Problemas

### ❌ Error: "Module not found"

**Solución:**
```bash
pip install -r requirements.txt --upgrade
```

### ❌ Error: "Port already in use"

**Backend (8001):**
```bash
# Windows
netstat -ano | findstr :8001
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8001 | xargs kill -9
```

**Frontend (8000):**
```bash
# Cambiar puerto
python -m http.server 8080
```

### ❌ Error: "Database locked"

**Solución:**
```bash
# Cerrar todas las conexiones
cd mood-keeper/data
rm mood_keeper.db
python -c "from app.database import init_db; init_db()"
```

### ❌ Gráficos no se muestran

**Verificar:**
1. Backend corriendo en puerto 8001
2. Frontend apuntando a `http://127.0.0.1:8001/api`
3. CORS habilitado en server.py

---

## 📱 Endpoints API Disponibles

### Autenticación
- `POST /api/accounts` - Registrar usuario
- `POST /api/sessions` - Iniciar sesión
- `POST /api/sessions/logout` - Cerrar sesión

### Entradas
- `POST /api/entries` - Crear entrada
- `GET /api/entries` - Listar entradas

### Análisis
- `GET /api/insights/summary` - Estadísticas generales
- `GET /api/insights/average` - Promedio por usuario
- `GET /api/insights/alerts?threshold=3&days=30` - Alertas
- `GET /api/insights/plot/hist?type=hist` - Histograma
- `GET /api/insights/plot/by_handle` - Boxplot por usuario
- `GET /api/insights/plot/ts` - Time series

### Recursos
- `GET /api/resources` - Recursos personalizados (requiere auth)

---

## 🎓 Documentación Completa

- [README.md](README.md) - Descripción general
- [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) - Todo lo implementado
- [INFORME_SEGUNDA_ENTREGA.md](INFORME_SEGUNDA_ENTREGA.md) - Análisis de datos
- [INFORME_TERCERA_ENTREGA.md](INFORME_TERCERA_ENTREGA.md) - Dashboard y visualización
- [ANALISIS_PROYECTO.md](ANALISIS_PROYECTO.md) - Cumplimiento de requisitos

---

## 💡 Datos de Prueba

Para probar rápidamente, crear estos usuarios:

```
Usuario 1:
- Handle: usuario1
- Email: usuario1@test.com
- Password: test123

Usuario 2:
- Handle: usuario2
- Email: usuario2@test.com
- Password: test123
```

Crear entradas con diferentes moods (1-10) para ver gráficos variados.

---

## 🆘 Soporte

**Problemas comunes:** Ver sección "Solución de Problemas" arriba

**Repositorio:** https://github.com/JacobzCode/ProyectoCarlosCano

**Issues:** https://github.com/JacobzCode/ProyectoCarlosCano/issues

---

## ✅ Checklist de Verificación

Después de la instalación, verificar:

- [ ] Backend corriendo en http://127.0.0.1:8001
- [ ] Frontend corriendo en http://localhost:8000
- [ ] Puede registrarse un usuario
- [ ] Puede iniciar sesión
- [ ] Puede crear una entrada
- [ ] Dashboard muestra gráficos
- [ ] Página de recursos carga
- [ ] Tests pasan (pytest)

---

**¡Listo para usar Mood Keeper! 🎉**

**Tiempo estimado de instalación:** 5-10 minutos
