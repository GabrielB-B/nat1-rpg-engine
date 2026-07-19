# Inventário de Ativos Visuais

- Projeto: Nat 1 RPG Engine
- Gate: G1 — fundação visual profissional
- Branch: `front/cartographer-brand-tokens`
- Data: 2026-07-18
- Status: inventário de ativos candidatos/provisórios

## Regra de classificação

Este inventário separa implementação técnica, aprovação visual e liberação comercial:

| Estado | Significado |
| --- | --- |
| Candidato | Pode ser avaliado e testado internamente; sujeito a substituição ou refinamento. |
| Aprovado em G1 | Passou pelo QA registrado e recebeu aprovação visual explícita de Gabriel. |
| Liberado comercialmente | Além de G1, possui proveniência, licenças, originalidade, similaridade e pesquisa marcária resolvidas. |

Nenhum ativo desta versão está classificado como final ou liberado comercialmente.

## Referências conceituais externas

| Referência | Localização | Uso autorizado nesta etapa | Proveniência/direitos | Estado |
| --- | --- | --- | --- | --- |
| `logonat1.png` — composição escura | Anexo fornecido por Gabriel; não versionado no repositório | Referência de atmosfera para Sombrio/Terror | Origem e direitos de uso ainda precisam ser confirmados antes de qualquer publicação comercial | Referência apenas |
| `1000661361.png` — composição clara | Anexo fornecido por Gabriel; não versionado no repositório | Referência conceitual de chapéu, d20 e anel para Cartógrafo | Origem e direitos de uso ainda precisam ser confirmados antes de qualquer publicação comercial | Referência apenas |

Os anexos não são arquivos mestres e não devem ser simplesmente vetorizados, recoloridos
ou publicados. A construção final precisa ser original, reprodutível e submetida aos gates
de similaridade e pesquisa marcária.

## Ativos de marca candidatos

| Ativo | Caminho | Origem técnica | Uso atual | Estado e pendência |
| --- | --- | --- | --- | --- |
| Símbolo Cartógrafo | `apps/web/public/brand/nat1-symbol-cartographer-candidate.svg` | SVG construído nesta branch a partir do briefing e dos invariantes documentados | Avaliação em tamanhos médios/grandes e referência estática | Candidato; pendem QA, refinamento, aprovação e liberação comercial |
| Micro marca | `apps/web/public/brand/nat1-micro-mark.svg` | Redução óptica construída nesta branch | Favicon e superfícies abaixo de 32 px | Candidata; pendem testes em 16/24/32 px e aprovação |
| Favicon | `apps/web/public/favicon.svg` | Aplicação candidata da micro marca | Navegador em ambiente local/de revisão | Candidato; acompanha o estado da micro marca |
| Componente de marca | `apps/web/src/components/brand/BrandMark.tsx` | Composição React/SVG versionada | Símbolo, micro marca e lockups na aplicação | Implementação candidata; wordmark vetorial mestre ainda pendente |
| Testes do componente | `apps/web/src/components/brand/BrandMark.test.tsx` | Testes automatizados do repositório | Semântica e variações do componente | Resultado deve ser registrado no relatório de QA |

## Tipografia

| Família | Pacote/versão | Arquivo servido | Licença preservada | Estado |
| --- | --- | --- | --- | --- |
| Alegreya Variable | `@fontsource-variable/alegreya@5.2.8` | `apps/web/public/fonts/alegreya-latin-variable.woff2` | `apps/web/public/fonts/LICENSE-ALEGREYA-OFL.txt` | Implementada como tipografia display candidata sob OFL-1.1 |
| Source Sans 3 Variable | `@fontsource-variable/source-sans-3@5.2.9` | `apps/web/public/fonts/source-sans-3-latin-variable.woff2` | `apps/web/public/fonts/LICENSE-SOURCE-SANS-3-OFL.txt` | Implementada como tipografia de interface candidata sob OFL-1.1 |

Integração técnica: `apps/web/src/styles/fonts.css`, com `font-display: swap`, subset Latin
e fallbacks definidos no sistema de marca. Os arquivos de licença devem permanecer junto
às fontes em distribuições que as incluam.

## Tokens e aplicação

| Recurso | Caminho | Finalidade | Estado |
| --- | --- | --- | --- |
| Contrato de temas | `apps/web/src/styles/themes.css` | Tokens semânticos para `cartographer`, `dark_horror` e `humanist_futuristic` | Implementação candidata; resultados de contraste e renderização devem constar no QA |
| Regras globais | `apps/web/src/styles/globals.css` | Tipografia, foco, movimento reduzido e aplicação visual | Implementação candidata; pendem inspeção nos estados e breakpoints |
| Testes dos temas | `apps/web/src/styles/themes.test.ts` | Presença do contrato e pares de contraste | Resultado deve ser registrado no relatório de QA |
| Mapeamento Tailwind | `apps/web/tailwind.config.ts` | Consumo do contrato semântico por utilitários | Compatibilidade técnica em revisão nesta branch |

O contrato separa `--border-default` (divisão ornamental) de `--control-border`
(limite operacional mínimo de 3:1). Os testes também protegem os tokens consumidos
diretamente por `BrandMark`, mapas, sombras, tipografia e textura.

## Ilustrações cartográficas decorativas

| Ativo | Caminho | Uso | Estado |
| --- | --- | --- | --- |
| Topografia superior | `apps/web/public/illustrations/topography-page-top.svg` | textura global de página | Candidata; tratamento por tema aplicado em CSS |
| Topografia inferior | `apps/web/public/illustrations/topography-page-bottom.svg` | textura global de página | Candidata; tratamento por tema aplicado em CSS |
| Topografia da autenticação | `apps/web/public/illustrations/topography-auth.svg` | painel narrativo de acesso | Candidata; tratamento por tema aplicado em CSS |
| Mapa amplo | `apps/web/public/illustrations/map-wide.svg` | previews de mapa | Candidato; base legada externalizada e filtrada por tema |
| Mapa de estado vazio | `apps/web/public/illustrations/empty-welcome-map.svg` | composição de onboarding | Candidato; base legada externalizada e filtrada por tema |
| Mapa de card | `apps/web/public/illustrations/map-card.svg` | capas de campanha | Candidato; base legada externalizada e filtrada por tema |

Esses arquivos substituem data-URIs embutidos e tornam a proveniência técnica e a
manutenção auditáveis. Antes do pacote comercial, as três ilustrações com mapa ainda
devem ser convertidas para máscaras monocromáticas ou variantes vetoriais finais, sem
depender de filtros para adaptar a paleta.

## Ativos finais ainda ausentes

- fonte vetorial mestre editável e seu grid de construção;
- wordmark final convertido/desenhado em vetor;
- lockups finais vertical e horizontal como arquivos independentes;
- variantes monocromática e reversa aprovadas;
- derivações Horror e Futurista com geometria final idêntica;
- PNGs aprovados em 1x/2x/4x e pacote de distribuição;
- relatório de originalidade/similaridade e pesquisa marcária;
- aprovação explícita de Gabriel e registro de liberação comercial.

## Controle de aprovação

- QA técnico: aprovado na rodada registrada em `RELATORIO_QA_VISUAL_G1.md`.
- QA visual: parcial; permanecem as pendências perceptivas e de superfícies autenticadas registradas no relatório.
- Aprovação visual de Gabriel: pendente.
- Liberação comercial: não concedida.
- Próxima revisão do inventário: após o QA visual ou qualquer troca de geometria, fonte ou licença.
