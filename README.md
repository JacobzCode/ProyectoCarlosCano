# Mood Keeper - Proyecto Carlos Cano

Plataforma web para monitorear el estado emocional y mental de jóvenes en contextos vulnerables, integrando herramientas de análisis de datos con Python para identificar patrones de riesgo, generar alertas tempranas y ofrecer recursos de apoyo.

## 📋 Descripción

Mood Keeper es una aplicación completa que permite a los usuarios:
- ✅ Registrar su estado de ánimo diario (escala 1-10)
- ✅ Monitorear hábitos (sueño, ejercicio, alimentación, socialización)
- ✅ Visualizar tendencias y patrones emocionales
- ✅ Recibir alertas tempranas de riesgo
- ✅ Acceder a recursos personalizados de apoyo

## 🏗️ Estructura del Proyecto

```
ProyectoCarlosCano/
├── frontend/          # Aplicación web frontend
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── app.js
│   └── styles.css
└── mood-keeper/       # Backend API
    ├── main.py
    ├── requirements.txt
    ├── app/
    │   ├── server.py
    │   ├── storage.py
    │   ├── security.py
    │   ├── insights.py
    │   └── dto.py
    └── data/
        ├── accounts.csv
        └── entries.csv
```

## 🚀 Instalación y Configuración

### Backend (mood-keeper)

1. Navegar al directorio del backend:
```bash
cd mood-keeper
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar el servidor:
```bash
python main.py
```

El servidor estará disponible en `http://localhost:5000`

### Frontend

1. Navegar al directorio del frontend:
```bash
cd frontend
```

2. Abrir `index.html` en un navegador web o usar un servidor local:
```bash
# Opción con Python
python -m http.server 8000

# Opción con Node.js
npx http-server
```

El frontend estará disponible en `http://localhost:8000`

## 🔧 Tecnologías

- **Backend**: Python, FastAPI, SQLAlchemy
- **Base de Datos**: SQLite (migrable a PostgreSQL)
- **Análisis de Datos**: Pandas, NumPy
- **Visualización**: Matplotlib, Seaborn, Chart.js
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5
- **Seguridad**: JWT tokens, bcrypt hashing
- **Testing**: pytest

## 📝 Características

### Funcionalidades Principales
- ✅ **Registro y autenticación** con seguridad JWT
- ✅ **Registro de mood** (1-10) con comentarios
- ✅ **Monitoreo de hábitos**: sueño, ejercicio, alimentación, socialización
- ✅ **Dashboard interactivo** con múltiples visualizaciones
- ✅ **Análisis de datos** con Pandas (estadísticas descriptivas, correlaciones)
- ✅ **Detección de riesgo** con algoritmo multifactorial
- ✅ **Alertas tempranas** basadas en scoring de riesgo (0-100)
- ✅ **Recursos personalizados** según estado emocional
- ✅ **Visualizaciones avanzadas**: histogramas, boxplots, time series
- ✅ **API RESTful** documentada y escalable

### Tipos de Gráficos
- 📊 Gráficos de barras (comparación por usuario)
- 📈 Series temporales (evolución de mood)
- 📉 Histogramas (distribución de estados)
- 📦 Boxplots (variabilidad individual)
- 🥧 Gráficos circulares y donut
- 🎯 Scatter plots (correlaciones)

## 🧪 Testing

Ejecutar tests unitarios:
```bash
cd mood-keeper
pytest tests/ -v
```

Tests disponibles:
- `test_security.py`: Validación de hashing y tokens
- `test_storage_db.py`: Operaciones CRUD en base de datos
- `test_insights.py`: Funciones de análisis y visualización

## 📚 Documentación Adicional

- [ANÁLISIS DEL PROYECTO](ANALISIS_PROYECTO.md) - Comparación con requisitos
- [INFORME SEGUNDA ENTREGA](INFORME_SEGUNDA_ENTREGA.md) - Gestión y análisis de datos
- [INFORME TERCERA ENTREGA](INFORME_TERCERA_ENTREGA.md) - Dashboard y visualización

## 🎯 Proyecto Integrador

Este proyecto cumple con los requisitos del **Proyecto Integrador** del módulo de Nuevas Tecnologías:

### Primera Entrega ✅
- ✅ Repositorio en GitHub organizado
- ✅ Scripts de registro de usuarios
- ✅ Manejo de archivos CSV/SQLite
- ✅ Control de versiones con Git
- ✅ Código modular y documentado

### Segunda Entrega ✅
- ✅ Base de datos SQLite con SQLAlchemy
- ✅ Limpieza y transformación de datos
- ✅ Análisis exploratorio con Pandas
- ✅ Visualizaciones con Matplotlib/Seaborn
- ✅ Algoritmo de detección de riesgo

### Tercera Entrega ✅
- ✅ Dashboard funcional con múltiples gráficos
- ✅ Estado emocional promedio por grupo
- ✅ Sistema de alertas con scoring
- ✅ Evolución temporal del bienestar
- ✅ Recursos de apoyo personalizados

## 📄 Licencia

Este proyecto es de uso educativo.

## 👤 Autor

**Carlos Cano**  
Proyecto Integrador - Nuevas Tecnologías  
2025
