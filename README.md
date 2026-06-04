# Nat 1 RPG Engine

Nat 1 RPG Engine is a web application for RPG masters and narrators to organize campaigns, chronicles, worlds, sessions, scenes, characters, creatures, locations, factions, documents, notes, and relationships.

The MVP 1 is organizational only. It does not include frontend implementation, AI/RAG, player access, chat, or advanced interactive maps in this stage.

## Official Documentation

The product and visual decisions live in:

- `Docs/Documento_tecnico/`
- `Docs/IdentidadeVisual/`

These documents are the source of truth for product scope, business rules, non-functional requirements, initial data modeling, and visual identity.

## Current Stage

This repository currently contains the backend foundation in `apps/api`, using:

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic Settings

## Backend Commands

```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --reload
pytest
```

Health check:

```txt
GET http://127.0.0.1:8000/api/v1/health
```
