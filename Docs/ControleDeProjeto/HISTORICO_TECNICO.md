# Historico Tecnico

Este arquivo registra decisoes tecnicas e marcos relevantes do Nat 1 RPG Engine.

## Registros Iniciais

- Decidido usar monorepo com `apps/api` e futuramente `apps/web`.
- Backend iniciado com FastAPI, SQLAlchemy, Alembic e PostgreSQL.
- Frontend sera React + TypeScript + Vite, mas ainda nao foi iniciado.
- MVP 1 e organizacional, sem IA pesada, RAG, jogadores, chat ou mapas interativos.
- Documentacao oficial esta em `Docs/Documento_tecnico`.
- Guia visual oficial esta em `Docs/IdentidadeVisual`.
- Branches devem ser pequenas e por tarefa.

## Marcos Tecnicos

### 2026-06-05 - Fundacao Backend

- Criada estrutura inicial em `apps/api`.
- Criado endpoint `GET /api/v1/health`.
- Configurados settings com `pydantic-settings`.
- Preparada base SQLAlchemy e sessao de banco.
- Preparado Alembic.
- Criados README inicial e `.gitignore`.
- Validacao registrada com `pytest`, `ruff check .` e health check HTTP.

### 2026-06-05 - Fundacao De Autenticacao

- Criados schemas de usuario, login, token e payload JWT.
- Criados repository e service para usuario/autenticacao.
- Criadas rotas `POST /api/v1/auth/register`, `POST /api/v1/auth/login` e `GET /api/v1/auth/me`.
- Criada dependencia `get_current_user` com Bearer token.
- Senhas sao salvas apenas com hash seguro.
- API nao retorna `password_hash`.
- Testes de cadastro, login e usuario autenticado adicionados.

### 2026-06-05 - PostgreSQL Local Com Docker

- Adicionado Docker Compose para PostgreSQL local de desenvolvimento.
- Banco padrao local: `nat1_db`.
- Usuario local: `nat1_user`.
- Servico/container: `nat1_postgres`.
- `DATABASE_URL` documentada em `apps/api/.env.example`.
- Fluxo local documentado: subir Docker, copiar `.env`, aplicar Alembic e retestar autenticacao pelo Swagger.

### 2026-06-05 - CRUD Inicial De Projetos De Jogo

- Criadas rotas protegidas para criar, listar, detalhar, atualizar, arquivar e restaurar `GameProject`.
- Mantida a equivalencia de produto: interface usa Campanhas & Cronicas; backend usa Projeto de Jogo / `GameProject`.
- Implementado isolamento por usuario autenticado em todas as consultas.
- Slugs sao gerados automaticamente e mantidos unicos por usuario.
- Novos projetos usam `status` inicial `preparation` e tema padrao `cartographer`.
- Criadas configuracoes iniciais de modulos por projeto em `project_module_settings`.
- Arquivamento foi implementado como soft delete com `archived_at`.
- Testes automatizados cobrem criacao, isolamento, atualizacao, arquivamento, restore, autenticacao e health check.

### 2026-06-05 - Fundacao De Workspace

- Criado CRUD basico de `World`, representando Mundos / Cenarios do mestre.
- Criado CRUD basico de `SystemTemplate`, representando Sistemas & Templates customizados.
- Templates built-in permanecem preparados como registros sem dono e protegidos contra edicao por usuario comum.
- Criados endpoints para listar e atualizar modulos de um `GameProject` via `ProjectModuleSetting`.
- Criado endpoint de summary de `GameProject` para futuro Dashboard.
- Summary retorna dados principais do projeto, mundo vinculado, sistema/template vinculado, modulos ativos e contadores basicos.
- Contadores de sessoes, cenas, personagens/criaturas, locais, organizacoes/faccoes, documentos, notas e relacoes retornam zero ate os modulos internos existirem.
- Reforcado isolamento por usuario em Worlds, SystemTemplates privados, ProjectModuleSettings e GameProject Summary.
- Mantida validacao de vinculo: `GameProject` so aceita `world_id` do dono e `system_template_id` built-in ou do dono.
- Nenhuma migration foi criada porque os models centrais ja tinham os campos necessarios.

## Restricoes De Escopo Mantidas

- Nao implementar frontend antes da fase propria.
- Nao implementar IA/RAG no MVP 1 inicial.
- Nao implementar jogadores ou permissoes avancadas nesta fase.
- Nao criar mapas interativos avancados no primeiro corte.
- Nao adicionar CRUDs fora da tarefa ativa.
