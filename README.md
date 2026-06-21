# Nat 1 RPG Engine

Nat 1 RPG Engine is a web application for RPG masters and narrators to organize campaigns, chronicles, worlds, sessions, scenes, characters, creatures, locations, factions, documents, notes, and relationships.

The MVP 1 is organizational only. It does not include AI/RAG, player access, chat, or advanced interactive maps in this stage.

## Official Documentation

The product, architecture, roadmap and visual decisions live in:

- `Docs/ControleDeProjeto/`
- `Docs/Documento_tecnico/`
- `Docs/IdentidadeVisual/`

These documents are the source of truth for product scope, business rules, non-functional requirements, architecture, checkpoints, data modeling, engineering standards and visual identity.

## Current Stage

This repository currently contains the backend foundation in `apps/api`, using:

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic Settings
- JWT authentication
- bcrypt password hashing
- protected Game Project, World and System Template endpoints

The frontend foundation is active in `apps/web`, using:

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- TanStack Query

The current frontend includes the Cartographer design system foundation, login/register routes, protected routing, API integration and the first real Campanhas & Crônicas screen. The Home do Mestre is still a mocked visual shell and is scheduled to consume real account data in `front/home-master-real-data`.

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
