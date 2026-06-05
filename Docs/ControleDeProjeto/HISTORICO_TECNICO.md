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

### 2026-06-05 - PostgreSQL Local Com Docker

- Adicionado Docker Compose para PostgreSQL local de desenvolvimento.
- Banco padrão local: `nat1_db`.
- Usuário local: `nat1_user`.
- Serviço/container: `nat1_postgres`.
- `DATABASE_URL` documentada em `apps/api/.env.example`.
- Fluxo local documentado: subir Docker, copiar `.env`, aplicar Alembic e retestar autenticação pelo Swagger.

### 2026-06-05 - CRUD Inicial De Projetos De Jogo

- Criadas rotas protegidas para criar, listar, detalhar, atualizar, arquivar e restaurar `GameProject`.
- Mantida a equivalencia de produto: interface usa Campanhas & Cronicas; backend usa Projeto de Jogo / `GameProject`.
- Implementado isolamento por usuario autenticado em todas as consultas.
- Slugs sao gerados automaticamente e mantidos unicos por usuario.
- Novos projetos usam `status` inicial `preparation` e tema padrao `cartographer`.
- Criadas configuracoes iniciais de modulos por projeto em `project_module_settings`.
- Arquivamento foi implementado como soft delete com `archived_at`.
- Testes automatizados cobrem criacao, isolamento, atualizacao, arquivamento, restore, autenticacao e health check.

## Restrições De Escopo Mantidas

- Não implementar frontend antes da fase própria.
- Não implementar IA/RAG no MVP 1 inicial.
- Não implementar jogadores ou permissões avançadas nesta fase.
- Não criar mapas interativos avançados no primeiro corte.
- Não adicionar CRUDs fora da tarefa ativa.
