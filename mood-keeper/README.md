# MoodKeeper

MoodKeeper es un microservicio para registrar usuarios y monitorear su estado emocional. Está pensado como un proyecto que reproduce las mismas capacidades que otro prototipo, pero con estructura y nombres distintos para facilitar compartirlo sin mostrar la misma organización.

Características principales:
- Registro / login / logout con JWT
- Persistencia sencilla en CSV (local)
- CRUD de encuestas de estado emocional (mood 1-10)
- Endpoints de análisis: resumen, promedio por grupo, alertas de riesgo, evolución temporal
- Visualizaciones PNG (opcional, requiere dependencias de analytics)

Estructura principal
- `main.py` - arranque (uvicorn)
- `requirements.txt` - dependencias principales
- `requirements-insights.txt` - dependencias opcionales para analytics
- `app/` - código fuente
  - `server.py` - rutas y app FastAPI
  - `security.py` - hashing y JWT
  - `storage.py` - CSV persistence (UserStore, EntryStore)
  - `dto.py` - Pydantic models
  - `insights.py` - EDA y plotting
- `data/` - CSVs (`accounts.csv`, `entries.csv`)

Instalación mínima:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Instalación opcional para analytics:
```powershell
pip install -r requirements-insights.txt
```

Ver `EXAMPLES.md` para ejemplos de uso.
