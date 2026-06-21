# Status Atual

Projeto: Nat 1 RPG Engine

Fase atual: front/game-project-list-create-polish

Branch: front/game-project-list-create

Status: concluida em validacao local

Data da ultima atualizacao: 2026-06-21

## Ultimas Entregas

- Criada rota protegida `/campaigns`.
- Criada tela de Campanhas & Crônicas com linguagem visual `cartographer`.
- Adicionada listagem real de campanhas via `GET /game-projects`.
- Adicionada criacao de campanha via `POST /game-projects`.
- Criada mutation `useCreateGameProject` com invalidacao da lista apos sucesso.
- Criados componentes `GameProjectCard`, `CreateGameProjectForm` e `GameProjectsEmptyState`.
- Adicionados estados de loading, erro, vazio e sucesso.
- Adicionada entrada navegavel "Campanhas" na sidebar.
- Mantidos Worlds e SystemTemplates como selects opcionais usando hooks existentes.
- Validada URL de capa no frontend com aceite apenas de `http` e `https`.
- Mantido genero/tom narrativo como campo visual planejado, sem envio para a API.
- Backend, banco e migrations permaneceram sem alteracoes.
- Refinado layout adaptativo da biblioteca para 0, 1-2 e 3+ campanhas.
- Substituido feedback de sucesso por toast compacto.
- Removido painel lateral de ações da biblioteca para evitar coluna auxiliar sem função principal.
- Ajustado menu secundario do card para impedir corte da opcao `Arquivar`.
- Adicionado filtro simples entre campanhas ativas e arquivadas.
- Adicionada acao de arquivar campanha com confirmacao.
- Corrigido vazio vertical no topo da biblioteca causado por grid com `min-height` sem `align-content: start`.
- Estado vazio da biblioteca foi refinado como empty state hibrido imersivo para a primeira campanha.
- Removido placeholder retangular solto do estado vazio ativo, substituido por composicao cartografica integrada em CSS.
- Aba Arquivadas recebeu estado vazio compacto, sem hero ou tutorial fixo.
- Estado vazio ativo passou a diferenciar biblioteca sem histórico e biblioteca com campanhas arquivadas.
- Biblioteca sem histórico usa CTA `Criar primeira campanha`.
- Biblioteca com campanhas arquivadas e nenhuma ativa usa CTA `Criar nova campanha` e ação secundária `Ver arquivadas`.
- Ação `Ver arquivadas` alterna diretamente para a aba Arquivadas.
- CTA superior `Nova campanha` fica oculto quando o empty state ativo concentra a ação principal.
- Layout com 1-2 campanhas passou a usar lista focalizada com largura máxima controlada.
- Tela `/campaigns` recebeu regra de respiro vertical entre topbar, hero, filtros e lista.
- Menu secundario dos cards passou a fechar com clique externo, mudança de foco e tecla Escape.
- Textos nao interativos dos cards receberam cursor e caret de leitura para evitar indicacao visual de edição.
- Hero do estado vazio recebeu ajustes de altura, colunas, espaçamento e composição visual para telas desktop e médias.
- Texto de confirmacao de arquivamento alinhado a regra da fase.
- Mantida exclusao permanente fora do escopo.

## Estado Tecnico Do Produto

Backend concluido ate esta etapa:

- Fundacao FastAPI com PostgreSQL local via Docker.
- SQLAlchemy, Alembic e settings com `pydantic-settings`.
- Autenticacao com JWT.
- Swagger Authorize com OAuth2PasswordRequestForm usando `username` como e-mail.
- CRUD de GameProject / Campanhas & Crônicas.
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
- Tela `/campaigns` integrada a dados reais de GameProjects, Worlds e SystemTemplates.
- Formulario de criacao de campanha integrado a API real.
- Arquivamento de campanha integrado ao endpoint real `POST /game-projects/{project_id}/archive`.
- Listagem de arquivadas usa `include_archived=true` e filtro local.
- Layout de `/campaigns` ancorado no topo util da tela, sem distribuicao artificial de espaco vertical.
- Ritmo vertical de `/campaigns` usa espaçamento controlado entre cabecalho, filtros e conteudo para evitar compressao visual.
- Menu de ações dos cards usa estado controlado no React em vez de comportamento nativo de `details`.
- Empty state ativo abre o fluxo de criacao no modal existente, preservando payload aceito pelo backend.
- Empty state ativo cobre os cenarios sem campanhas, somente arquivadas e campanhas ativas sem alterar a rota.
- Acoes primarias de criacao evitam duplicidade entre hero e topbar.

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
- `apps/web/src/features/game-projects/hooks/useCreateGameProject.ts`
- `apps/web/src/features/game-projects/hooks/useArchiveGameProject.ts`
- `apps/web/src/features/game-projects/hooks/useGameProjectSummary.ts`
- `apps/web/src/features/game-projects/components/ArchiveGameProjectDialog.tsx`
- `apps/web/src/features/game-projects/components/GameProjectCard.tsx`
- `apps/web/src/features/game-projects/components/CreateGameProjectForm.tsx`
- `apps/web/src/features/game-projects/components/GameProjectsEmptyState.tsx`
- `apps/web/src/features/game-projects/presentation.ts`
- `apps/web/src/features/game-projects/types.ts`
- `apps/web/src/features/worlds/api/worldsApi.ts`
- `apps/web/src/features/worlds/hooks/useWorlds.ts`
- `apps/web/src/features/worlds/types.ts`
- `apps/web/src/features/system-templates/api/systemTemplatesApi.ts`
- `apps/web/src/features/system-templates/hooks/useSystemTemplates.ts`
- `apps/web/src/features/system-templates/types.ts`
- `apps/web/src/pages/GameProjectsPage.tsx`
- `apps/web/src/app/router.tsx`
- `apps/web/src/components/layout/ModuleNavItem.tsx`
- `apps/web/src/components/layout/Sidebar.tsx`
- `apps/web/src/data/mockWorkspace.ts`
- `apps/web/src/styles/globals.css`
- `apps/web/README.md`
- `Docs/ControleDeProjeto/PLANO_PRODUTO_E_REFERENCIAS.md`

## Validacoes Executadas

- `npm.cmd run build`
- `npm.cmd run dev -- --host 127.0.0.1 --port 5173`
- `GET /login` no dev server local
- `GET /campaigns` no dev server local
- `GET /api/v1/health`
- Cadastro temporario via `POST /auth/register`
- Login temporario via `POST /auth/login`
- Criacao de campanha via `POST /game-projects`
- Arquivamento via `POST /game-projects/{project_id}/archive`
- Listagem ativa via `GET /game-projects`
- Listagem com arquivadas via `GET /game-projects?include_archived=true`
- Validacao funcional temporaria de `/campaigns` com Playwright e Microsoft Edge do sistema
- Varredura textual para confirmar nomenclatura acentuada de Campanhas & Crônicas
- `git diff --check`

## Resultado Das Validacoes

- Build do frontend concluido com sucesso.
- TypeScript compilado com sucesso.
- Bundle de producao gerado pelo Vite.
- Dev server do frontend respondeu `200 OK` em `/login`.
- Dev server do frontend respondeu `200 OK` em `/campaigns`.
- API respondeu `200 OK` em `/api/v1/health`.
- Criacao de campanha validada contra API local.
- Arquivamento de campanha validado contra API local.
- Campanha arquivada saiu da listagem ativa e apareceu na listagem com arquivadas.
- Ajuste visual da biblioteca validado por build local apos a correcao do grid e do estado vazio.
- Empty state hibrido validado por build local sem alteracao de API.
- Criacao e arquivamento foram revalidados via API apos o refinamento visual.
- Estado vazio sem historico validado com CTA `Criar primeira campanha` e sem CTA superior duplicado.
- Estado vazio com arquivadas validado com CTA `Criar nova campanha`, acao `Ver arquivadas` e alternancia de aba.
- Estado com campanhas ativas validado sem empty state e com CTA superior `Nova campanha`.
- Layout com 1-2 campanhas validado sem painel lateral e com largura focalizada de 1360px em viewport desktop.
- Ritmo vertical de `/campaigns` validado em viewport desktop com respiro entre hero, filtros e primeiro card.
- Menu de arquivamento validado com abertura, clique externo, tecla Escape e preservação da ação `Arquivar`.
- Textos dos cards validados com `caret-color` transparente e cursor padrão em conteúdo não interativo.
- Viewport intermediario validado para confirmar hierarquia e botoes visiveis.
- Nomenclatura `Campanhas & Crônicas` validada nos arquivos principais.
- Checagem de diff concluida sem erros de whitespace.

## Pendencias Conhecidas

- Home do Mestre permanece mockada.
- CTA "Abrir campanha" permanece visual porque a shell interna da campanha ainda nao existe.
- Genero/tom narrativo nao e enviado para a API por falta de campo explicito no backend.
- Jogadores ativos nao sao exibidos como dado real porque o backend ainda nao possui campo ou relacao de participantes.
- Proxima sessao nao e exibida como dado real porque sessoes ainda nao possuem entidade no backend.
- Sem edicao visual de campanha.
- Sem restauracao visual de campanha.
- Sem exclusao permanente.
- Sem refresh token.
- Sem recuperacao de senha.
- Sem OAuth externo.
- Sem permissoes avancadas.
- Sem script `lint` configurado em `apps/web/package.json`.

## Proxima Etapa Recomendada

Fase recomendada: `front/home-master-real-data`

Objetivo: conectar a Home do Mestre aos dados reais ja disponiveis, usando as campanhas criadas pelo frontend.

Justificativa tecnica: o fluxo cadastro, login, listagem e criacao de campanha ja existe. A Home do Mestre pode deixar de depender exclusivamente de mocks e passar a refletir o estado real da conta.

Alternativa tecnica posterior: `front/game-project-dashboard-shell`, para criar a entrada interna de cada campanha com summary e modulos ativos.

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado.
