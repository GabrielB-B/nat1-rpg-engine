# Proximas Tarefas Tecnicas

## Status Possiveis

- `pendente`
- `em andamento`
- `concluida`
- `bloqueada`

## Fila Do MVP 1

| Ordem | Branch | Status | Objetivo | Observacoes tecnicas | Criterios de aceite |
| --- | --- | --- | --- | --- | --- |
| 1 | `back/database-foundation` | concluida | Criar models centrais e migration inicial. | Base relacional preparada para entidades principais. | Migration aplicada e backend validado. |
| 2 | `back/auth-foundation` | concluida | Criar autenticacao basica com usuario, hash de senha e JWT. | Swagger Authorize usa OAuth2PasswordRequestForm. | Cadastro, login e `/auth/me` validados. |
| 3 | `back/game-project-crud` | concluida | Criar CRUD de Projetos de Jogo. | Produto usa Campanhas & Cronicas; backend usa `GameProject`. | CRUD protegido por usuario autenticado. |
| 4 | `back/workspace-foundation` | concluida | Criar Worlds, SystemTemplates, modulos de projeto e summary de GameProject. | Summary retorna contadores basicos ate os modulos internos existirem. | Endpoints protegidos e isolamento por usuario validado. |
| 5 | `front/setup-foundation` | concluida | Iniciar React, TypeScript, Vite, Tailwind, Router e Query. | App web preparado em `apps/web`. | Build inicial do frontend aprovado. |
| 6 | `front/design-system-foundation` | concluida | Aplicar tokens visuais do tema Cartografo e Home mockada. | Dashboard segue mockado e sem consumo real da API. | Home responsiva no tema `cartographer` e build aprovado. |
| 7 | `front/auth-pages` | concluida | Criar telas de login/cadastro e protecao basica de rotas. | Login usa form-urlencoded; cadastro usa JSON; token JWT fica em `localStorage`. | `/login`, `/register`, `/`, cadastro, login e `/auth/me` validados localmente. |
| 8 | `front/api-integration-foundation` | concluida | Criar camada base de integracao com API no frontend. | API client centralizado, erros padronizados, Bearer token e hooks de leitura com TanStack Query. | Build aprovado, dev server validado e backend sem alteracoes. |
| 9 | `front/home-master-shell` | pendente | Evoluir a Home do Mestre para fluxos reais de produto. | Preservar composicao visual aprovada e preparar integracao gradual com API. | Rota autenticada com estados de loading, vazio, erro e dados mock/API definidos por escopo. |
| 10 | `back/session-scene-foundation` | pendente | Criar fundacao backend de Sessoes e Cenas. | Definir entidades, endpoints protegidos e relacao com `GameProject`. | Migration, testes e documentacao atualizados. |

## Regras De Execucao

- Confirmar branch ativa antes de iniciar uma nova tarefa.
- Respeitar escopo aprovado para a fase.
- Evitar alteracoes em backend durante fases de frontend, exceto quando explicitamente previsto.
- Evitar alteracoes em banco durante fases sem migration prevista.
- Atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md` ao finalizar uma fase.
- Atualizar `Docs/ControleDeProjeto/HISTORICO_TECNICO.md` com data, fase, entregas, decisoes tecnicas e validacoes.
- Registrar comandos de validacao executados.

## Observacoes Tecnicas

- `front/design-system-foundation` permanece concluida com Home mockada no tema `cartographer`.
- A Home do Mestre atual e visual e utiliza dados mockados isolados em `apps/web/src/data/mockWorkspace.ts`.
- `front/auth-pages` permanece concluida com integracao real aos endpoints locais de autenticacao.
- `front/api-integration-foundation` permanece concluida com servicos e hooks preparados para leitura protegida.
- A proxima expansao da Home deve evitar CRUD visual completo enquanto a fase de modulos internos nao estiver definida.
