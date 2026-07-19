# Sistema de Marca e Design Tokens

- Projeto: Nat 1 RPG Engine
- Versão: 1.1 — fundação candidata para QA e aprovação visual
- Data: 2026-07-18
- Status: especificação e implementação candidata/provisória; marca final e uso comercial não aprovados

## Estado da implementação de G1

A branch `front/cartographer-brand-tokens` materializa esta especificação em uma primeira
fundação técnica, sem antecipar a decisão visual de Gabriel:

- símbolo Cartógrafo candidato em SVG;
- micro marca e favicon candidatos;
- componente reutilizável `BrandMark` para símbolo, micro marca e lockups;
- Alegreya e Source Sans 3 self-hosted, com licenças OFL preservadas;
- contrato de tokens semânticos para `cartographer`, `dark_horror` e
  `humanist_futuristic`;
- foco visível, preferência de movimento reduzido e testes automatizados como parte do
  gate técnico.

Os arquivos e licenças estão relacionados em `INVENTARIO_DE_ATIVOS.md`. O primeiro ciclo
de renderização, breakpoints e estados está registrado em `RELATORIO_QA_VISUAL_G1.md`, com
QA técnico aprovado e QA visual parcial. Enquanto as pendências desse relatório e a
aprovação explícita de Gabriel permanecerem abertas, todos os ativos continuam
**candidatos**. Eles não devem ser apresentados como logo final ou ativo liberado para uso
comercial.

O plugin Figma e o MCP remoto estão habilitados na configuração global do Codex. O OAuth
foi concluído anteriormente no host, mas a revalidação remota não pode ser repetida pelo
runner isolado desta thread, que não possui saída de rede. A extensão precisa ser
reiniciada e o trabalho retomado em nova thread para carregar as ferramentas. Nenhum
arquivo Figma foi modificado durante esta implementação local.

## Direção de marca

O Nat 1 deve parecer uma ferramenta premium de memória e continuidade narrativa, não
um painel administrativo fantasiado. A marca combina:

- **acaso:** o resultado natural `1` no dado;
- **ofício do mestre:** chapéu, tinta, selo e preparação;
- **orientação:** rosa dos ventos, órbita ou traço cartográfico;
- **memória:** pergaminho, arquivo e marcas de jornada.

O tom é autoral, culto e acolhedor. Ornamentação existe para criar atmosfera, mas não
compete com leitura, estados ou tarefas durante uma sessão.

## Diagnóstico dos anexos

### Anexo escuro

Pontos fortes:

- silhueta do chapéu e d20 é memorável;
- marfim, ouro envelhecido e vermelho selo combinam com a linguagem do produto;
- funciona como ponto de partida natural para `dark_horror`.

Limites:

- excesso de textura e detalhe perde legibilidade em tamanhos pequenos;
- o preto dominante desloca a marca principal para horror;
- lettering desgastado não deve ser usado como tipografia de interface;
- símbolo e palavra precisam de uma construção vetorial reproduzível.

### Anexo claro

Pontos fortes:

- composição clara, premium e amigável;
- chapéu, d20 e anel ornamental formam o melhor esqueleto para a marca principal;
- a leitura sobre pergaminho conversa diretamente com o Cartógrafo.

Limites:

- roxo e teal saturados não pertencem à paleta Cartógrafo atual;
- aquarela e brilhos finos não escalam para favicon ou navegação;
- o lockup precisa ser reconstruído, não apenas recolorido pixel a pixel.

Decisão recomendada: manter a **geometria conceitual do anexo claro** como base e usar o
anexo escuro como referência de acabamento para a variante Horror.

## Invariantes da marca

Todas as variações de tema devem preservar:

1. chapéu assimétrico com ponta reconhecível;
2. d20 frontal parcialmente sobreposto ao chapéu;
3. número `1` como foco central;
4. anel de orientação com quatro pontos cardeais;
5. proporções e área de proteção iguais;
6. wordmark `NAT 1 RPG` sem trocar estrutura entre temas.

Temas alteram paleta, textura e tratamento de linha. Não alteram a identidade geométrica.
Esses invariantes comparam lockups temáticos equivalentes. A micro marca é uma redução
óptica deliberada e pode preservar apenas `N1` ou a face central do dado quando o conjunto
completo não for legível.

## Família de logotipos

Família final desejada:

| Ativo | Uso |
| --- | --- |
| Lockup principal vertical | landing, materiais institucionais e telas amplas |
| Lockup horizontal | header, autenticação e documentos |
| Símbolo chapéu + d20 | sidebar, avatar de produto e splash |
| Micro marca `N1` simplificada | favicon e tamanhos abaixo de 32 px |
| Monocromática tinta | impressão simples e fundos claros |
| Reversa marfim | fundos escuros |
| Variante por tema | Cartógrafo, Horror e Futurista com geometria idêntica |

A implementação atual cobre uma candidata técnica do símbolo, micro marca e lockups
compostos pelo componente `BrandMark`. Isso não equivale à entrega da família final: o
wordmark vetorial mestre, variantes monocromática/reversa, exportações raster e arquivos
fonte editáveis permanecem condicionados a QA e aprovação.

O wordmark deve ser desenhado ou convertido em vetor final. Texto produzido em imagem
gerativa serve apenas como conceito, nunca como arquivo mestre.

Antes de qualquer uso comercial, Gabriel deve confirmar a proveniência e os direitos de
uso dos dois anexos. O vetor mestre será uma reconstrução original a partir do briefing,
com verificação de similaridade e pesquisa marcária; os anexos não serão simplesmente
vetorizados ou publicados. Fontes, texturas e demais recursos terão licença e autoria
registradas em um inventário de ativos.

## Variações por tema

### Cartógrafo — principal

- fundo: pergaminho ou transparente;
- linha: `#4A3424`;
- preenchimento claro: `#FFF8E8`;
- chapéu: verde cartográfico `#556B4E`, com sombra musgo `#6F7F58`;
- estrutura do d20 e órbita: dourado envelhecido `#B58A42`;
- `1` e gema cardeal: vermelho selo `#A1533F`;
- textura: papel e hachura muito leves, removidas na micro marca.

### Sombrio/Terror

- fundo: carvão `#111111` ou transparente;
- linha/preenchimento: osso antigo `#D8C7A5`;
- d20 e órbita: bronze velho `#B58A50`;
- `1`: sangue seco `#A8483F` com contraste reforçado por contorno;
- textura: gravura/dossiê controlada;
- não usar símbolos demoníacos como identidade central.

### Futurista Humanista

- fundo: branco frio `#F2F6F7` ou azul profundo `#102B3A`;
- estrutura: azul aço `#3A5E72`;
- sinais luminosos: ciano `#72C7D1` somente como acento;
- detalhe premium: dourado suave `#C3A66A`;
- `1`: violeta orbital `#5A4B7A` ou branco na reversa;
- tratamento: linhas geométricas e painel de nave, sem estética cyberpunk pesada.

## Área de proteção e tamanho mínimo

Definir `x` como a largura da face central do número `1` no d20.

- área de proteção: ao menos `1x` em todos os lados;
- símbolo detalhado: mínimo recomendado de 48 px digital;
- micro marca: 16, 24 e 32 px com desenho próprio;
- lockup horizontal: mínimo recomendado de 160 px;
- lockup vertical: mínimo recomendado de 220 px;
- abaixo desses limites, remover textura e ornamentos, não apenas reduzir o raster.

## Usos proibidos

- distorcer proporções ou inclinar o lockup;
- trocar apenas o chapéu ou o dado entre temas;
- aplicar gradiente roxo/azul genérico ao Cartógrafo;
- usar sombra neon no Horror;
- colocar o logo detalhado sobre textura de baixo contraste;
- usar lettering raster como texto editável da interface;
- gerar uma nova forma de logo a cada campanha;
- copiar símbolos, lettering ou composição proprietária de outra marca.

## Tipografia da fundação candidata

### Interface

- display e títulos editoriais: **Alegreya**, pesos 500–700;
- corpo e controles: **Source Sans 3**, pesos 400–700;
- fallbacks: Georgia para display; `Segoe UI`, system-ui e sans-serif para corpo.

As fontes estão self-hosted em WOFF2 com subset Latin e cópias das licenças OFL no
repositório. O inventário registra pacote, versão e caminho. O wordmark candidato em
interface pode compor os tipos durante G1, mas o wordmark final não deve depender da fonte
de interface: ele terá desenho vetorial próprio após aprovação.

Critérios:

- suporte completo a português;
- algarismos legíveis e tabulares onde necessário;
- corpo mínimo de 16 px em campos e textos operacionais;
- line-height confortável entre 1.45 e 1.65;
- títulos usam `text-wrap: balance` e corpo longo usa `text-wrap: pretty` quando suportado.

## Tokens semânticos

Componentes não devem consumir `gold`, `moss` ou `cyan` diretamente. A API visual mínima:

```text
--page-bg
--surface-1
--surface-2
--surface-raised
--surface-inset
--border-default
--border-strong
--control-border
--text-primary
--text-secondary
--text-disabled
--action-primary-bg
--action-primary-text
--action-secondary-bg
--action-secondary-text
--link
--focus-ring
--overlay
--status-success
--status-warning
--status-danger
--danger-action-bg
--danger-action-text
--disabled-bg
--disabled-text
```

`--border-default` permanece sutil e decorativo. Limites que identificam campos,
busca e botões contornados devem consumir `--control-border`, validado em pelo menos
3:1 contra `--surface-1` e `--page-bg`. `--border-strong` fica reservado a ênfase,
seleção e composição de marca.

O contrato também exige os tokens de marca e ilustração `--brand-*`, `--art-line`,
`--map-land`, `--map-water`, `--map-route` e `--texture-opacity`. Geometria não muda
entre temas; somente cor, tipografia display e tratamento de textura podem variar.

Pares interativos recomendados, calculados segundo WCAG:

| Tema/uso | Fundo | Texto | Contraste aproximado |
| --- | --- | --- | --- |
| Cartógrafo primário | `#3F573B` | `#FFF8E8` | 7,52:1 |
| Cartógrafo secundário | `#EAD6A6` | `#382717` | 9,97:1 |
| Cartógrafo danger | `#8A3F32` | `#FFF8E8` | 6,99:1 |
| Horror ouro | `#B58A50` | `#111111` | 6,04:1 |
| Horror secundário | `#263F3B` | `#E2D4B8` | 7,73:1 |
| Futurista primário | `#294C60` | `#FFFFFF` | 9,14:1 |
| Futurista ciano | `#72C7D1` | `#102B3A` | 7,56:1 |
| Futurista violeta | `#5A4B7A` | `#FFFFFF` | 7,71:1 |

O dourado e o ciano podem continuar ornamentais, mas texto claro sobre eles é proibido.

## Movimento e textura

- transições usam somente propriedades explícitas, preferencialmente `opacity` e `transform`;
- `prefers-reduced-motion` remove movimento não essencial;
- uma entrada orquestrada vale mais que animações dispersas;
- textura nunca reduz contraste de texto ou foco;
- gradientes e elementos cartográficos em CSS devem consumir tokens, evitando marrom hardcoded nos outros temas;
- SVGs decorativos legados foram externalizados em `public/illustrations` e recebem
  tratamento temático centralizado; a conversão final para máscaras monocromáticas
  continua pendente antes de liberar o pacote comercial;
- glow futurista é restrito a foco, status ou destaque operacional.

## QA visual obrigatório

Esta lista é condição de saída de G1, não recomendação opcional. Evidências e resultados
devem ser registrados em `RELATORIO_QA_VISUAL_G1.md`; a ausência de evidência mantém o item
pendente.

- lockups em fundo claro, escuro, fotográfico e uma cor;
- símbolo em 16, 24, 32, 48, 96 e 256 px;
- contraste dos pares realmente renderizados;
- daltonismo e informação que não dependa apenas de cor;
- zoom de 200% e reflow sem perda de ação;
- mobile 320/360/390 px, tablet e desktop amplo;
- foco de teclado, hover, active, disabled, loading, erro e sucesso;
- impressão monocromática;
- comparação visual entre temas com a mesma geometria;
- teste do logo ao lado do nome completo, sem confundir o número `1` com `I` ou `L`.

## Processo de finalização

1. aprovar uma construção geométrica em preto e branco;
2. desenhar símbolo, lockups e micro marca em vetor;
3. aplicar primeiro a paleta Cartógrafo;
4. derivar Horror e Futurista sem alterar geometria;
5. testar tamanhos e contraste;
6. exportar SVG otimizado e PNG 1x/2x/4x;
7. registrar fonte mestre, licença, grid e versões;
8. executar gate de originalidade, proveniência e pesquisa marcária;
9. integrar por componente `BrandMark`, nunca por imagem hardcoded em cada tela.

### Estado do processo nesta branch

- etapas 2, 3 e 9 possuem uma implementação **candidata**, sujeita a correções;
- etapas 5 e o QA operacional estão em andamento;
- etapas 1, 4, 6, 7 e 8 não podem ser presumidas concluídas;
- nenhuma etapa substitui a aprovação explícita de Gabriel;
- a aprovação de G1 não substitui a liberação comercial condicionada à proveniência,
  originalidade, licenças, similaridade e pesquisa marcária.
