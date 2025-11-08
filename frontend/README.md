# MoodKeeper Frontend

Multi-page frontend (HTML + vanilla JS) using Bootstrap + Chart.js that interacts with the MoodKeeper backend.

Pages:
- `index.html` — Landing / marketing page
- `register.html` — User registration
- `login.html` — Login
- `dashboard.html` — Main app dashboard (requires login)
- `profile.html` — Profile and recent history

Quick start:
1. Ensure MoodKeeper backend is running (`python main.py`) on port 8001.
2. Serve the `frontend/` folder (recommended) or open `index.html` directly. To serve with Python:

```powershell
# from the workspace root
python -m http.server 5500 -d frontend
# then open http://127.0.0.1:5500
```

Notes:
- Authentication: login stores a Bearer token in localStorage (for demo only).
- Charts: the dashboard uses backend JSON endpoints; PNG plots require server-side analytics libs (optional).
- This is a demo frontend — do not use as-is in production.
