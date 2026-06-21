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
- Registrada direcao de produto: Home do Mestre, Campanhas & Cronicas, modulos relacionais, mundo amplo, sistemas/templates separados e IA com aprovacao do mestre.
- Registradas referencias de produto: Kanka, World Anvil, LegendKeeper, Campfire, Notion, Obsidian e Roll20.
- Definida Kanka como referencia principal de organizacao modular.
- Definidas World Anvil, LegendKeeper e Campfire como referencias secundarias de worldbuilding e estrutura editorial.
- Definidas Notion e Obsidian como referencias de flexibilidade organizacional.
- Definido Roll20 como referencia secundaria de journal e mesa, sem papel de UX principal.
- Atualizada proxima fase recomendada para `front/game-project-list-create`.
- Validacoes executadas: pesquisa de referencias oficiais, revisao dos documentos de controle, varredura de tom documental, `git diff --check` e `npm.cmd run build`.
- Nenhum backend, endpoint, model, migration, banco ou codigo de frontend foi alterado nesta etapa.

## Restricoes De Escopo Mantidas

- Nao implementar IA/RAG no MVP 1 inicial.
- Nao implementar jogadores ou permissoes avancadas nesta fase.
- Nao criar mapas interativos avancados no primeiro corte.
- Nao transformar a tela tecnica inicial na Home final do Mestre sem tarefa propria.
- Nao adicionar CRUDs fora da tarefa ativa.
