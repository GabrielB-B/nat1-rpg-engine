# Relatório de QA Visual — G1

- Projeto: Nat 1 RPG Engine
- Branch: `front/cartographer-brand-tokens`
- Data da execução: 2026-07-18
- Status: QA técnico aprovado; QA visual parcial com ressalvas
- Decisão do gate: **G1 em andamento — aguarda pendências visuais e aprovação de Gabriel**

## Metadados da execução

| Campo | Registro |
| --- | --- |
| Base Git avaliada | `d34418e` + working tree da branch G1 ainda sem commit |
| Sistema operacional | Windows, PowerShell |
| Navegadores | Chrome `150.0.7871.125` via CDP isolado; Edge `150.0.4078.65` headless |
| Node.js/npm | Node `22.16.0`; npm `10.9.2` |
| URL/ambiente | `http://127.0.0.1:5173/login`, Vite local |
| Responsável | Codex, com revisão técnica independente de subagente |
| Data/hora de fechamento desta rodada | 2026-07-18 15:45:01 -03:00 |

O Node local está abaixo do mínimo canônico do repositório (`>=22.23.1`). Os comandos
passaram, mas CI permanece a fonte de verdade para o runtime suportado.

## Gate automatizado

| Verificação | Comando | Resultado | Evidência/observação |
| --- | --- | --- | --- |
| ESLint | `npm.cmd run lint` | aprovado | zero warnings e zero erros |
| TypeScript | `npm.cmd run typecheck` | aprovado | `tsc -b --pretty` concluído |
| Testes | `npm.cmd run test -- --run` | aprovado | 3 arquivos, 15 testes |
| Build de produção | `npm.cmd run build` | aprovado | Vite, 1.863 módulos; CSS 65,12 kB e JS 391,18 kB |
| XML dos SVGs | parse dos SVGs em `public` | aprovado | 9 arquivos válidos |
| Diff | `git diff --check` | aprovado | sem erro de whitespace; apenas aviso LF/CRLF do ambiente |
| Auditoria de dependências | auditoria automática do `npm install` | aprovado com ressalva | instalação reportou 0 vulnerabilidades; repetição isolada de `npm audit` foi bloqueada pela política do ambiente e deve rodar no CI |
| Contrato de tokens | `themes.test.ts` | aprovado | três temas e tokens semânticos/de marca obrigatórios |
| Pares de contraste | `themes.test.ts` | aprovado | texto, ações, status, foco e borda operacional nos três temas |
| Paridade geométrica | `BrandMark.test.tsx` | aprovado | JSX, SVG público, micro marca e favicon protegidos contra drift de paths |

## Resultados numéricos de contraste

As bordas decorativas continuam deliberadamente suaves. Controles usam
`--control-border`, com os seguintes mínimos medidos contra superfície/página:

| Tema | Superfície | Página | Resultado |
| --- | ---: | ---: | --- |
| Cartógrafo | 4,83:1 | 4,16:1 | aprovado |
| Sombrio/Terror | 5,70:1 | 6,04:1 | aprovado |
| Futurista Humanista | 9,14:1 | 8,40:1 | aprovado |

O foco usa anel opaco de 3 px. Na captura móvel, o e-mail focado retornou
`outlineWidth: 3px` e `outlineColor: rgb(107, 74, 30)`.

## Matriz da marca candidata

| Cenário | Resultado | Evidência/achado |
| --- | --- | --- |
| Micro marca em 16 px | pendente | precisa de inspeção óptica dedicada em favicon real |
| Micro marca em 24 px | pendente | precisa de inspeção óptica dedicada |
| Micro marca em 32 px | pendente | componente usa redução própria, mas falta captura isolada |
| Símbolo em 48–96 px | aprovado com ressalva | autenticação mostra 54/62 px; faltam pranchas nos tamanhos exatos |
| Símbolo em 256 px | pendente | sem prancha isolada |
| Lockup horizontal >= 160 px | aprovado | desktop e mobile sem quebra ou clipping |
| Lockup vertical >= 220 px | pendente | variante existe em código, ainda sem prancha |
| Fundo claro | aprovado | Cartógrafo e Futurista Humanista |
| Fundo escuro | aprovado | Sombrio/Terror |
| Fundo de uma cor | pendente | variante monocromática final ainda ausente |
| Fundo fotográfico/texturizado | aprovado com ressalva | textura cartográfica validada; falta fotografia real |
| Impressão/monocromia | pendente | ativo final não produzido |
| Leitura de `NAT 1 RPG` | aprovado | `1` permanece distinguível de `I` e `L` nas capturas |

## Matriz de interface e responsividade

| Superfície/viewport | Resultado | Evidência/achado |
| --- | --- | --- |
| Autenticação — 320 x 900 | aprovado | `innerWidth = scrollWidth = 320`; captura versionada |
| Autenticação — 360 x 900 | aprovado | `innerWidth = scrollWidth = 360`; sem corte na inspeção |
| Autenticação — 390 x 900 | aprovado | `innerWidth = scrollWidth = 390`; sem corte na inspeção |
| Autenticação — 768 x 1024 | aprovado | hierarquia e espaçamento preservados |
| Autenticação — 1440 x 1100 | aprovado | composição equilibrada em duas colunas |
| Sidebar/micro marca | pendente | integração existe, mas não houve captura autenticada nesta rodada |
| Empty state/símbolo | pendente | integração existe, mas não houve captura autenticada nesta rodada |
| Zoom 200% | aprovado com ressalva | reflow a 320 px e ausência de overflow comprovados; falta sessão manual com zoom do navegador |
| Navegação por teclado | aprovado com ressalva | foco do campo comprovado e validação leva ao primeiro campo inválido; falta percorrer toda a ordem de tabulação manualmente |
| `prefers-reduced-motion` | aprovado com ressalva | regra global revisada; emulação perceptiva ainda pendente |

## Temas e estados

| Estado | Cartógrafo | Sombrio/Terror | Futurista Humanista | Observação |
| --- | --- | --- | --- | --- |
| Texto principal/secundário | aprovado | aprovado | aprovado | tokens e render inicial validados |
| Link e foco | aprovado | aprovado por contraste | aprovado por contraste | foco visual capturado no Cartógrafo |
| Botão primário | aprovado | aprovado | aprovado | texto/fundo passam 4,5:1 |
| Botão secundário | aprovado por contrato | aprovado por contrato | aprovado por contrato | borda operacional passa 3:1 |
| Hover/active | aprovado com ressalva | aprovado por código | aprovado por código | tratamento cromático implementado; faltam capturas temáticas |
| Disabled | aprovado por contrato | aprovado por contrato | aprovado por contrato | contraste mínimo de 3:1 no par inativo |
| Loading | pendente | pendente | pendente | sem captura nesta rodada |
| Erro/danger | aprovado por contrato | aprovado por contrato | aprovado por contrato | sem captura de formulário inválido |
| Sucesso/warning | aprovado por contrato | aprovado por contrato | aprovado por contrato | sem captura de toast |
| Informação sem depender só de cor | aprovado com ressalva | aprovado com ressalva | aprovado com ressalva | estados atuais usam texto/ícone; fluxo completo ainda precisa QA |

Os temas alternativos foram carregados antes da inicialização da aplicação. A troca
dinâmica por campanha continua fora do G1 e não deve ser inferida dessas capturas.

## Testes perceptivos complementares

| Verificação | Resultado | Evidência/observação |
| --- | --- | --- |
| Protanopia | pendente | simulação dedicada ainda não executada |
| Deuteranopia | pendente | simulação dedicada ainda não executada |
| Tritanopia | pendente | simulação dedicada ainda não executada |
| Textura não interfere na leitura | aprovado | autenticação legível nos três temas |
| Geometria equivalente entre temas | aprovado | mesmo componente/paths; apenas tokens mudam |

## Achados e tratativas

| ID | Severidade | Descrição | Correção | Estado |
| --- | --- | --- | --- | --- |
| G1-QA-01 | alta | CSS legado empilhava o lockup horizontal | seletores antigos removidos; responsividade recapturada | resolvido |
| G1-QA-02 | alta | bordas de campos abaixo de 3:1 | criado `--control-border`, aplicado e testado | resolvido |
| G1-QA-03 | alta | halo de foco composto ficava abaixo de 3:1 | foco opaco de 3 px e testes contra página/superfície | resolvido |
| G1-QA-04 | média | data-URIs e gradientes cartográficos estavam acoplados ao Cartógrafo | gradientes migrados para tokens e SVGs externalizados em `public/illustrations` | resolvido com ressalva |
| G1-QA-05 | média | SVG público e JSX podiam divergir silenciosamente | óptica da micro marca alinhada e teste de paridade adicionado | resolvido |
| G1-QA-06 | média | auditoria npm isolada não pôde ser repetida | manter auditoria como job obrigatório de CI | aberto fora do visual |
| G1-QA-07 | média | falta prova óptica 16/24/32, lockup vertical, sidebar e empty state | produzir prancha/frames no Figma após reinício da extensão | aberto |
| G1-QA-08 | média | erros de autenticação não estavam associados aos campos nem levavam foco ao primeiro inválido | adicionados `name`, `aria-invalid`, `aria-describedby`, política de correção do e-mail e gestão de foco | resolvido |

Os SVGs cartográficos externalizados preservam a geometria dos data-URIs anteriores.
Build e XML passaram após a refatoração. A próxima rodada deve recapturar as superfícies
autenticadas e, antes da liberação comercial, substituir filtros por máscaras ou variantes
vetoriais finais.

## Evidências versionadas

- `evidencias/g1/auth-cartographer-desktop-1440.png`
- `evidencias/g1/auth-cartographer-mobile-320.png`
- `evidencias/g1/auth-cartographer-focus-390.png`
- `evidencias/g1/auth-dark-horror-desktop-1440.png`
- `evidencias/g1/auth-humanist-futuristic-desktop-1440.png`

Também foram inspecionados viewports transitórios de 360, 390 e 768 px. Os cinco arquivos
acima são o conjunto mínimo persistido para evitar inflar o repositório com duplicatas.

O plugin Figma e o MCP remoto estão habilitados na configuração global. O OAuth foi
concluído anteriormente no host; a tentativa de revalidá-lo nesta rodada foi inconclusiva
porque o runner isolado não alcança o endpoint externo. A extensão ainda exige reinício e
nova thread para expor as ferramentas. Nenhum arquivo Figma foi alterado nesta etapa.

## Decisão de saída

- Especificação coerente: **aprovada para a candidata**.
- Implementação candidata rastreável: **aprovada**.
- QA técnico: **aprovado**.
- QA visual: **parcial; pendências G1-QA-06 e G1-QA-07**.
- Aprovação explícita de Gabriel: **pendente**.
- Marca final: **não declarada**.
- Liberação comercial: **não concedida**.

G1 permanece em andamento. O próximo passo correto é reiniciar a extensão, levar o
componente e as evidências ao Figma, produzir a prancha de reduções/lockups e obter a
decisão visual explícita de Gabriel.
