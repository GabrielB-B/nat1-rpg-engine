# Escopo do MVP Vertical e Gates

- Projeto: Nat 1 RPG Engine
- Versão: 1.0
- Data: 2026-07-18
- Status: canônico para continuidade do MVP

## Objetivo

Entregar e validar um ciclo narrativo completo para mestres de RPG antes de ampliar
o produto horizontalmente.

```text
campanha → sessão → cenas → acontecimentos → recap → pendências
```

O valor do MVP não será medido pela quantidade de módulos, mas pela capacidade de o
mestre preparar uma sessão, registrar o que ocorreu, encerrar o encontro e retomar a
continuidade na sessão seguinte.

## Gates obrigatórios

| Gate | Resultado esperado | Condição de saída |
| --- | --- | --- |
| G0 — Segurança e integração | Branch baseline tecnicamente confiável | PostgreSQL real descartável, migration `up/down/up`, testes, lint, builds, auditorias configuradas, revisão e integração aprovada |
| G1 — Fundação profissional | Decisões de produto, engenharia e identidade visual sem ambiguidade | Estratégia canônica, não objetivos, C4/deployment, ameaças/LGPD e CI; especificação visual implementada como candidato rastreável; tokens semânticos, tipografia e acessibilidade validados; QA visual registrado e aprovação explícita de Gabriel |
| G2 — Entrada operacional | Produto deixa de apresentar dados fictícios | Home real, estados assíncronos e shell contextual de campanha |
| G3 — Vertical funcional | Um ciclo narrativo persiste de ponta a ponta | API, migration, autorização, UI e testes para o fluxo completo |
| G4 — Validação | Evidência com mestres reais | Entrevistas, piloto, métricas de ativação/sucesso e decisão `avançar`, `revisar` ou `parar` |
| G4A — Agenda opcional | Hipótese de agenda comprovada sem inflar o vertical | Executável somente após G3, decisão de G4 e validação de H5; permanece bloqueado caso contrário |
| G5 — Expansão relacional | Conteúdo conectado após valor comprovado | Personagens, locais, facções e relações priorizados por evidência |
| G6 — Conteúdo e assistência | Automação segura sobre uma base validada | Documentos, importação/exportação, PDF e IA com aprovação do mestre |

Nenhum gate posterior autoriza pular os anteriores. Entrevistas de problema podem
ocorrer em paralelo, mas novos módulos permanecem bloqueados até G4.

### Leitura operacional de G1

G1 é composto por quatro partes inseparáveis:

1. **especificação:** direção de marca, tipografia, tokens, contraste e regras de uso;
2. **implementação:** ativos candidatos versionados e aplicação por componentes/tokens;
3. **verificação:** testes técnicos e QA visual com evidências nos breakpoints e estados definidos;
4. **aprovação:** decisão explícita de Gabriel sobre a direção visual apresentada.

Documentação isolada não encerra G1. Da mesma forma, um SVG presente no repositório não
se torna automaticamente logo final. A saída do gate exige as quatro partes registradas.
Mesmo após a aprovação visual de G1, uso comercial da marca continua condicionado à
proveniência dos anexos, originalidade da reconstrução, licenças, pesquisa de similaridade
e pesquisa marcária descritas no sistema de marca.

## Entidades do vertical

### Session

- pertence a um `GameProject`;
- possui título, número opcional, objetivo, notas de preparação, data/hora opcional,
  fuso, estado e timestamps;
- estados iniciais: `draft`, `scheduled`, `in_progress`, `completed`, `cancelled`;
- somente uma sessão `in_progress` por campanha na primeira versão;
- conclusão exige recap aprovado e revisão explícita das pendências da sessão;
- reabertura exige confirmação e segue a política de recap definida abaixo.

### Scene

- pertence obrigatoriamente a uma sessão;
- possui título, objetivo, notas e posição inteira;
- posições são únicas entre cenas ativas da sessão; cenas arquivadas não bloqueiam uma
  nova posição;
- reordenação deve ser transacional;
- arquivamento lógico preserva histórico e referências.

### SessionOccurrence

- pertence a uma sessão e pode apontar para uma cena;
- registra um acontecimento concreto, sua ordem, impacto e horário opcional;
- não se chama `Event` para não colidir com calendário ou timeline futura;
- pode originar uma pendência.

### SessionRecap

- relação um-para-um com a sessão;
- contém resumo, decisões, consequências e estado `draft` ou `approved`;
- aprovação é ação explícita do mestre;
- aprovação registra autor e data;
- reabrir sessão com recap aprovado exige antes reabrir o recap por ação explícita, que
  retorna seu estado a `draft` e registra a invalidação da aprovação;
- nenhuma reabertura apaga o conteúdo anterior ou seus timestamps de auditoria;
- uma futura IA poderá sugerir conteúdo, mas nunca aprová-lo.

### PendingItem

- pertence à campanha;
- pode referenciar sessão ou acontecimento de origem;
- possui descrição, estado, prioridade e data opcional;
- estados iniciais: `open`, `resolved`, `discarded`;
- resolução registra data e preserva a origem;
- `session_id` e `session_occurrence_id`, quando informados, devem pertencer ao mesmo
  `GameProject` do PendingItem; a constraint é validada pelo service e pelo banco quando
  tecnicamente aplicável.

## Regras de autorização

Na versão atual, todo recurso do vertical é acessível somente ao proprietário da
campanha. Toda query deve aplicar o escopo por `owner_user_id` por meio da campanha,
inclusive leitura, edição, reordenação, encerramento e restauração.

A autorização futura será orientada a membership de campanha, com decisão negada por
padrão. Nenhum papel futuro deve ser inferido apenas do frontend.

## Contratos de API previstos

Os caminhos definitivos serão registrados antes da implementação. A direção inicial é:

```text
GET    /game-projects/{project_id}/sessions
POST   /game-projects/{project_id}/sessions
GET    /game-projects/{project_id}/sessions/{session_id}
PATCH  /game-projects/{project_id}/sessions/{session_id}
POST   /game-projects/{project_id}/sessions/{session_id}/start
POST   /game-projects/{project_id}/sessions/{session_id}/cancel
POST   /game-projects/{project_id}/sessions/{session_id}/restore
POST   /game-projects/{project_id}/sessions/{session_id}/complete
POST   /game-projects/{project_id}/sessions/{session_id}/reopen

GET    /game-projects/{project_id}/sessions/{session_id}/scenes
POST   /game-projects/{project_id}/sessions/{session_id}/scenes
PATCH  /game-projects/{project_id}/sessions/{session_id}/scenes/{scene_id}
POST   /game-projects/{project_id}/sessions/{session_id}/scenes/{scene_id}/archive
POST   /game-projects/{project_id}/sessions/{session_id}/scenes/reorder

GET    /game-projects/{project_id}/sessions/{session_id}/occurrences
POST   /game-projects/{project_id}/sessions/{session_id}/occurrences
PATCH  /game-projects/{project_id}/sessions/{session_id}/occurrences/{occurrence_id}

PUT    /game-projects/{project_id}/sessions/{session_id}/recap
POST   /game-projects/{project_id}/sessions/{session_id}/recap/approve
POST   /game-projects/{project_id}/sessions/{session_id}/recap/reopen

GET    /game-projects/{project_id}/pending-items
POST   /game-projects/{project_id}/pending-items
PATCH  /game-projects/{project_id}/pending-items/{pending_item_id}
```

IDs filhos nunca substituem a validação do `project_id` e do usuário autenticado.

## Experiência do usuário

### Home real

- saudação baseada no usuário autenticado;
- campanhas ativas reais;
- próxima sessão somente quando houver dado persistido;
- CTA para criar ou abrir campanha;
- nenhum NPC, mapa, nota ou sessão fictícia;
- loading, erro recuperável, vazio orientado e sucesso.

### Shell da campanha

- contexto persistente de nome, estado e tema da campanha;
- navegação inicial restrita a `Resumo` e `Sessões`;
- módulos futuros não aparecem como controles habilitados;
- breadcrumbs e URLs profundas preservam contexto;
- tema da campanha é aplicado no shell e restaurado ao sair.

### Workspace da sessão

- cenas são o índice lateral ou superior do workspace, não um módulo global separado;
- acontecimentos, recap e pendências pertencem ao mesmo fluxo operacional;
- autosave só será adotado com indicador de estado, retry e proteção contra conflito;
- ações destrutivas exigem confirmação ou desfazer;
- teclado, foco visível, redução de movimento e layout móvel são critérios de aceite.

## Instrumentação v0

Eventos permitidos:

- `campaign_created`;
- `campaign_opened`;
- `session_created`;
- `scene_created`;
- `session_occurrence_created`;
- `session_recap_approved`;
- `pending_item_created`;
- `pending_item_resolved`;
- `session_completed`.

Propriedades não podem conter conteúdo narrativo, e-mail aberto, token, nomes reais,
documentos ou segredos da campanha. O catálogo deve ser versionado antes do beta.

## Critérios de aceite do vertical

- migrations aplicam e revertem em PostgreSQL descartável;
- usuário A não acessa nenhum recurso da campanha do usuário B;
- mestre cria sessão, ordena cenas e registra acontecimentos;
- mestre aprova recap, revisa pendências e conclui a sessão;
- recarregar a página preserva todo o estado persistido;
- UI cobre loading, erro, vazio, sucesso e perda de conexão;
- testes backend cobrem domínio e IDOR;
- testes frontend cobrem rotas, formulários e estados críticos;
- CI executa banco, migration, backend, lint, testes, build e auditorias;
- telemetria não coleta conteúdo privado.

## Não objetivos

- VTT, rolagem de dados, fichas ou motor de regras;
- calendário completo e prevenção de conflitos;
- personagens, locais, facções, relações e Atlas Vivo;
- área de jogadores, convites e colaboração;
- uploads, documentos, PDF, RAG ou IA;
- publicação pública e monetização definitiva;
- customização visual avançada além dos temas já aprovados.

## Gate de validação com mestres

O piloto deve observar mestres executando tarefas com campanhas reais. Métricas mínimas:

- taxa de criação da primeira sessão;
- tempo até primeira cena ou acontecimento;
- percentual que conclui recap;
- percentual que registra ou resolve pendência;
- sucesso de retomada de contexto na sessão seguinte;
- retorno W1 e W4 por frequência da campanha;
- erros, pedidos de ajuda e abandono por etapa.

A expansão só ocorre após decisão documentada. Feedback favorável sem comportamento
observável não é evidência suficiente.
