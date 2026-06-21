# Plano De Produto E Referencias

Projeto: Nat 1 RPG Engine

Data de referencia: 2026-06-05

## Objetivo Do Produto

O Nat 1 RPG Engine deve evoluir como uma plataforma de gestao, criacao e organizacao de campanhas de RPG de mesa.

O produto deve atender primeiro o mestre, com foco em preparar, organizar, consultar e evoluir campanhas com consistencia. A expansao futura deve incluir assistencia por IA, upload de materiais e automacao de organizacao de conteudo, sempre com aprovacao do mestre antes de alterar informacoes canonicas.

## Direcao Estrategica

1. Entregar primeiro a Home do Mestre.
2. Consolidar Campanhas & Crônicas como unidade principal de trabalho.
3. Criar modulos internos relacionais dentro de cada campanha.
4. Manter Mundo / Cenario como camada ampla de worldbuilding, separada da campanha.
5. Manter Sistema / Template separado do mundo, permitindo campanhas com regras e estruturas diferentes.
6. Preparar IA e PDF inteligente como camadas futuras de assistencia, nao como substituto da decisao do mestre.

## Referencias De Produto

| Referencia | Papel Para O Nat 1 | Elementos Observados | Limites Para O Nat 1 |
| --- | --- | --- | --- |
| Kanka | Referencia principal de organizacao modular. | Campanhas, categorias modulares, personagens, locais, organizacoes, diarios, mapas, calendarios, timelines e controle do que fica ativo em cada campanha. | Nao copiar estrutura visual ou terminologia integral; usar como referencia de arquitetura modular. |
| World Anvil | Referencia secundaria de worldbuilding e estrutura editorial. | Artigos wiki, mapas interativos, timelines, templates e campanha RPG. | Evitar excesso de complexidade inicial e publicacao enciclopedica antes do fluxo do mestre estar funcional. |
| LegendKeeper | Referencia secundaria de wiki, atlas e navegacao por mapas. | Wiki colaborativa, mapas vinculados a artigos, pins, nesting de mapas, timelines e boards. | Nao priorizar mapas avancados antes dos modulos essenciais. |
| Campfire | Referencia secundaria de organizacao editorial e modular. | Modulos de personagens, locais, culturas, magia, itens, mapas, sistemas, paineis customizaveis e links entre elementos. | Nao transformar o Nat 1 em ferramenta de escrita literaria antes de consolidar RPG e campanha. |
| Notion | Referencia de flexibilidade organizacional. | Paginas, databases, wikis, propriedades, visualizacoes e organizacao por workspace. | Nao depender de configuracao manual excessiva para tarefas basicas do mestre. |
| Obsidian | Referencia de relacoes entre notas e pensamento em rede. | Links entre notas, grafo local/global e canvas visual. | Evitar grafo decorativo sem utilidade operacional para campanha. |
| Roll20 | Referencia secundaria de mesa e journal. | Journal com personagens, handouts, folders, permissoes e uso durante sessoes. | Nao usar Roll20 como referencia principal de UX; o Nat 1 deve priorizar organizacao, criacao e continuidade de campanha. |

## Diferencial Do Nat 1

- Fluxo guiado a partir da Home do Mestre.
- Organizacao por Campanhas & Crônicas antes de modulos profundos.
- Modulos relacionais planejados desde a base.
- Separacao entre campanha, mundo e sistema.
- IA como assistente de criacao, revisao e organizacao, com controle humano.
- Upload de PDF e materiais como entrada para catalogacao assistida.
- Conteudo sugerido pela IA deve passar por revisao e aprovacao antes de virar dado oficial.
- Design system tematico, com Cartografo como tema inicial e suporte futuro a temas alternativos.

## Principios De Arquitetura De Produto

- Toda entidade criada deve pertencer a um usuario e respeitar isolamento de dados.
- Campanhas devem operar como conteiner funcional dos modulos internos.
- Mundos devem permitir reutilizacao e expansao independente de campanhas.
- Sistemas/Templates devem modelar regras, campos e convencoes sem se misturar ao lore do mundo.
- Modulos internos devem ser ativaveis, ordenaveis e consultaveis por campanha.
- Relacoes entre entidades devem ser tratadas como parte central do produto, nao como recurso secundario.
- IA deve produzir sugestoes, resumos, classificacoes e organizacao assistida; a persistencia canonica deve exigir decisao explicita do mestre.

## Roadmap Direcional

| Ordem | Fase Recomendada | Objetivo | Resultado Esperado |
| --- | --- | --- | --- |
| 1 | `front/game-project-list-create` | Criar listagem e cadastro inicial de Campanhas & Crônicas no frontend. | Primeiro fluxo real: login, listar campanhas e criar campanha. |
| 2 | `front/home-master-real-data` | Conectar a Home do Mestre aos dados reais ja disponiveis. | Home com dados da conta, estados vazios e CTA funcional. |
| 3 | `front/game-project-dashboard-shell` | Criar shell interna da campanha com contexto do projeto ativo. | Entrada clara para modulos, summary e navegacao por campanha. |
| 4 | `back/session-scene-foundation` | Criar fundacao backend de sessoes e cenas. | Primeiros modulos internos do MVP com CRUD testado. |
| 5 | `front/session-scene-foundation` | Criar telas iniciais de sessoes e cenas. | Mestre registra sessoes e organiza cenas dentro da campanha. |
| 6 | `back/relational-modules-foundation` | Expandir entidades centrais: personagens, locais, organizacoes, documentos, notas e relacoes. | Base relacional para worldbuilding e campanha. |
| 7 | `front/relational-modules-shell` | Criar navegacao e shells para os modulos relacionais. | Experiencia modular consistente sem depender de CRUD completo em todos os modulos. |
| 8 | `back/document-ingestion-foundation` | Preparar upload controlado de PDFs e documentos. | Materiais podem ser enviados, armazenados, indexados e revisados sem IA generativa obrigatoria. |
| 9 | `back/ai-assist-foundation` | Criar assistencia inicial de IA com aprovacao do mestre. | Sugestoes, classificacoes e resumos nao alteram dados oficiais sem aprovacao. |
| 10 | `front/ai-review-workbench` | Criar bancada de revisao de sugestoes da IA. | Mestre aprova, edita ou rejeita organizacoes propostas. |

## Proxima Fase Recomendada

Fase: `front/home-master-real-data`

Objetivo: conectar a Home do Mestre aos dados reais ja disponiveis, usando a listagem e criacao de campanhas implementadas no frontend.

## Escopo Da Proxima Fase

- Consumir campanhas reais na Home do Mestre.
- Exibir estado vazio quando a conta ainda nao tiver campanhas.
- Destacar campanha recente ou principal quando existir dado real.
- Ajustar CTAs da Home para apontar para `/campaigns`.
- Preservar a Home visualmente alinhada ao tema `cartographer`.
- Manter CRUD visual completo de modulos internos fora do escopo.
- Manter edicao, arquivamento, upload, PDF e IA fora do escopo.
- Atualizar documentacao e validar build/dev server.

## Criterios De Aceite Da Proxima Fase

- Usuario autenticado acessa a Home do Mestre com dados reais basicos.
- Usuario anonimo continua sendo redirecionado para `/login`.
- Campanhas reais influenciam os cards e CTAs principais da Home.
- Estado vazio orienta a criacao da primeira campanha em `/campaigns`.
- Erros da API aparecem com mensagem controlada sem stack trace.
- Layout respeita o tema `cartographer` e o design system existente.
- `npm.cmd run build` passa.
- `npm.cmd run dev` funciona.
- Backend, banco e migrations nao sao alterados.

## Fontes Consultadas

- Kanka: `https://kanka.io/features/`
- World Anvil: `https://www.worldanvil.com/about`
- LegendKeeper: `https://www.legendkeeper.com/features/`
- Campfire: `https://www.campfirewriting.com/worldbuilding-tools`
- Notion: `https://developers.notion.com/guides/data-apis/working-with-databases`
- Obsidian: `https://help.obsidian.md/plugins/graph`
- Roll20: `https://help.roll20.net/hc/en-us/articles/360039675133-Journal/`
