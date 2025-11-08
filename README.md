# Mood Keeper - Proyecto Carlos Cano

Aplicación web completa para el seguimiento del estado de ánimo con backend en Python (Flask) y frontend en HTML/CSS/JavaScript.

## 📋 Descripción

Mood Keeper es una aplicación que permite a los usuarios registrar y hacer seguimiento de su estado de ánimo diario, incluyendo funcionalidades de autenticación, registro de entradas y análisis de insights.

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

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Almacenamiento**: CSV (archivos planos)
- **Seguridad**: Hashing de contraseñas, tokens de sesión

## 📝 Características

- ✅ Registro e inicio de sesión de usuarios
- ✅ Creación de entradas de estado de ánimo
- ✅ Dashboard con visualización de entradas
- ✅ Perfil de usuario
- ✅ Insights y análisis de estados de ánimo
- ✅ API RESTful

## 📄 Licencia

Este proyecto es de uso educativo.

## 👤 Autor

Carlos Cano
