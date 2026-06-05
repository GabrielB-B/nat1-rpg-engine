# Status Atual

## Identificacao

Projeto: Nat 1 RPG Engine  
Fase atual: MVP 1 - Fundacao Backend  
Data da ultima atualizacao: 2026-06-05  
Branch atual: `back/workspace-foundation`

## Tarefa Atual

Criar a fundacao do workspace do mestre ao redor de Campanhas & Cronicas.

## Ultima Tarefa Concluida

Fundacao de workspace implementada com CRUD basico de Worlds, CRUD basico de SystemTemplates, leitura/atualizacao de modulos de GameProject e summary basico para futuro Dashboard.

## Arquivos Principais Alterados

- `apps/api/app/api/v1/endpoints/worlds.py`
- `apps/api/app/api/v1/endpoints/system_templates.py`
- `apps/api/app/api/v1/endpoints/game_projects.py`
- `apps/api/app/api/v1/router.py`
- `apps/api/app/core/slug.py`
- `apps/api/app/schemas/world.py`
- `apps/api/app/schemas/system_template.py`
- `apps/api/app/schemas/project_module_setting.py`
- `apps/api/app/schemas/game_project.py`
- `apps/api/app/repositories/world_repository.py`
- `apps/api/app/repositories/system_template_repository.py`
- `apps/api/app/repositories/project_module_setting_repository.py`
- `apps/api/app/repositories/game_project_repository.py`
- `apps/api/app/services/world_service.py`
- `apps/api/app/services/system_template_service.py`
- `apps/api/app/services/project_module_setting_service.py`
- `apps/api/app/services/game_project_service.py`
- `apps/api/tests/test_workspace_foundation.py`
- `apps/api/README.md`
- `Docs/ControleDeProjeto/STATUS_ATUAL.md`
- `Docs/ControleDeProjeto/HISTORICO_TECNICO.md`
- `Docs/ControleDeProjeto/PROXIMAS_TAREFAS_CODEX.md`

## Endpoints Criados Ou Ampliados

```txt
POST /api/v1/worlds
GET /api/v1/worlds
GET /api/v1/worlds/{world_id}
PATCH /api/v1/worlds/{world_id}
POST /api/v1/worlds/{world_id}/archive
POST /api/v1/worlds/{world_id}/restore

POST /api/v1/system-templates
GET /api/v1/system-templates
GET /api/v1/system-templates/{template_id}
PATCH /api/v1/system-templates/{template_id}
POST /api/v1/system-templates/{template_id}/archive

GET /api/v1/game-projects/{project_id}/modules
PATCH /api/v1/game-projects/{project_id}/modules/{module_setting_id}
GET /api/v1/game-projects/{project_id}/summary
```

## Ultimos Testes Executados

```powershell
cd apps/api
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest
```

## Resultado Dos Testes

`ruff check .` passou.

`pytest` passou com 25 testes:

- health check preservado;
- autenticacao OAuth2 preservada;
- CRUD inicial de GameProject preservado;
- Worlds com criacao, listagem, isolamento, update, archive e restore;
- SystemTemplates com criacao, listagem, isolamento, update e archive;
- templates built-in listaveis, mas protegidos contra edicao;
- modulos de GameProject listaveis e atualizaveis pelo dono;
- bloqueio de modulos de projeto de outro usuario;
- summary de GameProject protegido por dono;
- summary retorna modulos ativos e contadores basicos zerados;
- GameProject so aceita vincular World do dono;
- GameProject so aceita vincular SystemTemplate built-in ou do dono.

Aviso conhecido: `StarletteDeprecationWarning` do `TestClient` sobre `httpx`, sem falha de teste.

## Endpoint Validado

```txt
GET /api/v1/health
```

Resultado esperado:

```json
{"status":"ok","service":"nat1-api"}
```

## Proxima Tarefa Recomendada

Seguir para frontend foundation ou iniciar a fundacao de Sessoes e Cenas no backend.

Tarefas recomendadas:

```txt
front/setup-foundation
back/session-scene-foundation
```

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado para a proxima etapa.

Nao foi criada migration nesta tarefa porque os models/tabelas necessarios ja existiam.

## Observacoes Importantes

- MVP 1 continua organizacional.
- Nao implementar IA pesada, RAG, jogadores, chat, mapas interativos avancados ou upload inteligente neste momento.
- O frontend ainda nao foi iniciado.
- `ProjectModuleSettings` possui update individual; reorder em lote fica para uma tarefa futura.
- Contadores do summary retornam zero ate os modulos internos existirem.
- A documentacao oficial de produto esta em `Docs/Documento_tecnico/`.
- O guia visual oficial esta em `Docs/IdentidadeVisual/`.
- Toda tarefa futura do Codex deve atualizar este arquivo ao final.
