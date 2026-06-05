# Status Atual

## Identificação

Projeto: Nat 1 RPG Engine  
Fase atual: MVP 1 - Fundação Backend  
Data da última atualização: 2026-06-05  
Branch atual: `back/auth-foundation`

## Última Tarefa Concluída

Fundação de autenticação básica do backend com cadastro, login, JWT e rota de usuário autenticado.

## Arquivos Principais Alterados

- `apps/api/app/core/security.py`
- `apps/api/app/api/deps.py`
- `apps/api/app/api/v1/endpoints/auth.py`
- `apps/api/app/api/v1/router.py`
- `apps/api/app/schemas/auth.py`
- `apps/api/app/schemas/user.py`
- `apps/api/app/repositories/user_repository.py`
- `apps/api/app/services/auth_service.py`
- `apps/api/tests/test_auth.py`
- `apps/api/README.md`

## Últimos Testes Executados

```powershell
cd apps/api
ruff check .
pytest
```

Validação HTTP registrada:

```txt
GET /api/v1/health
POST /api/v1/auth/register
POST /api/v1/auth/login
GET /api/v1/auth/me
```

## Resultado Dos Testes

Última validação técnica registrada: passando.

Endpoint validado:

```txt
GET /api/v1/health
```

Resultado esperado:

```json
{"status":"ok","service":"nat1-api"}
```

Fluxos de autenticação validados:

- Cadastro cria usuário e não retorna `password_hash`.
- Cadastro duplicado retorna erro.
- Login com senha correta retorna JWT.
- Login com senha errada retorna 401.
- `/api/v1/auth/me` retorna usuário com Bearer token válido.
- `/api/v1/auth/me` retorna 401 sem token.

## Próxima Tarefa Recomendada

Seguir para CRUD de Projetos de Jogo.

Tarefa recomendada:

```txt
back/game-project-crud
```

## Bloqueios Atuais

Nenhum bloqueio técnico registrado para a próxima etapa.

## Observações Importantes

- MVP 1 é organizacional.
- Não implementar IA pesada, RAG, jogadores, chat, mapas interativos avançados ou upload inteligente neste momento.
- O frontend ainda não foi iniciado.
- A documentação oficial de produto está em `Docs/Documento_tecnico/`.
- O guia visual oficial está em `Docs/IdentidadeVisual/`.
- Toda tarefa futura do Codex deve atualizar este arquivo ao final.
