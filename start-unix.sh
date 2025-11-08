#!/bin/bash

# Script de inicio rápido para Mood Keeper
# Linux / macOS

echo "========================================"
echo "   MOOD KEEPER - INICIO RAPIDO"
echo "========================================"
echo ""

# Activar entorno virtual
echo "[1/3] Activando entorno virtual..."
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "❌ ERROR: No se encontró el entorno virtual"
    echo "Ejecuta: python3 -m venv .venv"
    exit 1
fi

# Iniciar backend
echo "[2/3] Iniciando backend..."
cd mood-keeper
python main.py &
BACKEND_PID=$!

echo "[3/3] Esperando 3 segundos..."
sleep 3

echo ""
echo "========================================"
echo "   MOOD KEEPER INICIADO"
echo "========================================"
echo ""
echo "✅ Backend: http://127.0.0.1:8001 (PID: $BACKEND_PID)"
echo ""
echo "Para iniciar el frontend, abre otra terminal y ejecuta:"
echo "    cd frontend"
echo "    python -m http.server 8000"
echo ""
echo "Para detener el backend:"
echo "    kill $BACKEND_PID"
echo ""
echo "Presiona Ctrl+C para salir"
echo ""

# Esperar a que el usuario presione Ctrl+C
wait $BACKEND_PID
