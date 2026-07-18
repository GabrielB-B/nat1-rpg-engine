# Modulos Do Sistema

Projeto: Nat 1 RPG Engine

Data de referencia original: 2026-06-21

Última atualização: 2026-07-18

Fase relacionada: `docs/architecture-roadmap-checkpoints`

Atualização de direção: o corte executável está em
`ESCOPO_MVP_VERTICAL_E_GATES.md`. Módulos posteriores continuam neste mapa apenas para
arquitetura futura e não pertencem automaticamente ao MVP.

## Objetivo

Mapear módulos atuais e planejados do Nat 1 RPG Engine, registrando status, objetivo, dependências, dados principais, riscos e próxima etapa.

## Modulos Atuais

| Módulo | Status | Objetivo | Dependências | Dados principais | Riscos | Próxima etapa |
| --- | --- | --- | --- | --- | --- | --- |
| Auth | Implementado | Permitir cadastro, login, usuário atual e proteção básica de rotas. | `User`, JWT, bcrypt, API client. | Nome, e-mail, senha em hash, token de acesso. | Estratégia de token ainda simples para produção. | Avaliar refresh token e política de sessão em fase de segurança. |
| GameProjects / Campanhas & Crônicas | Implementado | Gerenciar a unidade principal de trabalho do mestre. | Auth, `World`, `SystemTemplate`, `ProjectModuleSetting`. | Nome, slug, formato, descrição, status, tema, capa, vínculos opcionais. | Ainda sem edição/restauração visual e sem shell interna. | Após G0, criar Home real e shell contextual em branches próprias. |
| Worlds | Implementado no backend | Registrar mundos ou cenários reutilizáveis. | Auth e isolamento por usuário. | Nome, descrição, status de arquivamento. | Sem interface dedicada e sem artigos internos de worldbuilding. | Criar experiência visual quando o workspace de campanha exigir seleção e manutenção. |
| SystemTemplates | Implementado no backend | Registrar sistemas, templates ou estruturas de regras. | Auth e templates internos do produto. | Nome, tipo, escopo built-in/custom, status de arquivamento. | Sem modelagem avançada de campos de sistema. | Expandir quando módulos internos exigirem regras e fichas parametrizadas. |
| ProjectModuleSettings | Implementado no backend | Controlar módulos ativos e ordenação por campanha. | `GameProject`. | Chave, nome exibido, ícone, ativo/inativo, ordem. | O padrão atual habilita módulos ainda inexistentes. | Restringir o default ao vertical antes da shell contextual. |
| Home do Mestre | Implementado como protótipo mockado | Validar direção visual inicial. | Design system e dados mockados. | Estatísticas, campanha, sessões, NPCs, mapa e notas fictícias. | Pode induzir o usuário a acreditar que dados inexistentes são reais. | Substituir por Home real em G2; remover controles e módulos falsos. |
| Design System | Implementado como fundação | Definir tokens, layout, componentes e tema inicial. | Tailwind CSS, CSS variables, lucide-react. | Tema `cartographer`, componentes de layout, cards e botões. | Temas alternativos ainda não possuem telas completas. | Consolidar padrões conforme novas telas reais surgirem. |
| API Integration | Implementado como fundação | Padronizar chamadas HTTP protegidas no frontend. | API client, auth storage, TanStack Query. | Token, erros padronizados, query keys, hooks de domínio. | Sem interceptors avançados ou retry específico por domínio. | Reutilizar em Home real e dashboard de campanha. |
| Documentação de controle | Implementado e em expansão | Manter histórico, status, roadmap, checkpoints e padrões. | Docs versionados no repositório. | Status atual, próximas tarefas, histórico, decisões, arquitetura. | Risco de desatualização se fases futuras não atualizarem checkpoints. | Aplicar padrão obrigatório para próximas fases. |

## Modulos Planejados

| Módulo | Status | Objetivo | Dependências | Dados principais | Riscos | Próxima etapa |
| --- | --- | --- | --- | --- | --- | --- |
| Master Home Real Data | Pendente | Conectar a Home do Mestre aos dados reais disponíveis. | Auth, GameProjects, API Integration. | Campanhas recentes, contadores básicos, estados vazios. | Pode expor lacunas de dados ainda não modelados. | Executar `front/home-master-real-data`. |
| Campaign Workspace | Pendente | Criar entrada interna da campanha com contexto ativo. | GameProject Summary, ProjectModuleSettings. | Campanha ativa, módulos, contadores, atalhos. | Navegação pode ficar rasa sem módulos reais. | Executar `front/game-project-dashboard-shell`. |
| GameProject Metadata | Pendente | Expandir metadados de campanha. | GameProject, Worlds, SystemTemplates. | Gênero, tom, tags, capa, resumo, estado editorial. | Campos podem ficar genéricos sem regras claras. | Definir schema antes de nova UI de edição. |
| Sessions | Pendente — G3 | Registrar preparação, realização e encerramento de sessões. | GameProject e autorização. | Título, objetivo, data/hora opcional, fuso, notas e estado. | Misturar agenda real com calendário fictício. | Implementar como raiz do vertical. |
| Scenes | Pendente — G3 | Organizar cenas ordenadas dentro da sessão. | Session e autorização herdada da campanha. | Título, ordem, objetivo, notas e estado. | Reordenação inconsistente. | Implementar no workspace da sessão, não como navegação global. |
| Session Occurrences | Pendente — G3 | Registrar acontecimentos concretos da sessão. | Session e Scene opcional. | Ordem, descrição, impacto e origem. | Colisão conceitual com eventos de calendário/timeline. | Usar `SessionOccurrence`, não `Event`. |
| Session Recap | Pendente — G3 | Consolidar a memória canônica ao fim da sessão. | Session. | Resumo, decisões, consequências e aprovação. | Conteúdo futuro de IA virar canônico sem revisão. | Um recap por sessão, aprovado explicitamente pelo mestre. |
| Pending Items | Pendente — G3 | Manter questões e consequências abertas entre sessões. | GameProject, Session/Occurrence opcionais. | Descrição, prioridade, estado, origem e resolução. | Virar lista genérica sem vínculo narrativo. | Integrar ao fechamento e retomada da sessão. |
| Calendar Scheduling | Bloqueado — G4A opcional | Evoluir data/hora de sessão para agenda completa. | Sessions reais, fuso horário, notificações futuras e H5 validada. | Indisponibilidade, duração, conflito e lembrete. | Hipótese de valor ainda não validada. | Avaliar somente após G4; não antecede o vertical. |
| Characters & Creatures | Bloqueado — pós-G4 | Registrar personagens, NPCs e criaturas. | GameProject, World, relações e evidência do piloto. | Nome, tipo, descrição, tags, vínculos. | Pode exigir templates por sistema cedo demais. | Priorizar em G5 somente se a evidência justificar. |
| Locations / Atlas | Bloqueado — pós-G4 | Organizar locais, regiões e pontos de interesse. | GameProject, World, Maps futuro e evidência do piloto. | Nome, tipo, descrição, hierarquia, vínculos. | Hierarquia complexa antes do uso real. | Priorizar em G5 somente se a evidência justificar. |
| Organizations & Factions | Bloqueado — pós-G4 | Registrar facções, instituições e grupos. | GameProject, World, relações e evidência do piloto. | Nome, tipo, objetivos, relações. | Relações sem modelo claro podem virar texto solto. | Priorizar em G5 somente se a evidência justificar. |
| Notes | Futuro sem gate executivo | Registrar notas rápidas e anotações de campanha. | GameProject, usuário, tags e fronteira definida com PendingItem/Document. | Título, conteúdo, contexto, vínculos. | Duplicar recap, pendência ou documento. | Não implementar até existir hipótese e gate próprios. |
| Documents | Bloqueado — G6 | Guardar handouts, documentos e materiais de lore. | GameProject, armazenamento e política de arquivos. | Título, conteúdo, tipo, anexos futuros. | Upload e segurança de arquivos exigem fase própria. | Avaliar em G6, após validação e threat model específico. |
| Maps | Futuro sem gate executivo | Registrar mapas e vínculos com locais. | Locations e armazenamento futuro. | Nome, imagem, pins futuros, camadas futuras. | Mapas interativos podem expandir escopo rapidamente. | Não implementar até existir hipótese e gate próprios. |
| Relationships | Bloqueado — pós-G4 | Modelar vínculos entre entidades do mundo e campanha. | Personagens, locais, facções e evidência do piloto. | Origem, destino, tipo, descrição. | Grafo visual sem valor operacional. | Priorizar em G5 somente se a evidência justificar. |
| Players | Futuro sem gate executivo | Gerenciar participantes da campanha. | Auth, convites, permissões e operação LGPD. | Usuário, papel, status, permissões. | Implica LGPD, convites e autorização fina. | Exige decisão própria após estabilização do workspace. |
| Invitations / RSVP | Futuro sem gate executivo | Convidar jogadores e registrar presença. | Players, Sessions e e-mail futuro. | Convite, aceite, presença, status. | Fluxos externos e abuso de convite. | Não implementar antes de Players e threat model específico. |
| Security Baseline | Em revisão para integração | Validar isolamento, configuração, dependências, PostgreSQL e CI. | Auth, API, frontend, Alembic e PostgreSQL. | Branch ainda sem commit/PR integrado. | Integrar G0 somente após aprovação e CI verde. |
| Public Auth/Session Hardening | Pendente antes de produção | Evoluir sessão e resistência a abuso. | Baseline integrada e deployment definido. | Cookie/refresh, revogação, rate limit, CORS e observabilidade. | Exposição pública prematura. | Executar antes de qualquer beta público. |
| RAG / AI Assistant | Pendente futuro | Auxiliar criação, resumo e organização de conteúdo. | Upload, documentos, aprovação do mestre, segurança. | Sugestões, classificações, resumos, pendências de aprovação. | IA alterar conteúdo canônico sem revisão humana. | Iniciar somente após módulos e ingestão de documentos. |

## Regras Transversais

- A campanha é o contêiner operacional dos módulos internos.
- Mundo e sistema devem continuar separados da campanha.
- Módulos internos devem ser ativáveis por campanha.
- Arquivamento deve ser preferido a exclusão permanente.
- Conteúdo sugerido por IA não deve virar dado oficial sem aprovação explícita do mestre.
- Dados pessoais devem ser limitados ao necessário e tratados por privacy by design desde agora, conforme `MODELO_DE_AMEACAS_AUTORIZACAO_E_LGPD.md`.
- Relações entre entidades devem ter utilidade operacional antes de receber visualização gráfica.

