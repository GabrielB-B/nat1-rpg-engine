# Histórico Técnico

Este arquivo registra decisões técnicas e marcos relevantes do Nat 1 RPG Engine.

## Registros Iniciais

- Decidido usar monorepo com `apps/api` e futuramente `apps/web`.
- Backend iniciado com FastAPI, SQLAlchemy, Alembic e PostgreSQL.
- Frontend será React + TypeScript + Vite, mas ainda não foi iniciado.
- MVP 1 é organizacional, sem IA pesada, RAG, jogadores, chat ou mapas interativos.
- Documentação oficial está em `Docs/Documento_tecnico`.
- Guia visual oficial está em `Docs/IdentidadeVisual`.
- Branches devem ser pequenas e por tarefa.

## Marcos Técnicos

### 2026-06-05 - Fundação Backend

- Criada estrutura inicial em `apps/api`.
- Criado endpoint `GET /api/v1/health`.
- Configurados settings com `pydantic-settings`.
- Preparada base SQLAlchemy e sessão de banco.
- Preparado Alembic.
- Criados README inicial e `.gitignore`.
- Validação registrada com `pytest`, `ruff check .` e health check HTTP.

### 2026-06-05 - Fundação De Autenticação

- Criados schemas de usuário, login, token e payload JWT.
- Criados repository e service para usuário/autenticação.
- Criadas rotas `POST /api/v1/auth/register`, `POST /api/v1/auth/login` e `GET /api/v1/auth/me`.
- Criada dependência `get_current_user` com Bearer token.
- Senhas são salvas apenas com hash seguro.
- API não retorna `password_hash`.
- Testes de cadastro, login e usuário autenticado adicionados.

## Restrições De Escopo Mantidas

- Não implementar frontend antes da fase própria.
- Não implementar IA/RAG no MVP 1 inicial.
- Não implementar jogadores ou permissões avançadas nesta fase.
- Não criar mapas interativos avançados no primeiro corte.
- Não adicionar CRUDs fora da tarefa ativa.
