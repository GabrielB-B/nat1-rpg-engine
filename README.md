# Nat 1 RPG Engine

Nat 1 RPG Engine is a web application for RPG masters and narrators to organize campaigns, chronicles, worlds, sessions, scenes, characters, creatures, locations, factions, documents, notes, and relationships.

The MVP 1 is organizational only. It does not include AI/RAG, player access, chat, or advanced interactive maps in this stage.

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

The frontend foundation is now started in `apps/web`, using:

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- TanStack Query

The first frontend design system foundation is also in place with the Cartographer theme, reusable UI/layout/dashboard components and a mocked Workspace do Mestre shell.

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

## Frontend Commands

```powershell
cd apps/web
npm install
Copy-Item .env.example .env
npm run dev
npm run typecheck
npm run build
```

Frontend local URL:

```txt
http://127.0.0.1:5173
```

## Local Database

Start the local PostgreSQL database:

```powershell
docker compose up -d
```

Check whether the container is running:

```powershell
docker ps
```

Stop the local database:

```powershell
docker compose down
```

Remove the local database volume only when you intentionally want to erase local data:

```powershell
docker compose down -v
```
