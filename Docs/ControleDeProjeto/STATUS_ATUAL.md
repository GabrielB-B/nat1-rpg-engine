# Status Atual

Projeto: Nat 1 RPG Engine

Fase atual: front/api-integration-foundation

Branch: front/api-integration-foundation

Status: concluida em validacao local

Data da ultima atualizacao: 2026-06-05

## Ultimas Entregas

- Implementada camada base de integracao com API no frontend.
- Adicionado tratamento padronizado de erros HTTP com `ApiError` e `ApiNetworkError`.
- Adicionado helper `withQueryParams` para montagem segura de query string.
- Adicionada configuracao central do API client para token Bearer salvo e callback de `401`.
- Mantida compatibilidade com `VITE_API_BASE_URL`.
- Ajustada autenticacao frontend para marcar login e cadastro como chamadas publicas.
- Adicionado logout automatico em respostas `401` de chamadas protegidas.
- Configurado TanStack Query para evitar retry em `401`, `403` e `404`.
- Criado hook `useCurrentUser`.
- Criados tipos, servicos e hooks de leitura para GameProjects.
- Criados tipos, servicos e hooks de leitura para Worlds.
- Criados tipos, servicos e hooks de leitura para SystemTemplates.
- Mantida a Home do Mestre como dashboard mockado, sem consumo real de dados pela tela.

## Estado Tecnico Do Produto

Backend concluido ate esta etapa:

- Fundacao FastAPI com PostgreSQL local via Docker.
- SQLAlchemy, Alembic e settings com `pydantic-settings`.
- Autenticacao com JWT.
- Swagger Authorize com OAuth2PasswordRequestForm usando `username` como e-mail.
- CRUD de GameProject / Campanhas & Cronicas.
- Workspace foundation com Worlds, SystemTemplates, ProjectModuleSettings e GameProject Summary.
- Testes automatizados com `pytest`.
- Validacao estatica com `ruff`.

Frontend concluido ate esta etapa:

- React, TypeScript, Vite, Tailwind CSS, React Router e TanStack Query.
- API client centralizado em `apps/web/src/lib/api/client.ts`.
- Tratamento de erro em `apps/web/src/lib/api/errors.ts`.
- Helper HTTP em `apps/web/src/lib/api/http.ts`.
- Design system inicial com componentes de UI, layout e dashboard.
- Home do Mestre mockada no tema `cartographer`.
- Telas de login e cadastro integradas aos endpoints reais de autenticacao local.
- Guardas basicos para rotas publicas e protegidas.
- Servicos e hooks de leitura preparados para consumo futuro de dados protegidos.

## Arquivos Principais Da Fase

- `apps/web/src/lib/api/client.ts`
- `apps/web/src/lib/api/errors.ts`
- `apps/web/src/lib/api/http.ts`
- `apps/web/src/lib/queryClient.ts`
- `apps/web/src/features/auth/api/authApi.ts`
- `apps/web/src/features/auth/authErrors.ts`
- `apps/web/src/features/auth/AuthContext.tsx`
- `apps/web/src/features/auth/hooks/useCurrentUser.ts`
- `apps/web/src/features/game-projects/api/gameProjectsApi.ts`
- `apps/web/src/features/game-projects/hooks/useGameProjects.ts`
- `apps/web/src/features/game-projects/hooks/useGameProjectSummary.ts`
- `apps/web/src/features/game-projects/types.ts`
- `apps/web/src/features/worlds/api/worldsApi.ts`
- `apps/web/src/features/worlds/hooks/useWorlds.ts`
- `apps/web/src/features/worlds/types.ts`
- `apps/web/src/features/system-templates/api/systemTemplatesApi.ts`
- `apps/web/src/features/system-templates/hooks/useSystemTemplates.ts`
- `apps/web/src/features/system-templates/types.ts`
- `apps/web/README.md`
- `Docs/ControleDeProjeto/PLANO_PRODUTO_E_REFERENCIAS.md`

## Validacoes Executadas

- `npm.cmd run build`
- `npm.cmd run dev -- --host 127.0.0.1 --port 5182`
- `GET /login` no dev server local
- Varredura de tom documental nos arquivos de controle.
- `git diff --check`

## Resultado Das Validacoes

- Build do frontend concluido com sucesso.
- Dev server do frontend iniciado com sucesso em `http://127.0.0.1:5182`.
- Rota `/login` respondeu `200 OK`.
- Documentacao de controle revisada sem termos proibidos de tom informal.
- Checagem de diff concluida sem erros de whitespace.

## Pendencias Conhecidas

- Hooks de dominio ainda nao estao conectados a telas finais do produto.
- Home do Mestre permanece mockada.
- Sem CRUD visual completo.
- Sem refresh token.
- Sem recuperacao de senha.
- Sem OAuth externo.
- Sem permissoes avancadas.
- Sem script `lint` configurado em `apps/web/package.json`.

## Proxima Etapa Recomendada

Fase recomendada: `front/game-project-list-create`

Objetivo: permitir que usuarios autenticados listem Campanhas & Cronicas reais e criem a primeira campanha pelo frontend, sem depender de Swagger ou chamadas manuais.

Justificativa tecnica: a Home do Mestre ainda depende de campanhas reais para deixar de ser mockada. A listagem/criacao de campanhas fecha o primeiro fluxo funcional do produto: cadastro, login, listagem e criacao de campanha.

Alternativa tecnica posterior: `front/home-master-real-data`, para conectar a Home aos dados reais depois que a criacao de campanha estiver disponivel no frontend.

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado.
