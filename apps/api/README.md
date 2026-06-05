# Nat 1 API

Backend foundation for Nat 1 RPG Engine.

This stage provides the FastAPI base, health check, settings, SQLAlchemy session setup, Alembic structure, security helpers, core database models, basic authentication, initial Game Project CRUD, workspace foundation endpoints, and tests. It does not implement AI/RAG, uploads, players, internal content module CRUD, or frontend.

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

## Banco Local Com Docker

1. Na raiz do projeto, suba o PostgreSQL local:

```powershell
docker compose up -d
```

2. Em `apps/api`, crie o arquivo `.env` local:

```powershell
Copy-Item .env.example .env
```

3. Confira no `.env`:

```env
DATABASE_URL=postgresql+psycopg://nat1_user:nat1_password@localhost:5432/nat1_db
```

4. Ative a virtualenv:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Aplique as migrations:

```powershell
alembic upgrade head
```

6. Suba a API:

```powershell
uvicorn app.main:app --reload
```

7. Teste:

```txt
GET http://127.0.0.1:8000/api/v1/health
POST http://127.0.0.1:8000/api/v1/auth/register
```

## Authentication

Register a user:

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/register `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"name":"Gabriel","email":"gabriel@example.com","password":"strong-password"}'
```

Login with OAuth2 form data:

```powershell
$login = Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/login `
  -Method Post `
  -ContentType "application/x-www-form-urlencoded" `
  -Body "username=gabriel@example.com&password=strong-password"
```

Use the Bearer token:

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/auth/me `
  -Headers @{ Authorization = "Bearer $($login.access_token)" }
```

Authentication notes:

- Passwords are stored only as hashes.
- API responses never return `password_hash`.
- The login endpoint uses OAuth2 form data.
- In Swagger, click `Authorize`, use the user's email in `username`, and use the password in `password`.

## Campanhas & Cronicas / Game Projects

The API uses the technical name `GameProject` for the product concept shown to users as Campanhas & Cronicas.

All Game Project routes require Bearer authentication:

```powershell
$headers = @{ Authorization = "Bearer $($login.access_token)" }
```

Create a Game Project:

```powershell
$project = Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/game-projects `
  -Method Post `
  -ContentType "application/json" `
  -Headers $headers `
  -Body '{"name":"Aelthos - A Dama de Ferro","format":"Campanha","description":"Campanha principal."}'
```

List active Game Projects:

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/game-projects `
  -Headers $headers
```

Include archived Game Projects:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects?include_archived=true" `
  -Headers $headers
```

Get, update, archive, and restore:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)" `
  -Headers $headers

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)" `
  -Method Patch `
  -ContentType "application/json" `
  -Headers $headers `
  -Body '{"description":"Descricao revisada.","status":"active"}'

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)/archive" `
  -Method Post `
  -Headers $headers

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)/restore" `
  -Method Post `
  -Headers $headers
```

Game Project notes:

- `slug` is generated automatically and is unique per user.
- New projects default to `status = "preparation"` and `theme = "cartographer"`.
- Archive is used instead of permanent deletion.
- Default module settings are created for each new project.

## Workspace Foundation

Workspace endpoints also require Bearer authentication with `$headers`.

Create and list Worlds:

```powershell
$world = Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/worlds `
  -Method Post `
  -ContentType "application/json" `
  -Headers $headers `
  -Body '{"name":"Aelthos","description":"Mundo autoral de fantasia sombria."}'

Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/worlds `
  -Headers $headers
```

Create and list System Templates:

```powershell
$template = Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/system-templates `
  -Method Post `
  -ContentType "application/json" `
  -Headers $headers `
  -Body '{"name":"Sistema Aelthos","type":"custom"}'

Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/v1/system-templates `
  -Headers $headers
```

Link a World or System Template to a Game Project:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)" `
  -Method Patch `
  -ContentType "application/json" `
  -Headers $headers `
  -Body "{`"world_id`":`"$($world.id)`",`"system_template_id`":`"$($template.id)`"}"
```

List and update Game Project modules:

```powershell
$modules = Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)/modules" `
  -Headers $headers

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)/modules/$($modules[0].id)" `
  -Method Patch `
  -ContentType "application/json" `
  -Headers $headers `
  -Body '{"display_name":"Painel","is_enabled":true,"order_index":5,"icon_key":"panel-top"}'
```

Get the Game Project summary for the future dashboard:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/v1/game-projects/$($project.id)/summary" `
  -Headers $headers
```

Workspace notes:

- Worlds and user-created System Templates are isolated by authenticated user.
- Built-in System Templates can be listed and read, but not edited or archived by regular users in this phase.
- Game Project summary returns zero counters until the internal modules are implemented.
- Module reorder in batch is intentionally left for a later task; individual `order_index` updates are available.

## Tests

```powershell
pytest
```

## Database Migrations

Create a new migration after model changes:

```powershell
alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```powershell
alembic upgrade head
```

Rollback the latest migration, if needed:

```powershell
alembic downgrade -1
```

Return to an empty schema, if needed:

```powershell
alembic downgrade base
```

## Code Quality

```powershell
ruff check .
```

## Notes

- Settings are loaded with `pydantic-settings`.
- Database access is prepared with SQLAlchemy and `SessionLocal`.
- Alembic is configured for versioned migrations.
- `SystemTemplate.owner_user_id` is nullable by design. Built-in templates belong to the product, not to a specific user; custom templates should set `owner_user_id`.
- Authentication is intentionally basic in this stage: register, login, JWT access token, and current-user lookup.
