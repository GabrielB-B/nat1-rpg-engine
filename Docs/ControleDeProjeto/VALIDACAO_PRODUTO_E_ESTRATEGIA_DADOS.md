# Validação de Produto, Estratégia de Mercado e Plano de Métricas — Nat 1 RPG Engine

- **Documento:** Validação de Produto e Estratégia de Dados
- **Projeto:** Nat 1 RPG Engine
- **Status:** Canônico para planejamento; hipóteses ainda dependem de validação
- **Versão:** 1.1
- **Data:** 18/07/2026
- **Documento relacionado:** `PLANO_PRODUTO_E_REFERENCIAS.md`
- **Local definitivo:** `Docs/ControleDeProjeto/VALIDACAO_PRODUTO_E_ESTRATEGIA_DADOS.md`

---

## 1. Finalidade

Este documento complementa o plano de produto existente e formaliza os elementos necessários para orientar decisões de produto, arquitetura, monetização, aquisição e mensuração.

O conteúdo estabelece:

- problema central e estado real de validação;
- perfil de cliente ideal;
- personas e antipersonas;
- tarefas que o mestre de RPG tenta resolver;
- alternativas atuais e gatilhos de migração;
- proposta de valor e diferenciação;
- referências de produto e critérios de adoção;
- hipóteses de monetização;
- métricas de aquisição, ativação, engajamento, retenção e receita;
- plano de instrumentação analítica;
- estratégia de aquisição;
- experimentos de validação;
- critérios objetivos para manter, revisar, adiar ou abandonar hipóteses.

Este documento não substitui o roadmap técnico, o plano de arquitetura ou os checkpoints. Seu papel é conectar a construção técnica a evidências de mercado e resultados mensuráveis.

---

## 2. Resumo executivo

O Nat 1 RPG Engine é uma plataforma web para organização, preparação, condução e continuidade de campanhas de RPG de mesa.

A proposta combina cinco capacidades centrais:

1. **Campaign Workspace** — área operacional da campanha.
2. **Agenda do Mestre** — sessões, indisponibilidades e prevenção de conflitos.
3. **Espinha Narrativa** — campanha, arcos, sessões, momentos e consequências.
4. **Atlas Vivo** — entidades e relações narrativas conectadas.
5. **Memória da Campanha** — histórico, journals, timeline e assistência futura baseada em dados aprovados pelo mestre.

A categoria já possui produtos que comprovam demanda por organização de campanhas, worldbuilding, calendários, timelines, mapas e colaboração. Kanka, World Anvil, LegendKeeper e ScribesBlade oferecem combinações desses recursos e adotam modelos gratuitos, assinaturas ou licença perpétua.[^kanka-features] [^worldanvil-home] [^legendkeeper-pricing] [^scribesblade]

Essa evidência confirma a existência da categoria, mas não valida automaticamente a proposta específica do Nat 1 no mercado brasileiro. O problema deve ser considerado **parcialmente sustentado e ainda não validado de forma empírica**.

A validação do produto depende de três resultados:

- mestres reconhecem a fragmentação e a perda de continuidade como problemas relevantes;
- o fluxo inicial reduz esforço real de preparação e organização;
- usuários ativados retornam para manter campanhas vivas ao longo das semanas.

---

## 3. Estado da validação

### 3.1 Classificação atual

| Dimensão | Estado | Evidência disponível |
|---|---|---|
| Existência da categoria | Sustentada | Produtos internacionais ativos e monetizados |
| Demanda por worldbuilding e campanha | Sustentada | Funcionalidades convergentes em produtos concorrentes |
| Problema de fragmentação de ferramentas | Hipótese forte | Posicionamento de concorrentes e experiência inicial do projeto |
| Demanda no mercado brasileiro | Não validada | Pesquisa formal ainda não executada |
| Disposição a pagar | Não validada | Nenhum teste de preço realizado |
| Retenção de longo prazo | Não validada | Produto ainda sem coortes reais |
| Diferencial Atlas Vivo | Não validado | Conceito planejado, sem teste de uso |
| Agenda com prevenção de conflito | Não validada | Regra de produto definida, sem evidência quantitativa |
| IA com aprovação do mestre | Não validada | Fase futura, dependente de dados estruturados |

### 3.2 Regra de governança

Nenhuma hipótese deve ser apresentada como fato validado sem evidência observável.

Classificações permitidas:

- **Sustentada:** há evidência externa consistente ou comportamento real medido.
- **Validada:** o público-alvo confirmou o problema ou valor em pesquisa e uso.
- **Hipótese forte:** existe coerência com a categoria, mas falta validação direta.
- **Hipótese exploratória:** proposta com evidência insuficiente.
- **Rejeitada:** testes não atingiram os critérios definidos.

---

## 4. Problema central

### 4.1 Formulação do problema

Mestres de RPG que mantêm campanhas recorrentes precisam coordenar informações narrativas, preparação de sessões, agenda, personagens, locais, facções, documentos e consequências.

Na ausência de uma fonte central de verdade, o conteúdo tende a se espalhar entre documentos, planilhas, aplicativos de notas, calendários, chats e VTTs. Essa fragmentação aumenta o tempo de preparação, dificulta a retomada de contexto e eleva o risco de inconsistências narrativas.

### 4.2 Problemas derivados

- dificuldade para localizar informações durante a sessão;
- perda de continuidade entre encontros;
- duplicação de NPCs, locais e notas;
- ausência de visão consolidada da campanha;
- conflitos entre sessões de campanhas diferentes;
- dificuldade para separar informação do mestre e informação dos jogadores;
- relações narrativas mantidas apenas na memória;
- histórico de campanha desconectado da agenda real;
- baixa portabilidade entre ferramentas;
- alto custo de manutenção manual.

### 4.3 Evidência de categoria

O ScribesBlade posiciona seu produto como resposta à fricção causada por ferramentas que exigem excesso de administração e organiza o mundo como peças conectadas, a campanha como uma espinha narrativa, sessões por momentos, timeline configurável e journals com menções clicáveis.[^scribesblade]

Kanka reúne personagens, locais, mapas, calendários, timelines, relações, journals e campanhas em estrutura modular.[^kanka-features]

World Anvil combina gerenciamento de campanhas, agendamento de sessões, timelines, mapas, calendários, relações e Chronicles, que conectam eventos a locais em uma interface temporal e geográfica.[^worldanvil-gm] [^worldanvil-chronicles]

LegendKeeper prioriza criação rápida, mapas, timelines, whiteboards e colaboração, com modelo em que o proprietário paga e convidados participam sem custo.[^legendkeeper-home] [^legendkeeper-pricing]

A convergência de funcionalidades indica uma necessidade real de organizar mundos e campanhas. Não comprova, isoladamente, que o Nat 1 obterá adoção.

---

## 5. Perfil de cliente ideal

### 5.1 ICP primário

**Mestre recorrente com campanha ativa**

Critérios comportamentais:

- conduz pelo menos uma campanha com encontros recorrentes;
- prepara sessões digitalmente;
- utiliza duas ou mais ferramentas para organizar a mesa;
- mantém NPCs, locais, facções, notas ou calendário;
- precisa retomar contexto entre sessões;
- aceita usar uma aplicação web;
- valoriza organização, continuidade e controle;
- possui autonomia para decidir qual ferramenta será usada;
- demonstra interesse em convidar jogadores futuramente.

Sinais de alta aderência:

- mais de uma campanha ativa;
- worldbuilding próprio;
- sessões quinzenais ou semanais;
- uso atual de Notion, Obsidian, Google Drive, planilhas, Discord, Roll20, Foundry ou ferramentas especializadas;
- histórico de perda de notas, contradições ou conflitos de agenda;
- necessidade de separar conteúdo público e privado.

### 5.2 ICP secundário

**Worldbuilder e autor de cenário**

Necessidades principais:

- organizar lore;
- criar timeline;
- conectar entidades;
- manter versões e relações;
- visualizar facções e eventos;
- exportar ou publicar conteúdo.

Aderência futura, após consolidação de Atlas Vivo, timeline e journals.

### 5.3 ICP futuro

**Grupo de jogadores vinculado a uma campanha**

Necessidades principais:

- consultar conteúdo revelado;
- acompanhar agenda;
- confirmar presença;
- receber materiais;
- registrar notas autorizadas;
- visualizar relações públicas.

Jogadores não devem ser tratados como principal pagador na fase inicial.

### 5.4 Antipersonas

Perfis que não devem orientar o MVP:

- pessoa que deseja apenas jogar em VTT, sem organizar conteúdo;
- mestre que conduz apenas sessões isoladas e rejeita ferramentas digitais;
- usuário que busca gerador automático de aventuras sem organização própria;
- estúdio que exige colaboração empresarial avançada antes da validação;
- autor que precisa exclusivamente de software de escrita de romance;
- usuário que espera substituição integral de regras, VTT ou videoconferência.

---

## 6. Personas funcionais

As personas devem ser tratadas como modelos de comportamento, não como estereótipos demográficos.

### 6.1 Mestre Operacional

**Contexto:** mantém uma ou mais campanhas recorrentes.

**Objetivos:**

- preparar sessões rapidamente;
- encontrar informações durante o jogo;
- marcar datas sem conflito;
- registrar o que mudou;
- retomar a campanha sem revisar diversos arquivos.

**Riscos de abandono:**

- onboarding longo;
- formulários excessivos;
- necessidade de cadastrar todo o mundo antes de obter valor;
- instabilidade durante a sessão.

### 6.2 Mestre Construtor de Mundo

**Contexto:** desenvolve cenário próprio, relações políticas e história extensa.

**Objetivos:**

- conectar pessoas, lugares, facções e eventos;
- manter cronologia;
- visualizar relações;
- separar fatos, rumores e segredos;
- reutilizar entidades sem duplicação.

**Riscos de abandono:**

- modelo de dados rígido;
- visualizações superficiais;
- ausência de exportação;
- dificuldade para editar grandes volumes.

### 6.3 Mestre de Campanhas Curtas

**Contexto:** organiza one-shots, mini-séries ou aventuras curtas.

**Objetivos:**

- criar campanha rapidamente;
- organizar elenco, cenas e materiais;
- agendar poucas sessões;
- arquivar sem perder conteúdo.

**Riscos de abandono:**

- complexidade desproporcional;
- exigência de configuração avançada;
- preço incompatível com uso esporádico.

### 6.4 Jogador Colaborador

**Contexto:** participa de uma campanha criada pelo mestre.

**Objetivos futuros:**

- consultar informações permitidas;
- acompanhar agenda;
- confirmar presença;
- registrar notas;
- receber atualizações.

**Restrições:**

- não deve visualizar segredos;
- não deve editar dados do mestre sem permissão;
- não deve pagar para participar de uma campanha básica.

---

## 7. Jobs to Be Done

Jobs to Be Done analisa o progresso que uma pessoa tenta realizar em determinada circunstância, incluindo dimensões funcionais, emocionais e sociais.[^jtbd]

### 7.1 Job principal

> Quando preparo e conduzo uma campanha recorrente, preciso manter informações, sessões, agenda e consequências conectadas, para retomar o contexto rapidamente e preservar a continuidade sem procurar em várias ferramentas.

### 7.2 Jobs funcionais

- criar uma campanha sem configuração excessiva;
- encontrar rapidamente conteúdo relevante;
- preparar uma sessão em sequência operacional;
- registrar consequências após o jogo;
- agendar sessões sem choque de horário;
- manter NPCs, locais e facções em registros canônicos;
- conectar entidades e eventos;
- consultar histórico e timeline;
- controlar o que jogadores podem visualizar;
- arquivar e recuperar campanhas;
- exportar ou preservar dados.

### 7.3 Jobs emocionais

- sentir controle sobre uma campanha complexa;
- reduzir ansiedade antes da sessão;
- confiar que informações importantes não serão perdidas;
- perceber progresso na construção do mundo;
- manter criatividade sem transformar preparação em administração.

### 7.4 Jobs sociais

- apresentar uma campanha organizada;
- fornecer aos jogadores informações claras;
- demonstrar consistência narrativa;
- facilitar compromisso do grupo com datas e materiais.

---

## 8. Alternativas atuais

### 8.1 Categorias de alternativas

| Categoria | Exemplos | Vantagem atual | Limitação para a proposta do Nat 1 |
|---|---|---|---|
| Documentos e nuvem | Google Drive, documentos, planilhas | Flexibilidade e familiaridade | Estrutura manual e baixa conexão entre entidades |
| Notas e wikis genéricas | Notion, Obsidian | Personalização e links | Fluxos de RPG dependem de configuração manual |
| VTTs | Roll20, Foundry | Execução da mesa, mapas e fichas | Organização narrativa não é o foco principal |
| Comunicação | Discord, WhatsApp | Coordenação do grupo | Informação se perde em conversas |
| Calendário genérico | Google Calendar | Agenda confiável | Não conhece campanhas, sessões ou disponibilidade de jogadores |
| Worldbuilding especializado | Kanka, World Anvil, LegendKeeper | Recursos maduros de mundo e campanha | O Nat 1 busca integrar operação de mesa, agenda, Atlas Vivo e idioma português |
| Aplicativo local especializado | ScribesBlade | Mundo conectado, espinha narrativa e timeline | Arquitetura desktop, local e sem colaboração web |

### 8.2 Motivos para migração

A migração só ocorrerá se o valor superar os custos de troca.

Gatilhos potenciais:

- reduzir o número de ferramentas usadas;
- importar conteúdo existente;
- encontrar informação com menos cliques;
- agendar sessões sem conflito;
- abrir uma campanha e recuperar contexto imediato;
- conectar entidades sem duplicação;
- compartilhar apenas conteúdo autorizado;
- obter visualizações que não exigem configuração manual;
- usar interface em português;
- manter backup e exportação confiáveis;
- receber assistência sem perder controle canônico.

### 8.3 Barreiras de migração

- receio de perda de dados;
- necessidade de reescrever conteúdo;
- curva de aprendizado;
- dependência de internet;
- custo de assinatura;
- ausência de integração com VTTs;
- falta de confiança em segurança e disponibilidade;
- dúvida sobre longevidade do produto.

### 8.4 Implicações de produto

Antes de investir em funcionalidades avançadas, devem existir:

- importação mínima por Markdown, CSV ou estrutura documentada;
- exportação completa da campanha;
- política de backup;
- arquivamento reversível;
- onboarding progressivo;
- valor perceptível sem cadastro exaustivo.

---

## 9. Proposta de valor

### 9.1 Formulação

> O Nat 1 organiza a operação e a memória de campanhas de RPG em um ambiente conectado, permitindo preparar, conduzir, agendar e acompanhar histórias sem fragmentar informações entre ferramentas.

### 9.2 Pilares

#### Campaign Workspace

Área interna da campanha com módulos, dados principais e acesso operacional.

#### Agenda do Mestre

Sessões, indisponibilidades, lembretes e prevenção de conflitos.

#### Espinha Narrativa

Campanha, arcos, sessões, momentos, encontros, cliffhangers e consequências.

#### Atlas Vivo

Personagens, locais, facções, itens e eventos conectados por relações estruturadas.

#### Memória da Campanha

Journals, menções, timeline, histórico e assistência futura com aprovação.

#### Visibilidade por papel

Informação privada, exclusiva do mestre, compartilhada com participantes ou pública.

### 9.3 Diferencial estratégico

A diferenciação não deve depender apenas da quantidade de módulos.

O diferencial pretendido é a integração entre:

```text
Agenda real
+ preparação de sessão
+ continuidade narrativa
+ entidades conectadas
+ visualização temporal
+ controle de visibilidade
+ assistência aprovada pelo mestre
```

---

## 10. Referências de produto e decisões de implementação

### 10.1 ScribesBlade

**Inspiração observada:**

- World Bible com elementos conectados;
- campanha organizada como espinha;
- arcos e sessões;
- sessões divididas em momentos ordenáveis;
- timeline configurável por mundo;
- journals hierárquicos;
- menções com `@`;
- separação entre informação do mestre e jogadores;
- imagem canônica reutilizada;
- acessibilidade;
- licença perpétua e operação offline.[^scribesblade]

**Aplicação no Nat 1:**

- entidade canônica;
- Campaign Arc;
- Session Beat;
- timeline do mundo;
- journals conectados;
- content mentions;
- regras de visibilidade;
- Atlas Vivo.

**Não adotar:**

- dependência exclusiva de Windows;
- ausência de conta;
- armazenamento apenas local;
- arquitetura sem sincronização;
- foco restrito a uma experiência desktop individual.

### 10.2 Kanka

**Inspiração observada:**

- estrutura modular;
- personagens, locais, mapas, calendários e timelines;
- relações;
- colaboração;
- núcleo gratuito;
- cobrança por campanhas premium e recursos adicionais.[^kanka-features] [^kanka-pricing]

**Aplicação no Nat 1:**

- módulos ativáveis;
- camada gratuita útil;
- campanhas premium como hipótese;
- organização por domínio;
- permissões e colaboração futura.

### 10.3 World Anvil

**Inspiração observada:**

- campaign manager;
- agendamento de sessões;
- timelines paralelas;
- Chronicles conectando tempo e mapa;
- family trees;
- diplomacy webs;
- mapas e calendários;
- controle de privacidade.[^worldanvil-gm] [^worldanvil-home] [^worldanvil-chronicles] [^worldanvil-pricing]

**Aplicação no Nat 1:**

- agenda integrada ao workspace;
- timeline do mundo separada da agenda real;
- Atlas Vivo;
- visualizações de relações;
- conteúdo público e privado;
- futura área de jogadores.

### 10.4 LegendKeeper

**Inspiração observada:**

- fluxo rápido de criação;
- wiki;
- mapas;
- timelines;
- whiteboards;
- colaboração;
- convidados gratuitos;
- assinatura simples.[^legendkeeper-home] [^legendkeeper-pricing] [^legendkeeper-features]

**Aplicação no Nat 1:**

- experiência sem formulários excessivos;
- edição rápida;
- participação gratuita de jogadores;
- precificação simples;
- colaboração sem cobrança por participante básico.

### 10.5 Referências técnicas planejadas

- **React Flow:** candidato para Atlas Vivo por suportar nós e arestas customizados, conexões interativas, animações e acessibilidade por teclado.[^reactflow-edges] [^reactflow-accessibility]
- **FullCalendar:** candidato para Agenda do Mestre por integração com React, eventos, fusos, seleção, drag-and-drop e redimensionamento.[^fullcalendar-react] [^fullcalendar-docs]
- **Motion for React:** candidato para microinterações e animações controladas, com suporte a redução de movimento.[^motion] [^motion-reduced]
- **TanStack Query:** camada adotada para ciclo de vida, cache, invalidação e mutations de estado remoto.[^tanstack]

A adoção de bibliotecas deve ocorrer apenas na fase correspondente, após avaliação de licença, bundle, acessibilidade, manutenção e necessidade real.

---

## 11. Hipótese de monetização

### 11.1 Estado

A monetização está em fase de hipótese. Nenhum preço deve ser tratado como definitivo antes de testes com usuários qualificados.

O mercado apresenta modelos distintos:

- Kanka mantém núcleo gratuito e cobra a partir de US$ 4,99 por campanhas premium.[^kanka-pricing]
- LegendKeeper cobra US$ 9 mensais ou US$ 90 anuais e permite convidados gratuitos.[^legendkeeper-pricing]
- World Anvil utiliza planos com diferentes limites e recursos, incluindo opções anuais e lifetime.[^worldanvil-pricing]
- ScribesBlade utiliza pagamento único em early access e preço de lançamento anunciado.[^scribesblade]

### 11.2 Modelo principal recomendado para teste

**Freemium orientado ao mestre**

#### Plano Gratuito

Objetivo: validar valor e permitir campanhas reais.

Hipótese de escopo:

- uma campanha ativa;
- campanhas arquivadas preservadas;
- criação básica de sessões;
- agenda básica;
- entidades essenciais;
- limite de armazenamento;
- exportação básica;
- participação básica de jogadores no futuro.

#### Plano Mestre

Objetivo: atender uso recorrente.

Hipótese de escopo:

- múltiplas campanhas ativas;
- agenda completa;
- mais armazenamento;
- timeline;
- módulos relacionais;
- exportação completa;
- personalização visual;
- convites de jogadores;
- backup ampliado.

#### Plano Mestre Pro

Objetivo: atender usuários intensivos e criadores.

Hipótese de escopo:

- limites superiores;
- Atlas Vivo avançado;
- histórico de relações;
- integrações;
- publicação;
- analytics da campanha;
- recursos de IA com franquia;
- templates avançados.

### 11.3 Princípios

- jogadores básicos não devem pagar para participar;
- conteúdo do usuário deve permanecer exportável;
- cancelamento não deve apagar dados;
- IA deve possuir limite separado por custo variável;
- preço deve refletir valor, não apenas quantidade de campos;
- limites não devem impedir o usuário de experimentar o fluxo principal;
- plano gratuito deve ser funcional, mas não substituir indefinidamente o valor dos recursos avançados.

### 11.4 Experimentos de preço

Faixas iniciais para teste, não para publicação:

- R$ 19,90;
- R$ 29,90;
- R$ 39,90;
- plano anual com desconto;
- licença de fundador limitada durante beta.

Métodos:

- entrevista com card de preço;
- landing page com planos;
- pré-venda;
- teste de checkout sem cobrança;
- oferta para beta fechado;
- análise de conversão por faixa.

---

## 12. Estratégia de métricas

A mensuração deve ligar objetivos a sinais e métricas. O framework HEART organiza métricas de experiência em felicidade, engajamento, adoção, retenção e sucesso da tarefa, com processo de Goals–Signals–Metrics.[^heart]

A North Star Metric deve representar o valor obtido pelo cliente e funcionar como indicador antecedente de receita.[^north-star]

As métricas desta seção descrevem a arquitetura futura do produto completo. Durante o
vertical v0, prevalecem a ativação e o funil mínimo da seção 25.3; módulos ainda
bloqueados não podem gerar eventos nem compor o gate operacional.

### 12.1 North Star Metric futura

**Mestres com Continuidade Semanal — MCS**

Definição:

Número de mestres únicos que, em uma janela de sete dias:

1. acessaram uma campanha ativa em pelo menos dois dias distintos; e
2. realizaram pelo menos duas ações de valor.

Ações de valor:

- criar ou atualizar sessão;
- agendar sessão;
- criar evento de calendário;
- criar ou atualizar entidade;
- criar relação;
- registrar journal;
- registrar evento de timeline;
- concluir sessão;
- registrar consequência.

Apenas abrir uma tela não caracteriza continuidade.

### 12.2 Métrica complementar de unidade de valor

**Campanhas Vivas Semanais — CVS**

Número de campanhas com atividade significativa em uma janela de sete dias.

Uso:

- identificar se o produto mantém campanhas em movimento;
- diferenciar usuários com várias campanhas;
- analisar retenção por formato e sistema.

---

## 13. Árvore de métricas

Esta árvore é o catálogo estratégico futuro. A ativação operacional do piloto não usa
Mundo, entidade, calendário, relação ou journal; sua definição versionada está na seção
25.3.

### 13.1 Aquisição

- visitantes qualificados;
- origem de aquisição;
- taxa de visita para cadastro;
- custo por cadastro;
- custo por mestre ativado;
- convites enviados;
- cadastros originados por convite;
- conversão de conteúdo para cadastro.

### 13.2 Ativação futura do produto ampliado

Evento de ativação inicial:

> Campanha criada e primeira ação operacional concluída em até sete dias.

Ações operacionais válidas:

- primeira sessão criada;
- primeira sessão agendada;
- primeiro mundo vinculado;
- primeira entidade cadastrada;
- primeiro evento de calendário criado.

Métricas:

- percentual que cria campanha em 24 horas;
- percentual que conclui ação operacional em sete dias;
- tempo mediano até primeira campanha;
- tempo mediano até primeira sessão;
- abandono por etapa;
- erros de formulário;
- necessidade de suporte.

### 13.3 Engajamento

- dias ativos por semana;
- ações de valor por campanha;
- sessões preparadas;
- eventos de calendário;
- entidades criadas;
- relações criadas;
- journals criados;
- funcionalidades adotadas;
- campanhas acessadas por mestre;
- profundidade de uso sem depender de tempo de tela.

### 13.4 Retenção

- retenção W1;
- retenção W4;
- retenção W8;
- retenção mensal;
- reativação de campanha;
- campanhas arquivadas;
- campanhas recuperadas;
- percentual de campanhas com sessão futura;
- percentual de mestres com atividade em semanas consecutivas.

### 13.5 Receita

- conversão gratuito para pago;
- receita mensal recorrente;
- receita anual recorrente;
- receita média por conta pagante;
- cancelamento;
- downgrade;
- expansão de plano;
- receita de IA;
- custo de infraestrutura por conta;
- margem por plano;
- relação LTV/CAC após volume suficiente.

### 13.6 Qualidade e sucesso da tarefa

- taxa de sucesso ao criar campanha;
- taxa de sucesso ao agendar sessão;
- conflitos corretamente bloqueados;
- erros de API por fluxo;
- tempo para encontrar uma entidade;
- tempo para preparar sessão;
- taxa de recuperação após erro;
- satisfação após tarefa;
- acessibilidade e uso de redução de movimento.

---

## 14. Plano de instrumentação

O catálogo abaixo registra a direção futura e não autoriza instrumentar funcionalidades
inexistentes. Para o piloto, somente os eventos v0 da seção 25.3 e de
`ESCOPO_MVP_VERTICAL_E_GATES.md` podem ser emitidos.

### 14.1 Catálogo futuro de eventos

| Evento | Momento |
|---|---|
| `account_registered` | cadastro concluído |
| `login_succeeded` | autenticação concluída |
| `campaign_created` | campanha criada |
| `campaign_opened` | workspace aberto |
| `campaign_archived` | campanha arquivada |
| `campaign_restored` | campanha restaurada |
| `session_created` | sessão criada |
| `session_scheduled` | data definida |
| `session_completed` | sessão concluída |
| `calendar_event_created` | evento criado |
| `calendar_conflict_blocked` | conflito impedido |
| `entity_created` | entidade criada |
| `entity_updated` | entidade atualizada |
| `relation_created` | relação criada |
| `journal_entry_created` | entrada criada |
| `timeline_event_created` | evento criado |
| `player_invited` | convite enviado |
| `player_joined` | convite aceito |
| `subscription_started` | assinatura iniciada |
| `subscription_cancelled` | assinatura cancelada |

### 14.2 Propriedades permitidas

- identificador interno pseudonimizado;
- plano;
- tipo de campanha;
- formato;
- sistema/template;
- idioma;
- origem de aquisição;
- dispositivo;
- versão da aplicação;
- resultado da ação;
- duração da tarefa;
- código de erro padronizado.

### 14.3 Dados proibidos em analytics

- senha;
- token;
- segredo JWT;
- conteúdo integral de notas;
- descrições privadas;
- nomes reais de jogadores;
- mensagens privadas;
- documentos enviados;
- conteúdo marcado como segredo;
- e-mail em texto aberto, salvo necessidade legal e sistema autorizado.

### 14.4 Governança

- catálogo de eventos versionado;
- nome de evento estável;
- definição única para cada métrica;
- propriedade obrigatória documentada;
- mudanças registradas;
- ambientes de desenvolvimento e produção separados;
- contas internas excluídas de métricas;
- política de retenção definida;
- consentimento e privacidade avaliados antes de ferramenta externa.

---

## 15. Estratégia de retenção

### 15.1 Ciclos naturais de uso

O produto não deve ser avaliado apenas por uso diário. Campanhas podem ser semanais, quinzenais ou mensais.

Coortes recomendadas:

- campanhas semanais;
- campanhas quinzenais;
- campanhas mensais;
- one-shots;
- mini-séries;
- worldbuilding sem sessão ativa.

### 15.2 Mecanismos de retenção

- próxima sessão visível;
- retomada rápida de contexto;
- resumo de alterações;
- pendências narrativas;
- agenda e lembretes;
- histórico de sessões;
- relações atualizadas;
- conteúdo compartilhado com jogadores;
- exportação e segurança de dados;
- progresso perceptível da campanha.

### 15.3 Retenção saudável

Retenção não deve ser artificialmente elevada por notificações excessivas.

O retorno deve ocorrer porque existe trabalho real a concluir:

- preparar;
- consultar;
- agendar;
- registrar;
- revisar;
- compartilhar.

---

## 16. Estratégia de aquisição

### 16.1 Fase 1 — descoberta e beta fechado

Canais:

- comunidades brasileiras de RPG;
- grupos de mestres;
- clubes de RPG;
- Discords;
- fóruns;
- podcasts;
- criadores pequenos e médios;
- mesas presenciais;
- eventos locais;
- rede de contatos do projeto.

Objetivo:

- recrutar mestres qualificados;
- executar entrevistas;
- observar preparação real;
- validar onboarding;
- medir ativação;
- obter depoimentos com autorização.

### 16.2 Fase 2 — conteúdo orientado a problema

Temas:

- organização de campanhas;
- preparação de sessões;
- continuidade narrativa;
- prevenção de conflitos de agenda;
- construção de NPCs conectados;
- timeline;
- separação de segredos;
- gestão de várias campanhas.

Formatos:

- vídeos curtos;
- demonstrações;
- artigos;
- templates;
- guias;
- estudos de uso;
- comparações de fluxo sem atacar concorrentes.

### 16.3 Fase 3 — aquisição orientada pelo produto

Mecanismos:

- convite gratuito de jogadores;
- páginas compartilháveis;
- handouts;
- calendário da campanha;
- templates por sistema;
- exportação;
- campanhas demonstrativas;
- créditos de referência;
- marca discreta em conteúdo público.

### 16.4 Fase 4 — parcerias

- criadores de conteúdo;
- editoras;
- sistemas independentes;
- eventos;
- lojas;
- clubes;
- streamers;
- comunidades de VTT;
- produtores de aventuras.

### 16.5 Métricas por canal

- cadastros qualificados;
- custo;
- ativação;
- retenção W4;
- conversão paga;
- indicação;
- qualidade das campanhas criadas;
- suporte necessário.

Um canal com muitos cadastros e baixa retenção não deve ser considerado eficiente.

---

## 17. Hipóteses e critérios de decisão

Os limites abaixo são metas internas iniciais. Não representam benchmarks universais.

### H1 — Fragmentação é problema relevante

**Teste:** 20 entrevistas com mestres qualificados.

**Validar se:**

- pelo menos 12 relatam fragmentação ou perda de contexto entre os três principais problemas;
- pelo menos 10 usam duas ou mais ferramentas;
- pelo menos 8 descrevem impacto concreto em preparação ou continuidade.

**Revisar se:** 6 a 11 apresentam o problema.

**Rejeitar como problema central se:** menos de 6 apresentam impacto real.

### H2 — O fluxo inicial produz valor

**Teste:** beta com pelo menos 50 cadastros qualificados.

**Validar se:**

- 40% criam campanha em até 24 horas;
- 25% concluem uma ação operacional em até sete dias;
- tempo mediano até primeira campanha inferior a 10 minutos.

**Revisar se:** ativação operacional ficar entre 15% e 24%.

**Reformular onboarding se:** ativação ficar abaixo de 15% após duas iterações.

### H3 — O produto gera retorno recorrente

**Teste:** coorte mínima de 40 usuários ativados.

**Validar se:**

- retenção W4 igual ou superior a 25%;
- retenção W8 igual ou superior a 15%;
- pelo menos 30% mantêm sessão futura ou atividade significativa.

**Revisar se:** W4 entre 15% e 24%.

**Reavaliar o núcleo se:** W4 abaixo de 15% após duas melhorias de produto.

### H4 — Existe disposição a pagar

**Teste:** 30 entrevistas de preço e oferta real para beta.

**Validar se:**

- 30% demonstram escolha positiva em pelo menos uma faixa;
- pelo menos 10 usuários concluem pagamento ou compromisso real;
- principal motivo de rejeição não é ausência de valor básico.

**Revisar se:** interesse entre 15% e 29%.

**Abandonar preço testado se:** menos de 10% aceitarem após clareza de proposta.

### H5 — Agenda é parte central

**Teste:** entrevistas com 15 mestres que conduzem duas ou mais campanhas.

**Validar se:**

- 60% relatam conflito, negociação recorrente ou controle manual de disponibilidade;
- 40% usariam bloqueios pessoais e prevenção automática.

**Adiar como diferencial se:** menos de 30% identificarem valor relevante.

### H6 — Atlas Vivo diferencia o produto

**Teste:** protótipo com 12 mestres e entidades reais.

**Validar se:**

- 70% compreendem a visualização sem explicação longa;
- 60% encontram uma relação específica;
- 50% afirmam que substituiria controle manual;
- tempo de tarefa inferior ao método atual para a maioria.

**Revisar se:** compreensão for alta, mas utilidade inferior a 50%.

**Adiar se:** a visualização for percebida como decoração.

### H7 — Jogadores geram aquisição orgânica

**Teste:** convite real em pelo menos 20 campanhas.

**Validar se:**

- 50% das campanhas enviam convite;
- 60% dos convites são aceitos;
- pelo menos 10% dos jogadores convidados criam campanha própria em 60 dias.

**Revisar se:** participação ocorrer sem geração de novos mestres.

---

## 18. Plano de pesquisa

### 18.1 Entrevistas de problema

Amostra inicial:

- 20 mestres;
- diferentes sistemas;
- campanhas curtas e longas;
- uma e múltiplas campanhas;
- uso digital baixo, médio e alto;
- diferentes frequências de sessão.

Perguntas devem investigar comportamento passado, não intenção genérica.

Tópicos:

- última preparação;
- ferramentas abertas;
- informação perdida;
- conflito de agenda;
- retomada após intervalo;
- compartilhamento com jogadores;
- custo de manutenção;
- ferramenta abandonada;
- decisão de pagamento anterior.

### 18.2 Observação contextual

Observar:

- preparação de uma sessão;
- busca de NPC;
- registro de consequência;
- marcação de próxima data;
- recuperação de contexto.

### 18.3 Teste de usabilidade

Tarefas:

- criar campanha;
- abrir workspace;
- agendar sessão;
- registrar entidade;
- encontrar informação;
- arquivar campanha;
- visualizar relação.

### 18.4 Pesquisa quantitativa

Executar apenas após entrevistas suficientes para formular perguntas corretas.

Objetivos:

- frequência dos problemas;
- ferramentas utilizadas;
- número de campanhas;
- frequência de sessões;
- disposição a pagar;
- prioridade de módulos.

---

## 19. Critérios de priorização

Uma funcionalidade deve avançar quando:

- resolve um job validado;
- possui evidência de uso;
- reduz risco relevante;
- desbloqueia outra função central;
- pode ser medida;
- possui custo proporcional ao valor.

Uma funcionalidade deve ser adiada quando:

- depende de entidades inexistentes;
- é apenas visual;
- não possui hipótese mensurável;
- cria grande custo de manutenção;
- não altera ativação ou retenção;
- compromete segurança;
- aumenta complexidade antes de gerar valor.

---

## 20. Horizontes estratégicos originais e mapeamento de gates

Os Gates 1–6 abaixo vieram da formulação estratégica original. Eles não são a fila
executável e não usam a mesma numeração dos gates técnicos atuais. Para execução,
prevalecem `ESCOPO_MVP_VERTICAL_E_GATES.md` e `PROXIMAS_TAREFAS_CODEX.md`.

| Horizonte original | Gate técnico atual | Regra de transição |
|---|---|---|
| Gate 1 — Fundação confiável | G0 + G1 | segurança integrada e fundação profissional documentada |
| Gate 2 — Fluxo principal | G2 + G3 | Home/shell e vertical; Agenda completa não faz parte deste corte |
| Gate 3 — Retenção | G4 | coortes, entrevistas e decisão baseada no piloto |
| Gate 4 — Diferenciação | G5 | módulos relacionais entram somente quando priorizados por evidência |
| Gate 5 — Colaboração e monetização | futuro sem gate executivo atual | exige autorização, operação LGPD e decisão comercial próprias |
| Gate 6 — IA | G6 | exige valor comprovado sem IA e threat model específico |

### Horizonte original Gate 1 — Fundação confiável

Requisitos:

- autenticação;
- isolamento;
- biblioteca de campanhas;
- segurança baseline;
- documentação;
- exportação mínima planejada.

### Horizonte original Gate 2 — Fluxo principal

Requisitos:

- abrir campanha;
- workspace;
- sessão;
- agenda, na hipótese original; no plano atual somente data/hora simples entra em G3,
  enquanto Agenda completa permanece bloqueada até o gate opcional G4A e a validação de H5;
- continuidade inicial;
- instrumentação de ativação.

### Horizonte original Gate 3 — Retenção

Requisitos:

- uso de coortes;
- resumo;
- próxima sessão;
- histórico;
- retorno semanal;
- entrevistas com usuários ativos e inativos.

### Horizonte original Gate 4 — Diferenciação

Requisitos:

- NPCs;
- locais;
- facções;
- Entity Relations;
- Atlas Vivo funcional;
- timeline;
- journals.

### Horizonte original Gate 5 — Colaboração e monetização

Requisitos:

- jogadores;
- visibilidade;
- convites;
- assinatura;
- limites;
- suporte;
- política de dados.

### Horizonte original Gate 6 — IA

Requisitos:

- dados estruturados;
- permissões;
- auditoria;
- qualidade;
- aprovação do mestre;
- custo mensurável;
- valor comprovado sem IA.

---

## 21. Riscos estratégicos

| Risco | Impacto | Mitigação |
|---|---|---|
| Produto amplo demais | Alto | fases, gates e núcleo operacional |
| Complexidade de onboarding | Alto | progressive disclosure e templates |
| Baixa frequência de uso | Alto | medir por ciclo de campanha |
| Migração difícil | Alto | importação e exportação |
| Concorrência madura | Médio/alto | foco em integração e português |
| Atlas Vivo sem utilidade | Médio | validar tarefas antes de animação |
| Agenda secundária | Médio | testar com mestres multicampanha |
| IA elevar custos | Alto | franquia, aprovação e fase posterior |
| Dados sensíveis | Alto | privacy by design e visibilidade no backend |
| Dependência de serviços externos | Médio | arquitetura modular e exportação |
| Abandono de campanhas | Natural | métricas por formato e arquivamento |

---

## 22. Diretrizes de análise de dados

### 22.1 Unidade de análise

Separar:

- usuário;
- mestre;
- campanha;
- sessão;
- evento;
- entidade;
- relação;
- assinatura.

### 22.2 Segmentação mínima

- plano;
- origem;
- formato de campanha;
- sistema;
- frequência de sessão;
- número de campanhas;
- usuário novo ou recorrente;
- campanha ativa ou arquivada.

### 22.3 Cuidados estatísticos

- não concluir com amostra muito pequena;
- apresentar intervalo e tamanho da amostra;
- separar correlação de causalidade;
- analisar coortes por data de ativação;
- excluir testes internos;
- evitar médias sem distribuição;
- usar mediana para tempos assimétricos;
- registrar mudanças de instrumentação;
- não comparar coortes incompatíveis.

### 22.4 Dashboard inicial

Painéis:

1. aquisição;
2. ativação;
3. retenção;
4. uso por módulo;
5. campanhas vivas;
6. confiabilidade técnica;
7. receita futura.

---

## 23. Decisões recomendadas

1. Manter mestres como ICP e pagadores principais.
2. Tratar jogadores como participantes gratuitos no fluxo básico.
3. Validar problema antes de ampliar o escopo.
4. Concluir workspace e sessões antes de Atlas Vivo.
5. Construir Atlas Vivo sobre entidades reais e relações persistidas.
6. Separar agenda real de timeline fictícia.
7. Manter IA fora do núcleo até retenção comprovada.
8. Instrumentar eventos antes do beta aberto.
9. Garantir exportação e confiança de dados.
10. Usar monetização freemium como hipótese principal.
11. Testar preços antes de publicar planos definitivos.
12. Avaliar sucesso por continuidade da campanha, não por tempo de tela.

---

## 24. Próximas ações

### Produto

- executar 20 entrevistas;
- organizar roteiro;
- classificar dores;
- priorizar jobs;
- testar proposta;
- recrutar beta.

### Engenharia

- concluir segurança baseline;
- implementar Home real e workspace contextual da campanha;
- criar o vertical sessão → cena → acontecimento → recap → pendência;
- instrumentar somente os eventos v0 permitidos;
- manter Agenda completa bloqueada até G4A/H5;
- planejar exportação para G6 sem antecipar sua implementação;
- manter checkpoints.

### Dados

- criar dicionário de eventos;
- definir IDs e propriedades;
- separar ambientes;
- criar consulta de MCS e CVS;
- preparar coortes;
- documentar qualidade.

### Negócio

- criar landing page;
- testar mensagem;
- testar faixas de preço;
- organizar canais;
- registrar leads;
- medir origem e ativação.

---

## 25. Adendo de escopo do MVP vertical v0

Este adendo prevalece sobre listas anteriores de módulos para o primeiro ciclo de
validação. O produto deve provar um fluxo completo antes de ampliar a quantidade
de cadastros.

### 25.1 Fluxo de valor inicial

```text
campanha → sessão → cenas ordenadas → acontecimentos → recap → pendências
```

Entidades propostas:

- `Session`: preparação, agendamento simples, realização e encerramento;
- `Scene`: unidade ordenada dentro da sessão;
- `SessionOccurrence`: fato registrado na sessão e opcionalmente ligado a uma cena;
- `SessionRecap`: síntese canônica, única por sessão e aprovada pelo mestre;
- `PendingItem`: questão aberta da campanha, opcionalmente originada por sessão ou acontecimento.

O nome `SessionOccurrence` evita conflito com futuros eventos históricos, políticos
ou de calendário.

### 25.2 Não objetivos do primeiro vertical

- não substituir VTT, videoconferência ou sistema de regras;
- não implementar personagens, locais, facções, relações ou Atlas Vivo antes do piloto;
- não implementar calendário completo, indisponibilidades ou prevenção de conflitos;
- não implementar colaboração de jogadores ou permissões avançadas;
- não implementar upload, ingestão de documentos, PDF ou IA;
- não publicar planos e preços como definitivos;
- não usar tempo de tela como sinal principal de valor;
- não armazenar conteúdo narrativo integral em analytics.

### 25.3 Ativação e continuidade v0

Ativação do vertical:

> Campanha criada, primeira sessão criada, ao menos uma cena preparada e ao menos um
> acontecimento registrado em até sete dias.

Funil inicial versionado, com etapas obrigatórias e ordenadas:

1. `campaign_created`;
2. `session_created`;
3. `scene_created`;
4. `session_occurrence_created`;
5. `session_recap_approved`;
6. `pending_item_created`;
7. `session_completed`.

`pending_item_resolved` é uma ação posterior de continuidade e retenção, não substitui a
criação da pendência no funil de ativação.

A MCS permanece como North Star futura. Durante o piloto, a métrica de aprendizado é
o percentual de mestres que conclui o fluxo até recap e retorna para preparar ou
registrar a sessão seguinte.

### 25.4 Agenda e expansão

O vertical v0 inclui somente data/hora opcional, fuso e estado da sessão. Calendário
completo, lembretes, indisponibilidades, drag-and-drop e prevenção de conflitos formam
o gate opcional G4A, executável somente depois de G3, da decisão de G4 e da validação da
hipótese H5.

Personagens, locais, facções, relações, documentos, PDF e IA permanecem bloqueados
até o piloto com mestres reais produzir decisão explícita de avançar.

---

## 26. Referências

[^scribesblade]: Destrola. **ScribesBlade**. Disponível em: https://www.destrola.com/scribesblade. Acesso em 18/07/2026.

[^kanka-features]: Kanka. **Worldbuilding Tool Features: Maps, Timelines & More**. Disponível em: https://kanka.io/features. Acesso em 18/07/2026.

[^kanka-pricing]: Kanka. **Plans & Pricing**. Disponível em: https://kanka.io/pricing. Acesso em 18/07/2026.

[^worldanvil-home]: World Anvil. **Worldbuilding tools & RPG Campaign Manager**. Disponível em: https://www.worldanvil.com/. Acesso em 18/07/2026.

[^worldanvil-gm]: World Anvil. **World Anvil for Game Masters**. Disponível em: https://www.worldanvil.com/learn/workflows/gm-workflow. Acesso em 18/07/2026.

[^worldanvil-chronicles]: World Anvil. **Feature Guide to Chronicles**. Disponível em: https://www.worldanvil.com/learn/chronicles/chronicles. Acesso em 18/07/2026.

[^worldanvil-pricing]: World Anvil. **Guild Membership Pricing**. Disponível em: https://www.worldanvil.com/pricing. Acesso em 18/07/2026.

[^legendkeeper-home]: LegendKeeper. **Worldbuilding and RPG Campaign Management**. Disponível em: https://www.legendkeeper.com/. Acesso em 18/07/2026.

[^legendkeeper-pricing]: LegendKeeper. **Simple Pricing**. Disponível em: https://www.legendkeeper.com/pricing. Acesso em 18/07/2026.

[^legendkeeper-features]: LegendKeeper. **Imagine Huge Worlds**. Disponível em: https://www.legendkeeper.com/features-worldbuilding/. Acesso em 18/07/2026.

[^jtbd]: Christensen Institute. **Jobs to Be Done Theory**. Disponível em: https://www.christenseninstitute.org/theory/jobs-to-be-done/. Acesso em 18/07/2026.

[^heart]: Google Research. Rodden, K.; Hutchinson, H.; Fu, X. **Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications**. CHI 2010. Disponível em: https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/. Acesso em 18/07/2026.

[^north-star]: Amplitude. **What Makes a Good vs Bad North Star Metric**. Disponível em: https://amplitude.com/blog/good-bad-north-star-metric. Acesso em 18/07/2026.

[^reactflow-edges]: React Flow. **Animating Edges**. Disponível em: https://reactflow.dev/examples/edges/animating-edges. Acesso em 18/07/2026.

[^reactflow-accessibility]: React Flow. **Accessibility**. Disponível em: https://reactflow.dev/learn/advanced-use/accessibility. Acesso em 18/07/2026.

[^fullcalendar-react]: FullCalendar. **React Component**. Disponível em: https://fullcalendar.io/docs/react. Acesso em 18/07/2026.

[^fullcalendar-docs]: FullCalendar. **Documentation**. Disponível em: https://fullcalendar.io/docs. Acesso em 18/07/2026.

[^motion]: Motion. **Motion for React**. Disponível em: https://motion.dev/docs/react. Acesso em 18/07/2026.

[^motion-reduced]: Motion. **useReducedMotion**. Disponível em: https://motion.dev/docs/react-use-reduced-motion. Acesso em 18/07/2026.

[^tanstack]: TanStack. **TanStack Query Overview**. Disponível em: https://tanstack.com/query/latest/docs/framework/react/overview. Acesso em 18/07/2026.
