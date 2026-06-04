# Nat 1 API

Backend foundation for Nat 1 RPG Engine.

This stage provides only the FastAPI base, health check, settings, SQLAlchemy session setup, Alembic structure, security helpers, and tests. It does not implement business models, authentication routes, AI/RAG, uploads, players, or frontend.

## Requirements

- Python 3.12+
- PostgreSQL for future database-backed features

## Setup

```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
```

Create a local environment file:

```powershell
Copy-Item .env.example .env
```

Update `.env` with local values. Do not commit `.env`.

## Run API

```powershell
uvicorn app.main:app --reload
```

Health check:

```txt
GET http://127.0.0.1:8000/api/v1/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "nat1-api"
}
```

## Tests

```powershell
pytest
```

## Code Quality

```powershell
ruff check .
```

## Notes

- Settings are loaded with `pydantic-settings`.
- Database access is prepared with SQLAlchemy and `SessionLocal`, but no models are implemented yet.
- Alembic is configured for future migrations.
- Security helpers include password hashing and JWT token creation helpers, but no authentication flow is implemented in this stage.
