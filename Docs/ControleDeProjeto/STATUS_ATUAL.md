# Status Atual

## Identificacao

Projeto: Nat 1 RPG Engine  
Fase atual: MVP 1 - Fundacao Backend  
Data da ultima atualizacao: 2026-06-05  
Branch atual: `back/auth-foundation`

## Tarefa Atual

Compatibilizar autenticacao com Swagger OAuth2 usando `OAuth2PasswordRequestForm`.

## Ultima Tarefa Concluida

Autenticacao basica validada com banco PostgreSQL local e ajustada para funcionar com o botao Authorize do Swagger.

## Arquivos Principais Alterados

- `apps/api/app/api/v1/endpoints/auth.py`
- `apps/api/app/schemas/auth.py`
- `apps/api/app/schemas/__init__.py`
- `apps/api/tests/test_auth.py`
- `apps/api/requirements.txt`
- `apps/api/README.md`
- `Docs/ControleDeProjeto/STATUS_ATUAL.md`

Arquivos ainda alterados da tarefa anterior de ambiente local:

- `docker-compose.yml`
- `apps/api/.env.example`
- `README.md`
- `apps/api/alembic.ini`
- `Docs/ControleDeProjeto/HISTORICO_TECNICO.md`

## Ultimos Testes Executados

```powershell
cd apps/api
ruff check .
pytest
```

Validacao HTTP registrada anteriormente com banco local:

```txt
GET /api/v1/health
POST /api/v1/auth/register
POST /api/v1/auth/login
GET /api/v1/auth/me
```

## Resultado Dos Testes

Autenticacao validada com banco local. Login ajustado para o padrao OAuth2 do Swagger, usando `username` como e-mail e `password` como senha.

Endpoint validado:

```txt
GET /api/v1/health
```

Resultado esperado:

```json
{"status":"ok","service":"nat1-api"}
```

Fluxos de autenticacao validados:

- Cadastro cria usuario e nao retorna `password_hash`.
- Cadastro duplicado retorna erro.
- Login OAuth2 com `username=email` e senha correta retorna JWT.
- Login com senha errada retorna 401.
- `/api/v1/auth/me` retorna usuario com Bearer token valido.
- `/api/v1/auth/me` retorna 401 sem token.

## Proxima Tarefa Recomendada

Seguir para CRUD de Projetos de Jogo ou fazer revisao final/commit da `auth foundation`.

Tarefa recomendada:

```txt
back/game-project-crud
```

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado para a proxima etapa.

Observacao: para testar pelo Swagger, o PostgreSQL local deve estar rodando, as migrations devem estar aplicadas e o `uvicorn` deve ser reiniciado depois de mudancas no `.env`.

## Observacoes Importantes

- MVP 1 e organizacional.
- Nao implementar IA pesada, RAG, jogadores, chat, mapas interativos avancados ou upload inteligente neste momento.
- O frontend ainda nao foi iniciado.
- A documentacao oficial de produto esta em `Docs/Documento_tecnico/`.
- O guia visual oficial esta em `Docs/IdentidadeVisual/`.
- Toda tarefa futura do Codex deve atualizar este arquivo ao final.
