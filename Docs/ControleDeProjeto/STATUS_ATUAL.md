# Status Atual

## Identificacao

Projeto: Nat 1 RPG Engine  
Fase atual: MVP 1 - Fundacao Backend  
Data da ultima atualizacao: 2026-06-05  
Branch atual: `back/game-project-crud`

## Tarefa Atual

Criar o CRUD inicial autenticado de Projetos de Jogo, exibidos no produto como Campanhas & Cronicas.

## Ultima Tarefa Concluida

CRUD inicial de `GameProject` implementado com rotas protegidas, isolamento por usuario, slug unico por usuario, modulos padrao e arquivamento sem exclusao permanente.

## Arquivos Principais Alterados

- `apps/api/app/api/v1/endpoints/game_projects.py`
- `apps/api/app/api/v1/router.py`
- `apps/api/app/schemas/game_project.py`
- `apps/api/app/schemas/__init__.py`
- `apps/api/app/repositories/game_project_repository.py`
- `apps/api/app/repositories/__init__.py`
- `apps/api/app/services/game_project_service.py`
- `apps/api/app/services/__init__.py`
- `apps/api/tests/test_game_projects.py`
- `apps/api/README.md`
- `Docs/ControleDeProjeto/STATUS_ATUAL.md`
- `Docs/ControleDeProjeto/HISTORICO_TECNICO.md`
- `Docs/ControleDeProjeto/PROXIMAS_TAREFAS_CODEX.md`

## Ultimos Testes Executados

```powershell
cd apps/api
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest
```

Validacoes cobertas por testes automatizados:

```txt
GET /api/v1/health
POST /api/v1/auth/register
POST /api/v1/auth/login
GET /api/v1/auth/me
POST /api/v1/game-projects
GET /api/v1/game-projects
GET /api/v1/game-projects/{project_id}
PATCH /api/v1/game-projects/{project_id}
POST /api/v1/game-projects/{project_id}/archive
POST /api/v1/game-projects/{project_id}/restore
```

## Resultado Dos Testes

`ruff check .` passou.

`pytest` passou com 17 testes:

- autenticacao basica preservada;
- health check preservado;
- criacao autenticada de Projeto de Jogo;
- bloqueio de criacao sem token;
- listagem isolada por usuario;
- bloqueio de acesso a projeto de outro usuario;
- atualizacao pelo dono;
- arquivamento ocultando da lista padrao;
- `include_archived=true` retornando arquivados;
- restore recolocando o projeto na lista padrao;
- slugs duplicados recebendo sufixo por usuario.

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

Seguir para endpoints simples de Worlds e SystemTemplates, aproveitando os models centrais ja existentes.

Tarefa recomendada:

```txt
back/world-system-templates
```

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado para a proxima etapa.

Para teste manual pelo Swagger, manter o PostgreSQL local rodando, migrations aplicadas e login feito pelo botao Authorize com `username=email`.

## Observacoes Importantes

- MVP 1 continua organizacional.
- Nao implementar IA pesada, RAG, jogadores, chat, mapas interativos avancados ou upload inteligente neste momento.
- O frontend ainda nao foi iniciado.
- A documentacao oficial de produto esta em `Docs/Documento_tecnico/`.
- O guia visual oficial esta em `Docs/IdentidadeVisual/`.
- Toda tarefa futura do Codex deve atualizar este arquivo ao final.
