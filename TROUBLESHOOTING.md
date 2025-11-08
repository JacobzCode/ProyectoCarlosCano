# 🔧 SOLUCIÓN DE PROBLEMAS COMUNES

## Mood Keeper - Troubleshooting Guide

---

## 🐛 Problemas de Instalación

### ❌ "ModuleNotFoundError: No module named 'sqlalchemy'"

**Causa:** Las dependencias no están instaladas o el entorno virtual no está activo.

**Solución:**
```bash
# Activar entorno virtual
# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate

# Instalar dependencias
cd mood-keeper
pip install -r requirements.txt
```

### ❌ "python: command not found"

**Causa:** Python no está instalado o no está en el PATH.

**Solución:**
1. Verificar instalación: `python --version` o `python3 --version`
2. Descargar Python 3.8+ de https://python.org
3. En Windows, marcar "Add to PATH" durante instalación

### ❌ "No module named 'app'"

**Causa:** Ejecutando desde el directorio incorrecto.

**Solución:**
```bash
# Debe estar en mood-keeper/
cd mood-keeper
python main.py
```

---

## 🌐 Problemas de Backend

### ❌ "Address already in use" (Puerto 8001)

**Causa:** Otro proceso está usando el puerto 8001.

**Solución:**

**Windows:**
```powershell
# Encontrar proceso
netstat -ano | findstr :8001

# Matar proceso (reemplazar <PID>)
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
# Encontrar y matar proceso
lsof -ti:8001 | xargs kill -9

# O cambiar puerto en main.py:
# run(..., port=8002, ...)
```

### ❌ "Database is locked"

**Causa:** Múltiples conexiones intentando acceder a SQLite simultáneamente.

**Solución:**
```bash
# Cerrar todas las conexiones
# Reiniciar el servidor

# Si persiste, recrear DB:
cd mood-keeper/data
rm mood_keeper.db
cd ..
python -c "from app.database import init_db; init_db()"
```

### ❌ "CORS error" en el navegador

**Causa:** El backend no está corriendo o configuración CORS incorrecta.

**Solución:**
1. Verificar que backend esté corriendo en http://127.0.0.1:8001
2. Verificar en `server.py`:
```python
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",  # Agregar
    "http://localhost:8000",   # Agregar
]
```

### ❌ "422 Unprocessable Entity"

**Causa:** Datos enviados no cumplen validación de Pydantic.

**Solución:**
1. Verificar que mood esté entre 1-10
2. Verificar que horas_sueno sea 0-24
3. Verificar que otros campos sean 0-10
4. Ver detalles en consola del navegador (F12)

---

## 🎨 Problemas de Frontend

### ❌ Gráficos no se muestran

**Causa:** Backend no está corriendo o no hay datos.

**Solución:**
1. Verificar backend: http://127.0.0.1:8001/api/insights/summary
2. Crear al menos 5 entradas para ver gráficos
3. Verificar consola del navegador (F12) para errores

### ❌ "Failed to fetch" en el navegador

**Causa:** URL incorrecta o backend no responde.

**Solución:**
```javascript
// Verificar en app.js:
const API_BASE = 'http://127.0.0.1:8001/api'

// Probar manualmente:
// http://127.0.0.1:8001/api/insights/summary
```

### ❌ Formulario no resetea después de enviar

**Causa:** Este error YA fue corregido en la última versión.

**Solución:**
```bash
# Actualizar repositorio
git pull origin main
```

### ❌ "Unauthorized" al crear entrada

**Causa:** Token JWT expiró o no existe.

**Solución:**
1. Cerrar sesión
2. Iniciar sesión nuevamente
3. Verificar que `localStorage.getItem('mk_token')` tenga valor

---

## 🧪 Problemas de Tests

### ❌ "ModuleNotFoundError" al ejecutar pytest

**Causa:** pytest no está instalado o no está en PATH.

**Solución:**
```bash
pip install pytest pytest-asyncio
pytest tests/ -v
```

### ❌ Tests fallan con "Database locked"

**Causa:** Tests accediendo a misma DB simultáneamente.

**Solución:**
```bash
# Ejecutar tests secuencialmente
pytest tests/ -v -n 0

# O usar DB de test separada
```

### ❌ "fixture 'db_session' not found"

**Causa:** Tests no encuentran fixtures.

**Solución:**
```bash
# Ejecutar desde directorio correcto
cd mood-keeper
pytest tests/ -v
```

---

## 📊 Problemas de Visualización

### ❌ "Plot not available" (404)

**Causa:** No hay suficientes datos para generar gráfico.

**Solución:**
1. Crear al menos 10 entradas con diferentes usuarios
2. Verificar que pandas y matplotlib estén instalados:
```bash
pip install pandas matplotlib seaborn
```

### ❌ Imágenes de gráficos no cargan

**Causa:** Backend no puede generar PNGs.

**Solución:**
```bash
# Verificar instalación de dependencias de visualización
pip install matplotlib seaborn pillow
```

---

## 🗄️ Problemas de Base de Datos

### ❌ "No such table: entries"

**Causa:** Base de datos no inicializada.

**Solución:**
```bash
cd mood-keeper
python -c "from app.database import init_db; init_db(); print('✅ DB creada')"
```

### ❌ "Duplicate entry" al migrar CSV

**Causa:** Datos ya fueron migrados previamente.

**Solución:**
```python
# El script de migración ya maneja duplicados
# Si necesitas reiniciar:
rm data/mood_keeper.db
python migrate_to_db.py
```

### ❌ Datos CSV no aparecen en dashboard

**Causa:** Datos no fueron migrados a SQLite.

**Solución:**
```bash
cd mood-keeper
python migrate_to_db.py
# Responder 's' para continuar
```

---

## 🔐 Problemas de Autenticación

### ❌ "Invalid credentials"

**Causa:** Usuario/contraseña incorrectos.

**Solución:**
1. Verificar handle (case-sensitive)
2. Registrar nuevo usuario si olvidaste credenciales
3. Verificar en `data/accounts.csv` o base de datos

### ❌ Token expira muy rápido

**Causa:** Configuración de expiración en `security.py`.

**Solución:**
```python
# En app/security.py, aumentar EXPIRE_MINUTES:
EXPIRE_MINUTES = 60  # 1 hora
# o
EXPIRE_MINUTES = 1440  # 24 horas
```

---

## 🔥 Errores Críticos

### ❌ "Internal Server Error" (500)

**Solución:**
1. Revisar logs del backend en la terminal
2. Verificar que todos los campos requeridos estén presentes
3. Verificar permisos de escritura en `data/`

### ❌ Backend se cierra inmediatamente

**Solución:**
```bash
# Ejecutar manualmente para ver error:
cd mood-keeper
python main.py

# Ver traceback completo
```

### ❌ "Permission denied" al escribir en data/

**Solución:**
```bash
# Windows (como administrador):
icacls "data" /grant Users:F /T

# Linux/Mac:
chmod -R 755 data/
```

---

## 📱 Problemas del Navegador

### ❌ LocalStorage no funciona

**Causa:** Modo incógnito o cookies bloqueadas.

**Solución:**
1. Usar modo normal (no incógnito)
2. Habilitar cookies en configuración
3. Probar otro navegador (Chrome, Firefox)

### ❌ Estilos no se aplican

**Causa:** Bootstrap no carga o styles.css no encontrado.

**Solución:**
1. Verificar conexión a internet (Bootstrap CDN)
2. Verificar que `styles.css` exista en `frontend/`
3. Limpiar caché del navegador (Ctrl+Shift+R)

---

## 🆘 Solución Nuclear (Reiniciar Todo)

Si nada funciona:

```bash
# 1. Desactivar entorno virtual
deactivate

# 2. Eliminar entorno virtual
rm -rf .venv  # Linux/Mac
rmdir /s .venv  # Windows

# 3. Recrear entorno
python -m venv .venv

# 4. Activar
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows

# 5. Instalar dependencias
cd mood-keeper
pip install -r requirements.txt

# 6. Recrear base de datos
rm data/mood_keeper.db
python -c "from app.database import init_db; init_db()"

# 7. Ejecutar
python main.py
```

---

## 📞 Contacto y Soporte

**Repositorio:** https://github.com/JacobzCode/ProyectoCarlosCano

**Issues:** https://github.com/JacobzCode/ProyectoCarlosCano/issues

**Documentación:**
- [GUIA_INSTALACION.md](GUIA_INSTALACION.md)
- [README.md](README.md)
- [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)

---

## ✅ Checklist de Diagnóstico

Antes de reportar un problema, verifica:

- [ ] Python 3.8+ instalado (`python --version`)
- [ ] Entorno virtual activado (prompt con `(.venv)`)
- [ ] Dependencias instaladas (`pip list`)
- [ ] Backend corriendo (http://127.0.0.1:8001)
- [ ] Puerto 8001 libre (`netstat -ano | findstr :8001`)
- [ ] Base de datos existe (`data/mood_keeper.db`)
- [ ] Permisos de escritura en `data/`
- [ ] Navegador actualizado
- [ ] Sin errores en consola del navegador (F12)
- [ ] Sin errores en terminal del backend

---

**Última actualización:** Noviembre 2025  
**Versión del documento:** 1.0
