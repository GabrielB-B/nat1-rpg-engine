# Nat 1 RPG Engine

Nat 1 RPG Engine is a web application for RPG masters and narrators to preserve the
operation and continuity of tabletop RPG campaigns.

The current MVP is intentionally vertical: campaign → session → scenes → occurrences →
recap → pending items. Characters, locations, relationships, documents, players, PDF,
AI/RAG, chat and advanced maps remain behind later validation gates.

## Official Documentation

The product, architecture, roadmap and visual decisions live in:

- `Docs/ControleDeProjeto/`
- `Docs/Documento_tecnico/`
- `Docs/IdentidadeVisual/`

Document authority is explicit:

- `Docs/ControleDeProjeto/STATUS_ATUAL.md` records verified current facts;
- `Docs/ControleDeProjeto/PROXIMAS_TAREFAS_CODEX.md` is the only executable queue;
- `Docs/ControleDeProjeto/VALIDACAO_PRODUTO_E_ESTRATEGIA_DADOS.md` and
  `Docs/ControleDeProjeto/ESCOPO_MVP_VERTICAL_E_GATES.md` govern product and scope;
- `Docs/ControleDeProjeto/ARQUITETURA_C4_E_DEPLOYMENT.md` and
  `Docs/ControleDeProjeto/MODELO_DE_AMEACAS_AUTORIZACAO_E_LGPD.md` govern the architecture baseline;
- checkpoints, history and PDFs preserve earlier decisions but do not override newer,
  dated addenda.

## Current Stage

This repository currently contains the backend foundation in `apps/api`, using:

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic Settings
- JWT authentication
- `bcrypt_sha256` password hashing with opportunistic legacy bcrypt migration
- protected Game Project, World and System Template endpoints

The frontend foundation is active in `apps/web`, using:

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- TanStack Query

The current frontend includes the Cartographer foundation, login/register, protected
routing, API integration and the first real Campanhas & Crônicas screen. The Home do
Mestre is still a visual mock and must be replaced with real data after the current
security branch is reviewed and integrated.

The active branch `security/baseline-hardening` now contains PostgreSQL integration
coverage and CI configuration, but the project protocol requires Gabriel's approval
before commit, Pull Request and integration.

## Backend Commands

```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
Copy-Item .env.example .env
pip install -r requirements.lock
uvicorn app.main:app --reload
pytest
ruff check .
```

Health check:

```txt
GET http://127.0.0.1:8000/api/v1/health
```

## Frontend Commands

```powershell
cd apps/web
npm ci
Copy-Item .env.example .env
npm run dev
npm run lint
npm test
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
docker compose up -d --wait
```

Check whether the container is running:

```powershell
docker compose ps
```

Stop the local database:

```powershell
docker compose down
```

Remove the local database volume only when you intentionally want to erase local data:

```powershell
docker compose down -v
```
