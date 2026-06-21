# Checkpoints Do Projeto

Projeto: Nat 1 RPG Engine

Data de referencia: 2026-06-21

## Objetivo

Registrar checkpoints por fase para permitir retomada técnica do projeto sem perda de contexto.

## CP-001 - Backend Database Foundation

- Fase: `back/database-foundation`
- Branch: `back/database-foundation`
- Status: concluído
- Objetivo: criar base relacional inicial do MVP.
- Entregas concluídas: models centrais, Alembic preparado, PostgreSQL local via Docker e documentação de setup.
- Validações executadas: migração validada e testes de backend registrados no histórico técnico.
- Pendências: módulos internos completos ainda não modelados.
- Próxima fase recomendada: `back/auth-foundation`.
- Riscos identificados: crescimento de entidades sem fronteiras claras de domínio.

## CP-002 - Backend Auth Foundation

- Fase: `back/auth-foundation`
- Branch: `back/auth-foundation`
- Status: concluído
- Objetivo: implementar autenticação inicial.
- Entregas concluídas: cadastro, login, usuário atual, hash de senha com bcrypt e JWT Bearer token.
- Validações executadas: testes de autenticação e validação manual via Swagger.
- Pendências: refresh token, recuperação de senha, OAuth externo e permissões avançadas.
- Próxima fase recomendada: `back/game-project-crud`.
- Riscos identificados: estratégia de token ainda simples para uso em produção.

## CP-003 - Backend Game Project CRUD

- Fase: `back/game-project-crud`
- Branch: `back/game-project-crud`
- Status: concluído
- Objetivo: implementar CRUD protegido de Campanhas & Crônicas.
- Entregas concluídas: criar, listar, detalhar, atualizar, arquivar e restaurar `GameProject`.
- Validações executadas: testes de isolamento por usuário e fluxos protegidos.
- Pendências: edição visual, restauração visual e exclusão permanente fora do escopo.
- Próxima fase recomendada: `back/workspace-foundation`.
- Riscos identificados: novos campos de campanha devem preservar compatibilidade com o frontend.

## CP-004 - Backend Workspace Foundation

- Fase: `back/workspace-foundation`
- Branch: `back/workspace-foundation`
- Status: concluído
- Objetivo: criar base de workspace para mundos, sistemas e módulos de campanha.
- Entregas concluídas: `World`, `SystemTemplate`, `ProjectModuleSetting` e summary de GameProject.
- Validações executadas: testes de endpoints protegidos, isolamento por usuário e regras de templates built-in.
- Pendências: CRUD dos módulos internos ainda não existe.
- Próxima fase recomendada: `front/setup-foundation`.
- Riscos identificados: summary retorna contadores básicos até os módulos internos serem implementados.

## CP-005 - Frontend Setup Foundation

- Fase: `front/setup-foundation`
- Branch: `front/setup-foundation`
- Status: concluído
- Objetivo: iniciar aplicação web oficial.
- Entregas concluídas: React, TypeScript, Vite, Tailwind CSS, React Router e TanStack Query.
- Validações executadas: build inicial do frontend.
- Pendências: design system e telas reais ainda não existiam nesta etapa.
- Próxima fase recomendada: `front/design-system-foundation`.
- Riscos identificados: manter estrutura de features por domínio para evitar crescimento desorganizado.

## CP-006 - Frontend Design System Foundation

- Fase: `front/design-system-foundation`
- Branch: `front/design-system-foundation`
- Status: concluído
- Objetivo: aplicar fundação visual do tema Cartógrafo.
- Entregas concluídas: tokens visuais, componentes base, sidebar, topbar, cards, Home do Mestre mockada e refinamento de escala de ícones.
- Validações executadas: `npm.cmd run build` e validações visuais registradas no histórico.
- Pendências: Home ainda mockada e temas alternativos ainda não aplicados em telas completas.
- Próxima fase recomendada: `front/auth-pages`.
- Riscos identificados: manter consistência visual conforme telas reais substituírem mocks.

## CP-007 - Frontend Auth Pages

- Fase: `front/auth-pages`
- Branch: `front/auth-pages`
- Status: concluído
- Objetivo: criar autenticação frontend integrada à API.
- Entregas concluídas: telas de login/cadastro, `AuthLayout`, storage de token, contexto de autenticação e rotas protegidas.
- Validações executadas: `npm.cmd run build`, renderização de `/login` e `/register`, cadastro/login local e `/auth/me`.
- Pendências: recuperação de senha, OAuth externo, refresh token e permissões avançadas.
- Próxima fase recomendada: `front/api-integration-foundation`.
- Riscos identificados: token em `localStorage` deve ser reavaliado antes de produção.

## CP-008 - Frontend API Integration Foundation

- Fase: `front/api-integration-foundation`
- Branch: `front/api-integration-foundation`
- Status: concluído
- Objetivo: padronizar integração com API real.
- Entregas concluídas: API client centralizado, erros padronizados, helpers HTTP, query client e hooks de leitura por domínio.
- Validações executadas: `npm.cmd run build`, dev server local e validações de endpoints protegidos.
- Pendências: integração da Home com dados reais.
- Próxima fase recomendada: `docs/product-roadmap-references`.
- Riscos identificados: manter camada de API coesa conforme novos domínios forem adicionados.

## CP-009 - Product Roadmap References

- Fase: `docs/product-roadmap-references`
- Branch: `docs/product-roadmap-references`
- Status: concluído
- Objetivo: consolidar direção de produto, referências e roadmap direcional.
- Entregas concluídas: plano de produto com referências a Kanka, World Anvil, LegendKeeper, Campfire, Notion, Obsidian e Roll20.
- Validações executadas: pesquisa de referências oficiais, revisão dos documentos de controle, varredura de tom documental, `git diff --check` e `npm.cmd run build`.
- Pendências: manter o roadmap atualizado a cada fase relevante.
- Próxima fase recomendada: `front/game-project-list-create`.
- Riscos identificados: copiar referências de mercado em vez de adaptar princípios ao Nat 1.

## CP-010 - Game Project List Create

- Fase: `front/game-project-list-create`
- Branch: `front/game-project-list-create`
- Status: concluído
- Objetivo: criar primeiro fluxo real de Campanhas & Crônicas no frontend.
- Entregas concluídas: rota `/campaigns`, listagem real via `GET /game-projects`, criação via `POST /game-projects`, formulário e componentes de biblioteca.
- Validações executadas: `npm.cmd run build`, dev server local, respostas HTTP de `/login`, `/campaigns` e `/api/v1/health`.
- Pendências: arquivamento visual, edição, restauração e abertura interna de campanha.
- Próxima fase recomendada: `front/game-project-list-create-polish`.
- Riscos identificados: dados de jogadores e próxima sessão ainda não existem no backend.

## CP-011 - Game Project List Create Polish

- Fase: `front/game-project-list-create-polish`
- Branch: `front/game-project-list-create`
- Data: 2026-06-21
- Status: concluído
- Objetivo: refinar biblioteca de campanhas, reduzir vazio visual e corrigir interações.
- Entregas concluídas: empty state condicional, lista focalizada, remoção de painel lateral auxiliar, abas ativas/arquivadas, arquivamento via API e menu secundário controlado.
- Validações executadas: `npm.cmd run build`, validações de API locais, Playwright temporário, varredura textual e `git diff --check`.
- Pendências: Home real, shell interna da campanha, edição visual e restauração visual.
- Próxima fase recomendada: `docs/architecture-roadmap-checkpoints`.
- Riscos identificados: página `/campaigns` deve continuar sem assumir módulos internos ainda não implementados.

## CP-012 - Architecture Roadmap Checkpoints

- Fase: `docs/architecture-roadmap-checkpoints`
- Branch: `docs/architecture-roadmap-checkpoints`
- Data: 2026-06-21
- Status: concluído
- Objetivo: consolidar arquitetura, módulos, decisões técnicas, checkpoints e padrões de engenharia.
- Entregas concluídas: criação de plano de arquitetura, mapa de módulos, checkpoints, padrões de engenharia e decisões técnicas.
- Validações executadas: `npm.cmd run build`, `pytest`, varredura de tom documental proibido, varredura de espaços finais, revisão de arquivos alterados, `git diff --check` e `git status --short --branch`.
- Pendências: manter checkpoints atualizados nas próximas fases.
- Próxima fase recomendada: `front/home-master-real-data`.
- Riscos identificados: documentação pode se desatualizar se fases futuras não atualizarem os checkpoints.

## Padrão De Atualização

- Cada fase concluída deve atualizar este arquivo.
- Cada checkpoint deve registrar status, validações, pendências e próxima fase.
- Fases documentais devem declarar quando testes de código não forem aplicáveis.
- Histórico técnico detalhado permanece em `HISTORICO_TECNICO.md`.
