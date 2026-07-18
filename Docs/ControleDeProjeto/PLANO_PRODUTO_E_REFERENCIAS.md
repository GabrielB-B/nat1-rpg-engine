# Plano De Produto E Referencias

Projeto: Nat 1 RPG Engine

Data de referencia original: 2026-06-05

Última atualização: 2026-07-18

Status: referência histórica, subordinada aos documentos canônicos de 2026-07-18.

Autoridade atual:

- estratégia e métricas: `VALIDACAO_PRODUTO_E_ESTRATEGIA_DADOS.md`;
- recorte e gates: `ESCOPO_MVP_VERTICAL_E_GATES.md`;
- fila executável: `PROXIMAS_TAREFAS_CODEX.md`.

Documentos complementares:

- Arquitetura técnica: `Docs/ControleDeProjeto/PLANO_ARQUITETURA.md`.
- Módulos atuais e planejados: `Docs/ControleDeProjeto/MODULOS_DO_SISTEMA.md`.
- Checkpoints por fase: `Docs/ControleDeProjeto/CHECKPOINTS.md`.
- Padrões de engenharia: `Docs/ControleDeProjeto/PADROES_DE_ENGENHARIA.md`.
- Decisões técnicas: `Docs/ControleDeProjeto/DECISOES_TECNICAS.md`.

## Objetivo Do Produto

O Nat 1 RPG Engine deve evoluir como uma plataforma de gestao, criacao e organizacao de campanhas de RPG de mesa.

O produto deve atender primeiro o mestre, com foco em preparar, organizar, consultar e evoluir campanhas com consistencia. A expansao futura deve incluir assistencia por IA, upload de materiais e automacao de organizacao de conteudo, sempre com aprovacao do mestre antes de alterar informacoes canonicas.

## Direcao Estrategica

1. Concluir a fundação de segurança, PostgreSQL, migrations e CI.
2. Consolidar Campanhas & Crônicas como unidade principal de trabalho.
3. Entregar Home real e shell contextual sem dados ou controles fictícios.
4. Provar o vertical sessão → cena → acontecimento → recap → pendência.
5. Validar o fluxo com mestres reais antes de módulos relacionais.
6. Manter Mundo / Cenário e Sistema / Template como conceitos separados.
7. Preparar personagens, locais, relações, documentos, PDF e IA apenas após os gates.

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

O roadmap operacional deixou de ser mantido neste documento para evitar direções
concorrentes. A única fila executável é `PROXIMAS_TAREFAS_CODEX.md`, organizada pelos
gates definidos em `ESCOPO_MVP_VERTICAL_E_GATES.md`.

## Proxima Fase Recomendada

Fase: encerrar G0 por revisão e integração aprovada da branch
`security/baseline-hardening`.

## Escopo Da Proxima Fase

- revisar diff e evidências de PostgreSQL real;
- obter autorização de commit e abrir Pull Request;
- integrar somente após CI verde;
- iniciar G1/G2 em branches próprias após a integração.

## Criterios De Aceite Da Proxima Fase

- PostgreSQL 16 descartável aprovado em `upgrade → teste → downgrade → upgrade`;
- backend, lint, frontend, build e testes aprovados;
- CI versionado e revisado;
- status/checkpoint refletem integração pendente, sem declarar merge inexistente;
- commit e PR continuam dependentes de aprovação de Gabriel.

## Fontes Consultadas

- Kanka: `https://kanka.io/features/`
- World Anvil: `https://www.worldanvil.com/about`
- LegendKeeper: `https://www.legendkeeper.com/features/`
- Campfire: `https://www.campfirewriting.com/worldbuilding-tools`
- Notion: `https://developers.notion.com/guides/data-apis/working-with-databases`
- Obsidian: `https://help.obsidian.md/plugins/graph`
- Roll20: `https://help.roll20.net/hc/en-us/articles/360039675133-Journal/`
