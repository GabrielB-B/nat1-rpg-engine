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
- Mantida a equivalencia de produto: interface usa Campanhas & Crônicas; backend usa Projeto de Jogo / `GameProject`.
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

### 2026-06-05 - Fundacao Visual Do Frontend

- Criada shell visual mockada do Workspace do Mestre em `apps/web`.
- Criados componentes reutilizaveis de UI, layout e dashboard: `Button`, `Card`, `Badge`, `Sidebar`, `Topbar`, `ModuleNavItem`, `StatCard`, `DashboardSection`, `CampaignCard`, `SessionList` e `RecentNotes`.
- Dados mockados do dashboard foram isolados em `apps/web/src/data/mockWorkspace.ts` para futura substituicao por API.
- Tema `cartographer` foi refinado como tema visual padrao.
- Temas `dark_horror` e `humanist_futuristic` permanecem previstos por tokens.
- Nenhuma funcionalidade real de frontend, CRUD, autenticacao visual ou consumo de API foi implementada nesta etapa.

### 2026-06-05 - Refinamento Visual Do Tema Cartografo

- Home do Mestre foi compactada para se aproximar da referencia aprovada do Tema Cartografo / Modelo C.
- Sidebar foi reduzida e passou a usar menu compacto com icones leves via `lucide-react`.
- Topbar foi reduzida com busca compacta, botoes de icone e acao principal "Nova sessao".
- Card de campanha ativa passou a usar composicao horizontal com mapa mockado por CSS, tags e botao "Abrir campanha".
- Parte inferior passou a exibir cards especificos de ultimos NPCs, mapa recente e notas recentes.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Refinamento Profundo Da Home Cartografo

- Interface mockada da Home do Mestre foi reescalada para parecer mais com produto SaaS real para mestres de RPG.
- Sidebar foi ajustada para largura proxima da referencia aprovada, com itens mais legiveis, estado ativo refinado e usuario no rodape.
- Topbar foi mantida compacta em 56px, com busca, botoes de icone e acao principal "Nova sessao".
- Dashboard passou a usar melhor a largura disponivel com `max-width` maior, grid de estatisticas em linha, campanha ativa central e coluna lateral de proximas sessoes.
- Mapa CSS foi refinado com camadas cartograficas: contornos, rotas, montanhas, marcadores e rosa dos ventos.
- Cards inferiores de NPCs, mapa recente e notas recentes foram compactados para aparecerem melhor no primeiro viewport desktop.
- Breakpoint mobile foi ajustado para empilhar conteudo sem sobreposicao.
- Validacoes executadas: `npm run typecheck`, `npm run build`, dev server local e screenshots desktop/mobile.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Refinamento Cirurgico Da Home Cartographer

- Comparada a Home do Mestre com a referencia visual aprovada do tema `cartographer`.
- Bloco de saudacao deixou de ser card isolado e passou a ficar solto sobre o fundo, com ornamento cartografico discreto.
- Fundo visual foi corrigido: removidas linhas diagonais pesadas e adicionadas linhas de mapa laterais, granulo leve e textura de pergaminho.
- Grid principal foi compactado, reduzindo espacamentos entre estatisticas, campanha ativa, coluna lateral e cards inferiores.
- Topbar foi refinada com icones mais discretos e botao "Nova sessao" em dourado, mais proximo do mock aprovado.
- Mapa CSS recebeu camada SVG inline com rio, rotas, montanhas e textura para parecer menos esquematico.
- Validacoes executadas: `npm run typecheck`, `npm run build`, `npm run dev` em `http://127.0.0.1:5177` e screenshot desktop `1365x768`.
- `npm run lint` nao foi executado porque nao existe script `lint` no frontend.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Correcao De Largura Da Home Cartographer

- Identificado desvio visual em viewport largo: tela pequena e centralizada.
- Causa identificada: `workspace-dashboard` ainda usava `max-width` e `margin: auto`, criando uma ilha centralizada.
- Corrigido para layout fluido: dashboard usa `width: 100%`, `max-width: none` e `margin: 0`.
- Grid principal foi recalibrado para ocupar a largura util da area ao lado da sidebar, mantendo coluna direita encaixada.
- Validacoes executadas: `npm run typecheck`, `npm run build` e screenshot desktop largo `1904x960`.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Ajuste Responsivo De Respiro Da Home Cartographer

- Identificado excesso de expansao horizontal em telas largas, com perda do respiro cartografico a direita.
- Layout foi corrigido para uma regra responsiva mais precisa: ocupa 100% em telas comuns, mas em telas largas usa `max-width: 1480px` ancorado a esquerda.
- `workspace-main` passou a usar padding direito responsivo para preservar margem visual sem recentralizar a tela.
- Resultado esperado: composicao mais parecida com a referencia, com conteudo encostado a esquerda da area principal e faixa de fundo visivel a direita em monitores largos.
- Validacoes executadas: `npm run typecheck`, `npm run build`, screenshot `1365x768` e screenshot largo `1904x960`.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Refinamento Final De Escala Da Home Cartographer

- Identificados tres pontos de ajuste visual: sobra inferior excessiva, largura esticada em desktop largo e tipografia pesada em areas pequenas de UI.
- Tipografia foi recalibrada: serif editorial preservada em titulos, enquanto menu, labels, metadados, badges e listas passaram a usar peso mais limpo e utilitario.
- `workspace-dashboard` passou a usar largura maxima ampla e ancorada, com grid mais controlado para reduzir o mapa principal em monitores largos sem voltar ao aspecto de ilha centralizada.
- Cards de estatistica foram compactados em altura, numero e icone para se aproximarem da densidade do mock aprovado.
- Em telas largas e altas, a altura extra passou a ser distribuida principalmente no mapa ativo, enquanto cards inferiores mantem acoes ancoradas e altura mais controlada.
- Breakpoint intermediario foi reorganizado: campanha e proximas sessoes ficam lado a lado, NPCs e notas abaixo, e mapa recente ocupa faixa completa para evitar painel lateral vazio.
- Menu mockado da Home global do Mestre foi documentado no codigo e no README; a navegacao interna futura de campanha devera vir de `ProjectModuleSettings`.
- Validacoes executadas: `npm run typecheck`, `npm run build`, dev server em `http://127.0.0.1:5177`, screenshots `1904x960`, `1365x768`, `1120x820` e `390x844`.
- `npm run lint` nao foi executado porque nao existe script `lint` em `apps/web/package.json`.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Correcao De Fidelidade Da Home Cartographer

- Identificado afastamento da referencia aprovada na composicao lateral criada na versao anterior.
- Campanha ativa foi restaurada para a estrutura correta: titulo da secao, mapa horizontal no topo, titulo da campanha com badge abaixo, metadados, tags e CTA no rodape direito.
- Mapa recente foi restaurado para a estrutura correta: titulo da secao, imagem no topo, titulo/meta/descricao abaixo e link inferior.
- Refinamentos preservados sem mudar a composicao: largura desktop controlada, altura do mapa limitada, padding compacto, metadados legiveis e textura cartografica CSS.
- O metadado da campanha passou a exibir `Proxima sessao: O Porto Cinzento` no card, aproximando a Home da referencia.
- Validacoes executadas: `npm run typecheck`, `npm run build`, dev server em `http://127.0.0.1:5177`, screenshots `1904x960`, `1365x768` e `1120x820`.
- `npm run lint` nao foi executado porque nao existe script `lint` em `apps/web/package.json`.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Correcao De Densidade Da Home Cartographer

- Identificado vazio inferior em desktop largo, apesar de comportamento adequado em telas menores.
- Card `Campanha ativa` recebeu a secao visivel `Resumo da campanha`, posicionada abaixo dos metadados e antes das tags/CTA.
- O resumo usa texto mockado curto para reforcar continuidade narrativa sem transformar o card em bloco pesado.
- Cards inferiores passaram a exibir detalhes ja existentes nos mocks de NPCs e notas, tornando a linha inferior mais util e menos vazia.
- `dashboard-grid` ganhou altura responsiva baseada no viewport em desktop, preservando a disposicao aprovada: campanha/mapa no topo, sessoes a direita e linha inferior com NPCs, mapa e notas.
- Fundo `cartographer` recebeu camada topografica adicional por CSS, com baixa opacidade e concentracao visual no lado direito/bordas.
- Iconografia definida foi preservada: classes `icon-xs`, `icon-sm`, `icon-md`, `icon-lg` e `strokeWidth` 1.75.
- Validacoes executadas: `npm.cmd run build`, dev server em `http://127.0.0.1:5180` e resposta HTTP `200 OK`.
- Nenhum backend, endpoint, model, migration, banco ou consumo real de API foi alterado.

### 2026-06-05 - Fundacao De Autenticacao Frontend

- Criadas telas `/login` e `/register` no tema `cartographer`, com card central, textos de produto, inputs e erros simples.
- Criado `AuthLayout` para as telas publicas de autenticacao.
- Criado modulo `apps/web/src/features/auth` com tipos, storage de token, API client de auth, contexto de autenticacao e rotas publica/protegida.
- Login frontend usa `POST /auth/login` com OAuth2 form data, enviando o e-mail no campo `username`.
- Cadastro frontend usa `POST /auth/register` com JSON e faz login automatico apos sucesso.
- Sessao inicial e validada com `GET /auth/me` quando existe token em `localStorage`.
- Token JWT e salvo em `localStorage` como `nat1.auth.access_token` e removido no logout.
- Rota `/` foi protegida: usuario anonimo redireciona para `/login`; usuario autenticado acessa a Home mockada.
- Usuarios autenticados sao redirecionados de `/login` e `/register` para `/`.
- Logout simples foi adicionado como acao discreta na topbar.
- `apiRequest` passou a suportar melhor JSON, form-urlencoded, Bearer token e erros estruturados com `ApiError`.
- Validacoes executadas: `npm.cmd run build`, dev server em `http://127.0.0.1:5181`, `GET /health`, cadastro, login form-urlencoded e `GET /auth/me` com Bearer token.
- Nenhum backend, endpoint, model, migration ou banco foi alterado.
- Dashboard segue mockado; nao foi implementado CRUD visual nem consumo real de dados da Home.

### 2026-06-05 - Fundacao De Integracao Com API Frontend

- Implementada camada base de integracao com API em `apps/web/src/lib/api`.
- Adicionado tratamento padronizado de erros HTTP com `ApiError` e `ApiNetworkError`.
- Adicionado parser de erros compatível com payloads `detail` do FastAPI.
- Adicionado helper `withQueryParams` para montagem de query string.
- Adicionada configuracao central do API client para token Bearer salvo e callback de `401`.
- Ajustada autenticacao frontend para chamadas publicas em login/cadastro e chamadas protegidas em `/auth/me`.
- Adicionado logout automatico em respostas `401` de chamadas protegidas.
- Configurado TanStack Query para evitar retry em `401`, `403` e `404`.
- Criado hook `useCurrentUser`.
- Criados tipos, servicos e hooks de leitura para GameProjects.
- Criados tipos, servicos e hooks de leitura para Worlds.
- Criados tipos, servicos e hooks de leitura para SystemTemplates.
- Mantida a Home do Mestre com dados mockados, sem ligacao direta aos hooks novos nesta fase.
- Validacoes executadas: `npm.cmd run build`, dev server em `http://127.0.0.1:5182` e resposta HTTP `200 OK` em `/login`.
- Nenhum backend, endpoint, model, migration ou banco foi alterado.

### 2026-06-05 - Planejamento De Produto E Referencias

- Criado documento `Docs/ControleDeProjeto/PLANO_PRODUTO_E_REFERENCIAS.md`.
- Registrado objetivo do Nat 1 como plataforma de gestao, criacao e organizacao de campanhas de RPG.
- Registrada direcao de produto: Home do Mestre, Campanhas & Crônicas, modulos relacionais, mundo amplo, sistemas/templates separados e IA com aprovacao do mestre.
- Registradas referencias de produto: Kanka, World Anvil, LegendKeeper, Campfire, Notion, Obsidian e Roll20.
- Definida Kanka como referencia principal de organizacao modular.
- Definidas World Anvil, LegendKeeper e Campfire como referencias secundarias de worldbuilding e estrutura editorial.
- Definidas Notion e Obsidian como referencias de flexibilidade organizacional.
- Definido Roll20 como referencia secundaria de journal e mesa, sem papel de UX principal.
- Atualizada proxima fase recomendada para `front/game-project-list-create`.
- Validacoes executadas: pesquisa de referencias oficiais, revisao dos documentos de controle, varredura de tom documental, `git diff --check` e `npm.cmd run build`.
- Nenhum backend, endpoint, model, migration, banco ou codigo de frontend foi alterado nesta etapa.

### 2026-06-21 - Listagem E Criacao De Campanhas No Frontend

- Criada rota protegida `/campaigns` para Campanhas & Crônicas.
- Criada pagina `GameProjectsPage` com listagem real de campanhas via `GET /game-projects`.
- Criados componentes de interface para card de campanha, estado vazio e formulario de criacao.
- Criada mutation `useCreateGameProject` usando TanStack Query e invalidacao da lista apos sucesso.
- Adicionado `POST /game-projects` na camada de API do frontend.
- Adicionada entrada navegavel "Campanhas" na sidebar, preservando a Home como rota principal.
- Implementado formulario rapido com nome, formato, sistema/template, mundo/cenario, status, descricao curta e URL de capa.
- Mantido tema visual `cartographer`, com cards em linguagem de biblioteca de cronicas e placeholder cartografico para campanhas sem capa.
- Genero/tom narrativo ficou visualmente preparado, mas nao e enviado para a API porque o backend ainda nao possui campo explicito.
- Mantidos fora do escopo: edicao, arquivamento visual, upload, PDF, IA e shell interna da campanha.
- Nenhum backend, endpoint, model, migration ou banco foi alterado.
- Validacoes executadas: `npm.cmd run build`, dev server em `http://127.0.0.1:5173`, resposta HTTP `200 OK` em `/login`, resposta HTTP `200 OK` em `/campaigns` e `GET /api/v1/health`.
- Validacao manual de criacao com banco local nao foi concluida porque o Docker/PostgreSQL local nao estava disponivel no ambiente.

### 2026-06-21 - Polish Da Biblioteca De Campanhas

- Refinada tela `/campaigns` na fase `front/game-project-list-create-polish`.
- Substituido feedback de sucesso por toast compacto, evitando faixa alta e espaco morto.
- Adicionado layout adaptativo para 0, 1-2 e 3+ campanhas.
- Substituido painel tutorial fixo por painel compacto `Acoes da biblioteca` quando houver 1 ou 2 campanhas.
- Estado vazio passou a concentrar a orientacao inicial com texto curto e CTA de primeira campanha.
- Refinados cards de campanha com metadados de sistema, mundo, jogadores pendentes, proxima sessao pendente e ultima atualizacao.
- Adicionado menu secundario de acoes no card, com correcao de clipping para impedir corte da opcao `Arquivar`.
- Implementado arquivamento de campanha via endpoint existente `POST /game-projects/{project_id}/archive`.
- Adicionada confirmacao antes do arquivamento, informando que a campanha sai da biblioteca principal sem exclusao permanente.
- Adicionadas abas simples `Ativas` e `Arquivadas`, usando `GET /game-projects?include_archived=true` e filtro local.
- Mantida exclusao permanente fora do escopo.
- Jogadores ativos e proxima sessao foram documentados como pendencias funcionais porque nao existem campos ou relacoes no backend atual.
- Nenhum backend, endpoint, model, migration ou banco foi alterado.
- Validacoes executadas: `npm.cmd run build`, criacao de conta via API, criacao de campanha via API, arquivamento via API, listagem ativa, listagem com arquivadas, resposta HTTP `200 OK` em `/campaigns` e `git diff --check`.

### 2026-06-21 - Correcao De Imersao Da Biblioteca De Campanhas

- Identificado que a tela `/campaigns` ainda apresentava um vazio vertical grande no topo em desktop.
- Causa tecnica: `.projects-page` era um grid com `min-height` e sem alinhamento inicial, permitindo que o navegador distribuisse a sobra vertical entre as linhas.
- Corrigido o alinhamento da pagina com `align-content: start`, mantendo hero, abas e conteudo ancorados no topo util da tela.
- Reduzida a altura minima do hero da biblioteca e aproximados filtros/conteudo para remover espaco morto.
- Estado vazio recebeu composicao cartografica mais imersiva, com mapa maior, trilha de fundo, camadas de terreno e CTA alinhado ao bloco narrativo.
- Mantida a correcao anterior do menu secundario dos cards para impedir corte da opcao `Arquivar`.
- Nenhum backend, endpoint, model, migration ou banco foi alterado.
- Validacoes executadas: `npm.cmd run build` e `git diff --check`.

### 2026-06-21 - Empty State Hibrido De Primeira Campanha

- Refinado estado vazio de Campanhas & Crônicas com a Opcao C: boas-vindas imersiva, texto editorial curto e CTA forte para primeira campanha.
- Substituido o bloco visual retangular por composicao cartografica integrada ao painel, com tomo aberto, rotas, marcadores, rosa dos ventos e selo discreto do Nat 1 em CSS.
- Atualizado texto principal do estado ativo para comunicar inicio de cronica e proximo passo de criacao.
- Mantido CTA `Criar primeira campanha` acionando o modal existente de criacao, sem navegacao externa.
- Estado vazio da aba Arquivadas foi mantido compacto para nao competir com o empty state principal.
- Ajustado texto de confirmacao de arquivamento para informar remocao da biblioteca principal e recuperacao futura.
- Mantida validacao de URL de capa apenas para `http` e `https`.
- Nenhum backend, endpoint, model, migration, banco, upload, IA, calendario ou jogadores foi alterado.
- Validacoes executadas: `npm.cmd run build`, resposta HTTP `200 OK` em `/campaigns`, resposta HTTP `200 OK` em `/api/v1/health`, cadastro/login temporario via API, criacao de campanha, arquivamento e listagem com arquivadas.

### 2026-06-21 - Ajuste Condicional Do Empty State De Campanhas

- Fase: `front/game-project-list-create-polish`.
- Estado vazio ativo passou a diferenciar biblioteca sem histórico e biblioteca com campanhas arquivadas.
- Biblioteca sem campanhas usa título de primeira campanha e CTA `Criar primeira campanha`.
- Biblioteca com campanhas arquivadas e nenhuma ativa usa título `Nenhuma campanha ativa no momento.`, CTA `Criar nova campanha` e ação secundária `Ver arquivadas`.
- Ação `Ver arquivadas` alterna diretamente para a aba Arquivadas.
- CTA superior `Nova campanha` fica oculto quando o empty state ativo concentra a ação principal.
- CTA superior `Nova campanha` permanece disponível quando existem campanhas ativas.
- Removida ação duplicada de criação no painel `Acoes da biblioteca`.
- Hero do empty state recebeu ajuste de altura, colunas, espaçamentos e composição cartográfica para melhor leitura em desktop e viewport intermediário.
- Corrigida nomenclatura acentuada de `Campanhas & Crônicas` nos arquivos principais da fase.
- Nenhum backend, endpoint, model, migration, banco, upload, IA, calendário ou jogador foi alterado.
- Validações executadas: `npm.cmd run build`, `GET /api/v1/health`, validação funcional temporária com Playwright e Microsoft Edge, cenários ativos 0/arquivadas 0, ativos 0/arquivadas maior que 0, ativos maior que 0, viewport 900x720, varredura textual de nomenclatura e `git diff --check`.

### 2026-06-21 - Remocao Do Painel Lateral Da Biblioteca

- Fase: `front/game-project-list-create-polish`.
- Removido componente lateral `GameProjectsActionPanel` da rota `/campaigns`.
- Removida renderização do painel `Acoes da biblioteca` para evitar coluna auxiliar com ações repetidas ou secundárias.
- Layout com 1-2 campanhas passou a usar lista focalizada em uma única coluna, com largura máxima controlada para evitar esticamento excessivo dos cards.
- Layout com 3 ou mais campanhas manteve grid de cards.
- A ação de criação permanece na topbar quando existem campanhas ativas.
- O acesso a campanhas arquivadas permanece nas abas `Ativas` e `Arquivadas`.
- Nenhum backend, endpoint, model, migration, banco, upload, IA, calendário ou jogador foi alterado.
- Validações executadas: `npm.cmd run build`, varredura de importações e estilos do painel removido, e `git diff --check`.

### 2026-06-21 - Ajuste De Ritmo Vertical Da Biblioteca

- Fase: `front/game-project-list-create-polish`.
- Aplicada regra de respiro vertical na tela `/campaigns` entre topbar, hero, filtros e lista.
- Hero recebeu aumento controlado de altura, `padding-top` e espaçamento interno entre kicker, título e subtítulo.
- Filtros e cards receberam intervalo maior para reduzir compressão visual no topo da página.
- Lista focalizada manteve largura máxima controlada e não voltou a usar painel lateral.
- Nenhum backend, endpoint, model, migration, banco, upload, IA, calendário ou jogador foi alterado.
- Validações executadas: `npm.cmd run build`, medição renderizada em viewport desktop e `git diff --check`.

### 2026-06-21 - Correcao De Interacao Dos Cards De Campanha

- Fase: `front/game-project-list-create-polish`.
- Substituido menu secundario baseado em `details` por menu controlado em React.
- Menu de arquivamento passou a fechar com clique externo, mudança de foco e tecla Escape.
- Ação `Arquivar` fecha o menu antes de abrir a confirmação de arquivamento.
- Textos nao interativos dos cards receberam cursor padrão, seleção desabilitada e `caret-color` transparente para evitar indicação visual de edição.
- Mantidos botões, modal de criação e confirmação de arquivamento como elementos interativos normais.
- Nenhum backend, endpoint, model, migration, banco, upload, IA, calendário ou jogador foi alterado.
- Validações executadas: `npm.cmd run build`, teste renderizado de abertura/fechamento do menu, validação de estilo de caret e `git diff --check`.

### 2026-06-21 - Architecture Roadmap Checkpoints

- Fase: `docs/architecture-roadmap-checkpoints`.
- Criado plano de arquitetura com camadas de backend, frontend, infra local, fluxos, riscos e lacunas.
- Criado mapa de módulos atuais e planejados, incluindo Auth, GameProjects, Worlds, SystemTemplates, ProjectModuleSettings, Home do Mestre, módulos relacionais, upload futuro e IA/RAG.
- Criado controle de checkpoints por fase com objetivo, entregas, validações, pendências, próxima fase e riscos.
- Criado guia de padrões de engenharia com regras para código, comentários, backend, frontend, segurança, documentação, branches e validações.
- Criado registro de decisões técnicas para FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT, bcrypt, React, TanStack Query, tema Cartógrafo, arquivamento, separação entre campanha/mundo/sistema e IA com aprovação do mestre.
- Atualizados `STATUS_ATUAL.md`, `PROXIMAS_TAREFAS_CODEX.md`, `PLANO_DE_TRABALHO.md`, `PLANO_PRODUTO_E_REFERENCIAS.md`, `README.md`, `apps/api/README.md` e `apps/web/README.md`.
- Preservados histórico técnico, plano de produto, temas aprovados e documentação visual existente.
- Nenhum backend, frontend, endpoint, model, migration, banco, dependência ou redesign visual foi alterado.
- Validações executadas: `npm.cmd run build`, `pytest`, varredura de tom documental proibido, varredura de espaços finais, revisão de arquivos alterados, `git diff --check` e `git status --short --branch`.

### 2026-06-21 - Baseline De Segurança Do MVP

- Fase: `security/baseline-hardening`.
- Branch: `security/baseline-hardening`.
- Revisada configuração de autenticação JWT, storage de token, rotas protegidas, CORS local, schemas, endpoints protegidos e isolamento por usuário.
- Criado `Docs/ControleDeProjeto/RELATORIO_SEGURANCA_BASELINE.md`.
- Reforçado `.gitignore` para caches, artefatos temporários, relatórios locais e bancos locais.
- Adicionada validação para impedir `SECRET_KEY` placeholder fora de ambientes locais/teste.
- Atualizado `apps/api/.env.example` com placeholder explícito de desenvolvimento local.
- Adicionada validação backend para `cover_image_url`, aceitando apenas URLs `http` e `https`.
- Adicionados testes para token inválido em `/auth/me` e erro genérico no login com e-mail inexistente.
- Adicionados testes de IDOR para update, archive e restore de GameProject de outro usuário.
- Adicionado teste para rejeição de `cover_image_url` com protocolo inseguro.
- `pytest` direto falhou no Python global por ausência de `psycopg`; validação aprovada pelo `.venv` local.
- `ruff check .` direto falhou porque `ruff` não está no `PATH` global; validação aprovada pelo `.venv` local.
- Validações executadas: `.\.venv\Scripts\python.exe -m pytest`, `.\.venv\Scripts\python.exe -m ruff check .`, `.\.venv\Scripts\python.exe -m pip check`, `npm.cmd run build`, `npm.cmd audit`, varreduras textuais de segurança, `git diff --check` e `git status --short --branch`.
- Resultado: 33 testes backend aprovados, `ruff` aprovado, build frontend aprovado, `pip check` sem dependências quebradas e `npm audit` com 0 vulnerabilidades reportadas.
- Pendências registradas: `localStorage` para token JWT, ausência de rate limiting, CORS de produção, security headers, lock de dependências backend e credenciais locais do Docker Compose.

### 2026-07-18 - Preparação Técnica Local De G0 E Consolidação De Direção

- Fase: continuação de `security/baseline-hardening`.
- Branch: `security/baseline-hardening`.
- Confirmado que branch, `main` e `origin/main` ainda apontam para `7cd56d7`; todo o trabalho permanece sem commit no working tree.
- Alinhada a URL padrão do PostgreSQL com Docker Compose e `.env.example`.
- `ENVIRONMENT`, `DATABASE_URL` e `SECRET_KEY` passaram a ser obrigatórios em toda execução; configuração ausente ou inválida interrompe a inicialização da API (fail-closed).
- Fora de local/teste, a URL/credencial documentada do banco é recusada e CORS exige HTTPS com host não-loopback; secret e expiração de token também receberam validações restritivas.
- Adicionados headers HTTP baseline e verificação de hash dummy para login com usuário inexistente.
- Novos hashes passaram a usar `passlib` `bcrypt_sha256`, com limite de 128 caracteres; hashes bcrypt legados permanecem verificáveis e são regravados oportunisticamente após login válido.
- Tentativas com mais de 128 caracteres e credenciais bcrypt legadas acima de 72 bytes são recusadas com erro genérico; o segundo caso dependerá do futuro fluxo de reset de senha.
- Fixadas dependências Python e criado `apps/api/requirements.lock`.
- Substituído `python-jose` por `PyJWT==2.13.0`: `ecdsa` possuía CVE-2024-23342/GHSA-wj6h-64fc-37mp sem versão corrigida, enquanto o Nat 1 usa somente `HS256`; a troca removeu dependências assimétricas desnecessárias do lock.
- Criado teste PostgreSQL integrado sem `Base.metadata.create_all()`.
- Criado workflow `.github/workflows/ci.yml` com backend, PostgreSQL, Alembic, frontend, lint, testes, build e auditorias.
- Adicionados ESLint, Vitest e dois testes de smoke do componente `Button`.
- Corrigido fallback instável de lista em `GameProjectsPage` identificado pelo lint de hooks.
- PostgreSQL 16 validado em container descartável, porta `55432`, `tmpfs` e sem volume persistente.
- Aprovados `upgrade head`, `current`, `check`, smoke integrado, `downgrade base`, novo `upgrade head` e novo smoke.
- Container descartável parado e removido; nenhum banco persistente do projeto foi alterado.
- Backend aprovado com Ruff, `58 passed` unitários e `1 warning` upstream de Starlette/TestClient; integração PostgreSQL permaneceu separada e foi aprovada com `1 passed`; `pip check` limpo.
- Frontend aprovado em lint, typecheck, `2 passed` Vitest e build.
- Instalação npm reportou 0 vulnerabilidades; auditorias online explícitas locais foram bloqueadas pela política de envio de metadados e permanecem como gate remoto do Pull Request.
- Incorporado integralmente o documento `VALIDACAO_PRODUTO_E_ESTRATEGIA_DADOS.md` recebido do usuário.
- Criados escopo vertical/gates, C4/deployment, modelo de ameaças/autorização/LGPD, plano de qualidade/CI e sistema de marca/tokens.
- Consolidado o fluxo canônico `sessão → cena → acontecimento → recap → pendência`.
- Agenda completa movida para o gate opcional G4A, posterior ao vertical e condicionado à validação de H5; módulos relacionais, documentos, PDF e IA bloqueados até validação com mestres.
- Ajustados planos, módulos, fila, status, checkpoint e READMEs para eliminar próximas fases concorrentes.
- Figma autorizado pelo usuário, mas o conector não foi exposto nesta sessão; nenhuma alteração em arquivo Figma foi realizada.
- Nenhum commit, Pull Request ou merge foi executado automaticamente.

### 2026-07-18 - Autorização Para Publicação E Integração De G0

- Gabriel autorizou explicitamente o commit das alterações, a publicação da branch e o avanço até a conclusão do G0.
- GitHub CLI autenticado como `GabrielB-B`; repositório alvo confirmado como `GabrielB-B/nat1-rpg-engine`, base `main`.
- O fechamento permanece condicionado a CI remoto verde, auditorias aprovadas e revisão do Pull Request.
- O conector Figma continuou indisponível e não faz parte deste commit de segurança, qualidade e documentação.

### 2026-07-18 - Pull Request, Correção De Auditoria E Aprovação Técnica De G0

- Criado o commit `65b9f34` com a baseline de segurança, arquitetura, produto, qualidade e identidade visual documentada.
- Publicada a branch `security/baseline-hardening` e aberto o PR [#13](https://github.com/GabrielB-B/nat1-rpg-engine/pull/13) contra `main`.
- A primeira execução remota aprovou o frontend, PostgreSQL, migrations, lint e testes, mas o `pip-audit` bloqueou `pydantic-settings==2.14.1` e `starlette==1.2.1`.
- Aplicado o patch mínimo: `pydantic-settings==2.14.2` no manifesto e lock, e `starlette==1.3.1` no lock; FastAPI, Pydantic, HTTPX e AnyIO permaneceram nas versões compatíveis já fixadas.
- A correção foi registrada no commit `569e9e1`; localmente, `pip check`, Ruff e `58 passed` unitários foram aprovados.
- A política local impediu o envio explícito do inventário de dependências ao serviço público de auditoria; nenhuma tentativa de contorno foi realizada.
- A execução remota [29651420670](https://github.com/GabrielB-B/nat1-rpg-engine/actions/runs/29651420670) aprovou backend, PostgreSQL, ciclo reversível de migrations, testes, `pip-audit`, frontend, build e `npm audit`.
- G0 ficou tecnicamente aprovado; a entrada deste registro em `main` pelo PR #13 materializa o encerramento do gate.

### 2026-07-18 - Início De G1 Visual E Recuperação Do Acesso Ao Figma

- Fase: G1 — `front/cartographer-brand-tokens`.
- Branch: `front/cartographer-brand-tokens`.
- Corrigida a leitura do gate: G1 não é apenas documental e passa a exigir especificação, implementação candidata rastreável, QA com evidências e aprovação explícita de Gabriel.
- Criada a primeira construção vetorial candidata do símbolo Cartógrafo, acompanhada de micro marca e favicon; esses ativos são provisórios e não representam logo final ou autorização comercial.
- Criado componente central `BrandMark` e iniciada a substituição dos placeholders de marca nos pontos existentes do frontend.
- Adicionadas Alegreya e Source Sans 3 em WOFF2 self-hosted, com cópias das licenças OFL e registro no inventário de ativos.
- Consolidado contrato de tokens semânticos para Cartógrafo, Sombrio/Terror e Futurista Humanista, preservando aliases temporários para a interface existente.
- O plugin Figma e o MCP remoto foram habilitados na configuração global do Codex. O OAuth foi concluído anteriormente no host; a revalidação externa ficou inconclusiva no runner isolado. Como ferramentas MCP não são injetadas na thread já aberta, a extensão precisa ser reiniciada e o trabalho retomado em nova thread para uso do conector.
- Nenhum arquivo Figma foi alterado nesta etapa.
- Separadas bordas decorativas de bordas operacionais por `--control-border`; os três temas agora possuem teste automático de contraste para texto, ações, status, foco e limites de controle.
- SVGs cartográficos antes embutidos como data-URI foram externalizados em `public/illustrations`; gradientes e elementos DOM passaram a consumir tokens de marca/mapa, com tratamento centralizado dos SVGs por tema.
- Adicionados testes de paridade geométrica entre `BrandMark`, SVG público, micro marca e favicon.
- QA técnico aprovado com lint, TypeScript, 15 testes, build e XML de 9 SVGs. A autenticação foi inspecionada sem overflow em 320, 360, 390, 768 e 1440 px, com evidências Cartógrafo, Horror, Futurista e foco visível versionadas.
- Criados `INVENTARIO_DE_ATIVOS.md` e `RELATORIO_QA_VISUAL_G1.md` para rastreabilidade. QA visual permanece parcial e a aprovação explícita de Gabriel continua pendente; G1 não foi encerrado.

## Restricoes De Escopo Mantidas

- Nao implementar IA/RAG no MVP 1 inicial.
- Nao implementar jogadores ou permissoes avancadas nesta fase.
- Nao criar mapas interativos avancados no primeiro corte.
- Nao transformar a tela tecnica inicial na Home final do Mestre sem tarefa propria.
- Nao adicionar CRUDs fora da tarefa ativa.
