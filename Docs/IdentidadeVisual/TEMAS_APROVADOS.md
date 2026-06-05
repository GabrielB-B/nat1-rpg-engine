# Nat 1 - Temas Visuais Aprovados

## Estado do projeto

Esta documentacao foi consolidada antes da fase `front/setup-foundation`.

O objetivo e impedir divergencia visual antes da criacao do frontend, dos tokens de tema, das CSS variables, do Tailwind e do design system inicial.

## Regra geral

A UX base deve permanecer consistente entre os temas. Os temas mudam atmosfera, paleta, textura, icones, avatares e contraste, mas nao reinventam a navegacao.

A estrutura base aprovada para dashboard inclui menu lateral, cards, busca no topo, campanha ativa, notas rapidas e visao organizada.

## Tema 1 - Cartografo / Modelo C

- Chave tecnica: `cartographer`
- Papel: tema principal/original e padrao inicial do produto.
- Uso: fantasia, medieval, exploracao, campanha classica e worldbuilding.
- Direcao visual: claro, cartografico, pergaminho, verde cartografico, dourado, mapas, jornada, campanha e mundo vivo.
- UX base: menu lateral, cards, busca no topo, campanha ativa, notas rapidas e dashboard organizado.
- Personalidade: ferramenta moderna de campanha, nao sistema administrativo generico.

### Paleta resumida

| Token visual | Cor |
| --- | --- |
| Pergaminho claro | `#F4EAD2` |
| Marfim | `#FFF8E8` |
| Verde cartografico | `#556B4E` |
| Musgo suave | `#6F7F58` |
| Dourado envelhecido | `#B58A42` |
| Tinta marrom | `#4A3424` |
| Vermelho selo | `#A1533F` |
| Linha mapa | `#C9B77E` |

### Elementos visuais

- Icones: mapa, bussola, dado, pena, pergaminho, estandarte, ruina, sessao, local, personagem.
- Texturas: papel leve, linhas de mapa, marcas cartograficas discretas.
- Avatares: 2D fantasy/editorial, sem hiper-realismo.
- Dashboard: cards claros, hierarquia limpa, foco em continuar campanha e consultar modulos.

### Observacoes para frontend

- Este e o primeiro tema a ser implementado funcionalmente.
- A chave `cartographer` deve ser o valor padrao de `theme`.
- Componentes nao devem depender diretamente da estetica de pergaminho; devem consumir tokens.

## Tema 2 - Sombrio/Terror / Modelo II

- Chave tecnica: `dark_horror`
- Papel: tema atmosferico escuro.
- Uso: investigacao, horror, Vampiro, Ordem Paranormal, Call of Cthulhu, conspiracao e arquivo proibido.
- Direcao visual: dossie, ritual, investigacao proibida, documento marcado pelo tempo e terror sobrio.
- Restricao: nao usar simbolos demoniacos explicitos como identidade principal.
- UX base: a mesma do Cartografo, com alteracao de atmosfera, textura, icones, avatares e contraste.

### Paleta resumida

| Token visual | Cor |
| --- | --- |
| Carvao | `#111111` |
| Preto arquivo | `#1A1715` |
| Osso antigo | `#D8C7A5` |
| Sangue seco | `#6E1E1A` |
| Cinza fumaca | `#4D4A45` |
| Verde petroleo ritual | `#263F3B` |
| Bronze velho | `#8A6A3C` |
| Papel queimado | `#B9A27E` |

### Elementos visuais

- Icones: olho, arquivo, vela, mascara, dossie, evidencia, sangue seco, selo, documento rasgado.
- Texturas: papel queimado, ruido, cinza fumaca, bordas gastas, carimbo de arquivo.
- Avatares: noir/gotico, retratos de dossie, silhuetas investigativas.
- Dashboard: mais compacto, misterioso, mas sem perder leitura e clareza.

### Observacoes para frontend

- A chave `dark_horror` deve nascer prevista nos tokens.
- O tema pode ter contraste mais alto, mas a legibilidade nao pode ser sacrificada.
- A navegacao continua compartilhada com os demais temas.

## Tema 3 - Futurista Humanista / Modelo II

- Chave tecnica preferencial: `humanist_futuristic`
- Alias aceitavel futuro, apenas se necessario: `futuristic`
- Papel: tema tecnico/imersivo para sci-fi.
- Uso: sci-fi, naves, space opera, tecnologia, futuro elegante e investigacao tecnologica.
- Direcao visual: interface limpa, imersiva, elegante, espacial, com inspiracao humanista e sensacao de painel de bordo.
- Influencia aprovada: tecnologia elegante e humanista, com sensacao proxima de interfaces como Detroit: Become Human.
- UX base: a mesma estrutura geral do Cartografo, mas com componentes mais limpos, brilho controlado e icones tecnicos.

### Paleta completa aprovada

| Token visual | Cor |
| --- | --- |
| Branco frio | `#F2F6F7` |
| Azul aco | `#3A5E72` |
| Ciano suave | `#72C7D1` |
| Grafite tecnico | `#1B242C` |
| Dourado suave | `#C3A66A` |
| Azul profundo | `#102B3A` |
| Cinza interface | `#B8C4C9` |
| Violeta orbital | `#5A4B7A` |

### Elementos visuais

- Icones: nave, radar, terminal, estrela, chip, constelacao, missao, tripulacao, mapa orbital.
- Texturas: grids sutis, paineis translucidos, linhas de interface, glow controlado.
- Avatares: 2D/3D limpo, androide humanista, tripulacao, piloto, explorador espacial.
- Dashboard: claro, tecnico, elegante, com cards de bordo e leitura rapida.

### Observacoes para frontend

- A chave preferencial para tokens e persistencia deve ser `humanist_futuristic`.
- O alias `futuristic` so deve ser usado se houver necessidade tecnica futura de compatibilidade.
- Este tema deve nascer previsto nos tokens desde o inicio, mesmo que a primeira implementacao funcional seja Cartografo.
- Deve lembrar navegacao, painel de missao, mapas estelares, radar, tripulacao e dados de bordo.
- Deve usar brilho controlado, cards limpos, componentes tecnicos e icones de nave/interface.

### Alertas explicitos

- Nao repetir Cartografo.
- Nao usar cyberpunk pesado.
- Nao usar estetica medieval, pergaminho, mapa antigo ou fantasia classica.
- Nao substituir por verde cartografico, dourado envelhecido e textura de papel.
- Manter estetica elegante, humanista, espacial e tecnica.

## Comparativo

| Tema | Chave | Uso principal | Papel no produto |
| --- | --- | --- | --- |
| Cartografo | `cartographer` | Fantasia, medieval, exploracao, worldbuilding | Tema padrao inicial |
| Sombrio/Terror | `dark_horror` | Horror, investigacao, ocultismo | Tema escuro atmosferico |
| Futurista Humanista | `humanist_futuristic` | Sci-fi, naves, futuro elegante | Tema tecnico/imersivo |

## Notas para o frontend futuro

- Criar tokens por tema desde o inicio.
- Nao prender componentes ao tema Cartografo.
- A navegacao deve ser compartilhada entre temas.
- O frontend deve aceitar troca de tema por `theme_key`.
- O tema Cartografo sera o primeiro implementado funcionalmente.
- Sombrio/Terror e Futurista Humanista devem nascer previstos nos tokens.
- Evitar repetir paleta do Cartografo no Futurista Humanista.
- Evitar transformar o Futurista Humanista em cyberpunk pesado.
- Preparar CSS variables ou design tokens para:
  - `background`;
  - `surface`;
  - `border`;
  - `text`;
  - `text-muted`;
  - `primary`;
  - `accent`;
  - `danger`;
  - `success`;
  - `warning`.
