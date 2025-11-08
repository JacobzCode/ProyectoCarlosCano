@echo off
REM Script de inicio rápido para Mood Keeper
REM Windows PowerShell / CMD

echo ========================================
echo    MOOD KEEPER - INICIO RAPIDO
echo ========================================
echo.

REM Activar entorno virtual
echo [1/3] Activando entorno virtual...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    echo Ejecuta: python -m venv .venv
    pause
    exit /b 1
)

echo [2/3] Iniciando backend en mood-keeper...
cd mood-keeper
start "Mood Keeper Backend" cmd /k "python main.py"

echo [3/3] Esperando 3 segundos...
timeout /t 3 /nobreak > nul

echo.
echo ========================================
echo    MOOD KEEPER INICIADO
echo ========================================
echo.
echo Backend: http://127.0.0.1:8001
echo.
echo Para iniciar el frontend, ejecuta:
echo    cd frontend
echo    python -m http.server 8000
echo.
echo Presiona Ctrl+C en la ventana del backend para detenerlo
echo.
pause
