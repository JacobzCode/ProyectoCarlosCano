#!/usr/bin/env python3
"""MoodKeeper entrypoint"""
from uvicorn import run
from app.database import init_db

if __name__ == '__main__':
    print('Starting MoodKeeper...')
    print('Initializing database...')
    init_db()
    print('✅ Database ready')
    run('app.server:app', host='127.0.0.1', port=8001, reload=True)
