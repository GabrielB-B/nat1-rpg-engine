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
| 3 | `back/game-project-crud` | concluida | Criar CRUD de Projetos de Jogo. | Produto usa Campanhas & Crônicas; backend usa `GameProject`. | CRUD protegido por usuario autenticado. |
| 4 | `back/workspace-foundation` | concluida | Criar Worlds, SystemTemplates, modulos de projeto e summary de GameProject. | Summary retorna contadores basicos ate os modulos internos existirem. | Endpoints protegidos e isolamento por usuario validado. |
| 5 | `front/setup-foundation` | concluida | Iniciar React, TypeScript, Vite, Tailwind, Router e Query. | App web preparado em `apps/web`. | Build inicial do frontend aprovado. |
| 6 | `front/design-system-foundation` | concluida | Aplicar tokens visuais do tema Cartografo e Home mockada. | Dashboard segue mockado e sem consumo real da API. | Home responsiva no tema `cartographer` e build aprovado. |
| 7 | `front/auth-pages` | concluida | Criar telas de login/cadastro e protecao basica de rotas. | Login usa form-urlencoded; cadastro usa JSON; token JWT fica em `localStorage`. | `/login`, `/register`, `/`, cadastro, login e `/auth/me` validados localmente. |
| 8 | `front/api-integration-foundation` | concluida | Criar camada base de integracao com API no frontend. | API client centralizado, erros padronizados, Bearer token e hooks de leitura com TanStack Query. | Build aprovado, dev server validado e backend sem alteracoes. |
| 9 | `docs/product-roadmap-references` | concluida | Registrar direcao de produto, referencias e roadmap direcional. | Documentacao criada em `Docs/ControleDeProjeto/PLANO_PRODUTO_E_REFERENCIAS.md`. | Objetivos, referencias e proxima fase documentados. |
| 10 | `front/game-project-list-create` | concluida | Criar listagem e cadastro inicial de Campanhas & Crônicas no frontend. | Usa hooks e API client existentes; nao altera backend. | Usuario autenticado lista e cria campanhas reais; build validado. |
| 10.1 | `front/game-project-list-create-polish` | concluida | Refinar biblioteca de campanhas, reduzir vazio visual, adicionar empty state hibrido e arquivamento. | Usa endpoint real de arquivamento, filtro local de arquivadas, empty state condicional e lista focalizada sem painel lateral; nao altera backend. | Layout adaptativo, CTAs sem duplicidade, cards sem esticamento excessivo, fluxo para arquivadas, confirmacao de arquivamento e build validado. |
| 10.2 | `docs/architecture-roadmap-checkpoints` | concluida | Consolidar arquitetura, módulos, checkpoints, padrões de engenharia e decisões técnicas. | Fase documental sem alteração funcional de backend, frontend, banco, dependências ou design visual. | Plano de arquitetura, mapa de módulos, checkpoints, decisões e padrões registrados; validações documentais concluídas. |
| 10.3 / G0 | `security/baseline-hardening` | em andamento | Fechar a baseline com PostgreSQL real, migrations, CI e revisão. | Publicação e integração autorizadas; commit, PR e CI remoto estão em execução. | PostgreSQL descartável `up/test/down/up`, backend, lint, frontend, build e CI comprovados; PR verde e integrado. |
| 11 / G1 | `docs/professional-foundation` | em andamento | Consolidar produto, métricas, não objetivos, C4/deployment, ameaças, autorização, LGPD e qualidade. | Documentos canônicos foram preparados junto ao G0 por solicitação explícita; integração ainda pendente. | Hierarquia documental única, links revisados e nenhuma próxima fase concorrente. |
| 12 / G1 | `front/cartographer-brand-tokens` | pendente | Consolidar marca Cartógrafo, tipografia, tokens semânticos, contraste e QA visual. | Preservar geometria do logo entre temas; produzir SVG mestre e micro marca. | Ativos aprovados, tokens AA, foco/reduced motion e QA nos breakpoints. |
| 13 / G2 | `front/home-master-real-data` | pendente | Substituir a Home fictícia por dados reais e estados honestos. | Remover NPCs/mapas/notas/sessões mockadas e CTAs inertes. | Home real com loading, erro, vazio, sucesso e rotas funcionais. |
| 14 / G2 | `front/game-project-dashboard-shell` | pendente | Criar shell contextual da campanha. | Navegação inicial restrita a Resumo e Sessões; aplica tema da campanha. | `/campaigns/:projectId` protegido, profundo, responsivo e acessível. |
| 15 / G3 | `back/session-continuity-vertical` | pendente | Implementar Session, Scene, SessionOccurrence, SessionRecap e PendingItem. | Exige modelagem, migration PostgreSQL, autorização por campanha, services e repositories. | API e regras de domínio completas, testes IDOR e migration reversível. |
| 16 / G3 | `front/session-continuity-vertical` | pendente | Entregar o workspace sessão → cena → acontecimento → recap → pendência. | Consumir contratos reais; cenas pertencem ao workspace da sessão. | Fluxo persistido de ponta a ponta, estados assíncronos, testes e E2E crítico. |
| 17 / G4 | `research/gm-vertical-pilot` | pendente | Validar o vertical com mestres reais. | Entrevistas de problema podem começar antes; expansão funcional aguarda a decisão. | Evidências, métricas, achados e decisão `avançar`, `revisar` ou `parar`. |
| 17.1 / G4A | `back/calendar-scheduling-foundation` | bloqueada | Implementar Agenda completa somente se H5 for validada. | Gate opcional posterior ao vertical e ao piloto; depende de Sessions reais e evidência sobre conflitos/indisponibilidades. | H5 validada, escopo próprio aprovado e agenda real separada de timeline fictícia. |
| 18 / pré-beta | `security/public-auth-session-hardening` | pendente | Preparar autenticação e operação para exposição pública. | Rate limiting, estratégia de cookie/refresh, revogação, CORS HTTPS/não-loopback no domínio real, observabilidade e incidente. | Threat model revisado e checklist público aprovado. |
| 19 / G5 | `back/relational-modules-foundation` | bloqueada | Expandir personagens, locais, facções e relações. | Bloqueada até G4. | Só entra na fila após evidência do piloto. |
| 20 / G6 | `back/content-ai-foundation` | bloqueada | Evoluir documentos, exportação/importação, PDF e IA aprovada pelo mestre. | Bloqueada até valor sem IA, segurança e governança de dados. | Só entra após gates e decisão própria de risco/custo. |

## Regras De Execucao

- Confirmar branch ativa antes de iniciar uma nova tarefa.
- Respeitar escopo aprovado para a fase.
- Evitar alteracoes em backend durante fases de frontend, exceto quando explicitamente previsto.
- Evitar alteracoes em banco durante fases sem migration prevista.
- Atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md` ao finalizar uma fase.
- Atualizar `Docs/ControleDeProjeto/HISTORICO_TECNICO.md` com data, fase, entregas, decisoes tecnicas e validacoes.
- Registrar comandos de validacao executados.
- Atualizar `Docs/ControleDeProjeto/CHECKPOINTS.md` ao concluir ou redirecionar uma fase.
- Registrar decisões técnicas relevantes em `Docs/ControleDeProjeto/DECISOES_TECNICAS.md`.

## Observacoes Tecnicas

- `front/design-system-foundation` permanece concluida com Home mockada no tema `cartographer`.
- A Home do Mestre atual e visual e utiliza dados mockados isolados em `apps/web/src/data/mockWorkspace.ts`.
- `front/auth-pages` permanece concluida com integracao real aos endpoints locais de autenticacao.
- `front/api-integration-foundation` permanece concluida com servicos e hooks preparados para leitura protegida.
- `front/game-project-list-create` permanece concluida com listagem e criacao real de campanhas.
- `front/game-project-list-create-polish` permanece concluida com biblioteca adaptativa, empty state condicional, CTAs sem duplicidade, lista focalizada sem painel lateral e arquivamento via API real.
- `docs/architecture-roadmap-checkpoints` consolida arquitetura, módulos, checkpoints, padrões e decisões sem alterar código funcional.
- `security/baseline-hardening` possui baseline preparada e checks locais executáveis aprovados; publicação e integração foram autorizadas.
- A próxima ação não é iniciar uma feature: é publicar, comprovar o CI e integrar G0.
- Depois da integração, concluir G1 visual e então executar Home e shell em branches próprias.
- A única expansão funcional aprovada antes do piloto é o vertical de continuidade.
- Personagens, locais, facções, relações, documentos, PDF e IA permanecem bloqueados.

## Padrão Obrigatório Para Próximas Fases

Toda fase técnica deve:

1. Ler documentação de controle antes de alterar arquivos.
2. Identificar fase atual e branch.
3. Respeitar escopo da fase.
4. Não apagar histórico.
5. Atualizar checkpoints.
6. Atualizar status atual.
7. Atualizar próximas tarefas.
8. Documentar pendências.
9. Manter código legível e manutenível.
10. Executar validações.
11. Informar arquivos alterados.
12. Não fazer commit automático.
