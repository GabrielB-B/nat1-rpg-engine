# Modulos Do Sistema

Projeto: Nat 1 RPG Engine

Data de referencia: 2026-06-21

Fase relacionada: `docs/architecture-roadmap-checkpoints`

## Objetivo

Mapear módulos atuais e planejados do Nat 1 RPG Engine, registrando status, objetivo, dependências, dados principais, riscos e próxima etapa.

## Modulos Atuais

| Módulo | Status | Objetivo | Dependências | Dados principais | Riscos | Próxima etapa |
| --- | --- | --- | --- | --- | --- | --- |
| Auth | Implementado | Permitir cadastro, login, usuário atual e proteção básica de rotas. | `User`, JWT, bcrypt, API client. | Nome, e-mail, senha em hash, token de acesso. | Estratégia de token ainda simples para produção. | Avaliar refresh token e política de sessão em fase de segurança. |
| GameProjects / Campanhas & Crônicas | Implementado | Gerenciar a unidade principal de trabalho do mestre. | Auth, `World`, `SystemTemplate`, `ProjectModuleSetting`. | Nome, slug, formato, descrição, status, tema, capa, vínculos opcionais. | Ainda sem edição/restauração visual e sem shell interna. | Criar Home com dados reais e depois dashboard interno da campanha. |
| Worlds | Implementado no backend | Registrar mundos ou cenários reutilizáveis. | Auth e isolamento por usuário. | Nome, descrição, status de arquivamento. | Sem interface dedicada e sem artigos internos de worldbuilding. | Criar experiência visual quando o workspace de campanha exigir seleção e manutenção. |
| SystemTemplates | Implementado no backend | Registrar sistemas, templates ou estruturas de regras. | Auth e templates internos do produto. | Nome, tipo, escopo built-in/custom, status de arquivamento. | Sem modelagem avançada de campos de sistema. | Expandir quando módulos internos exigirem regras e fichas parametrizadas. |
| ProjectModuleSettings | Implementado no backend | Controlar módulos ativos e ordenação por campanha. | `GameProject`. | Chave, nome exibido, ícone, ativo/inativo, ordem. | Ainda sem UI para configuração. | Usar na shell interna da campanha para montar navegação modular. |
| Home do Mestre | Implementado como shell mockada | Apresentar visão inicial do mestre. | Design system e dados mockados. | Estatísticas, campanha ativa, sessões, NPCs, mapa e notas em mock. | Ainda não reflete dados reais da conta. | Executar `front/home-master-real-data`. |
| Design System | Implementado como fundação | Definir tokens, layout, componentes e tema inicial. | Tailwind CSS, CSS variables, lucide-react. | Tema `cartographer`, componentes de layout, cards e botões. | Temas alternativos ainda não possuem telas completas. | Consolidar padrões conforme novas telas reais surgirem. |
| API Integration | Implementado como fundação | Padronizar chamadas HTTP protegidas no frontend. | API client, auth storage, TanStack Query. | Token, erros padronizados, query keys, hooks de domínio. | Sem interceptors avançados ou retry específico por domínio. | Reutilizar em Home real e dashboard de campanha. |
| Documentação de controle | Implementado e em expansão | Manter histórico, status, roadmap, checkpoints e padrões. | Docs versionados no repositório. | Status atual, próximas tarefas, histórico, decisões, arquitetura. | Risco de desatualização se fases futuras não atualizarem checkpoints. | Aplicar padrão obrigatório para próximas fases. |

## Modulos Planejados

| Módulo | Status | Objetivo | Dependências | Dados principais | Riscos | Próxima etapa |
| --- | --- | --- | --- | --- | --- | --- |
| Master Home Real Data | Pendente | Conectar a Home do Mestre aos dados reais disponíveis. | Auth, GameProjects, API Integration. | Campanhas recentes, contadores básicos, estados vazios. | Pode expor lacunas de dados ainda não modelados. | Executar `front/home-master-real-data`. |
| Campaign Workspace | Pendente | Criar entrada interna da campanha com contexto ativo. | GameProject Summary, ProjectModuleSettings. | Campanha ativa, módulos, contadores, atalhos. | Navegação pode ficar rasa sem módulos reais. | Executar `front/game-project-dashboard-shell`. |
| GameProject Metadata | Pendente | Expandir metadados de campanha. | GameProject, Worlds, SystemTemplates. | Gênero, tom, tags, capa, resumo, estado editorial. | Campos podem ficar genéricos sem regras claras. | Definir schema antes de nova UI de edição. |
| Sessions | Pendente | Registrar sessões reais da campanha. | GameProject, calendário real, participantes futuros. | Título, data/hora real, pauta, resumo, status. | Misturar agenda real com calendário fictício. | Criar `back/session-scene-foundation`. |
| Scenes | Pendente | Organizar cenas dentro de sessões ou campanha. | Sessions, GameProject. | Título, ordem, objetivo, notas, estado. | Excesso de granularidade no MVP. | Modelar junto de Sessions. |
| Calendar Scheduling | Pendente | Agendar próximas sessões no calendário real do mestre. | Sessions, fuso horário, notificações futuras. | Data real, hora, duração, status. | Confusão com calendário fictício do mundo. | Manter separado de timelines e calendários de lore. |
| Characters & Creatures | Pendente | Registrar personagens, NPCs e criaturas. | GameProject, World, relações. | Nome, tipo, descrição, tags, vínculos. | Pode exigir templates por sistema cedo demais. | Começar com modelo simples e expansível. |
| Locations / Atlas | Pendente | Organizar locais, regiões e pontos de interesse. | GameProject, World, Maps futuro. | Nome, tipo, descrição, hierarquia, vínculos. | Hierarquia complexa antes do uso real. | Implementar depois de workspace interno. |
| Organizations & Factions | Pendente | Registrar facções, instituições e grupos. | GameProject, World, relações. | Nome, tipo, objetivos, relações. | Relações sem modelo claro podem virar texto solto. | Projetar junto de Relationships. |
| Notes | Pendente | Registrar notas rápidas e anotações de campanha. | GameProject, usuário, tags. | Título, conteúdo, contexto, vínculos. | Duplicar documentos/artigos se não houver limite claro. | Definir diferença entre nota, documento e artigo. |
| Documents | Pendente | Guardar handouts, documentos e materiais de lore. | GameProject, Upload futuro. | Título, conteúdo, tipo, anexos futuros. | Upload e segurança de arquivos exigem fase própria. | Criar fundação sem upload binário inicialmente. |
| Maps | Pendente | Registrar mapas e vínculos com locais. | Locations, upload futuro. | Nome, imagem, pins futuros, camadas futuras. | Mapas interativos podem expandir escopo rapidamente. | Planejar depois de Locations. |
| Relationships | Pendente | Modelar vínculos entre entidades do mundo e campanha. | Personagens, locais, facções, documentos, notas. | Origem, destino, tipo, descrição. | Grafo visual sem valor operacional. | Começar por relações simples e consultáveis. |
| Players | Pendente | Gerenciar participantes da campanha. | Auth, convites, permissões. | Usuário, papel, status, permissões. | Implica LGPD, convites e autorização fina. | Executar após workspace de campanha estabilizado. |
| Invitations / RSVP | Pendente | Convidar jogadores e registrar presença. | Players, Sessions, e-mail futuro. | Convite, aceite, presença, status. | Fluxos externos e abuso de convite. | Planejar depois de Players. |
| Security Audit | Pendente | Revisar segurança antes de exposição pública. | Auth, API, frontend storage, logs. | CORS, token, rate limit, headers, validações. | Publicar sem hardening mínimo. | Executar fase dedicada antes de deploy público. |
| RAG / AI Assistant | Pendente futuro | Auxiliar criação, resumo e organização de conteúdo. | Upload, documentos, aprovação do mestre, segurança. | Sugestões, classificações, resumos, pendências de aprovação. | IA alterar conteúdo canônico sem revisão humana. | Iniciar somente após módulos e ingestão de documentos. |

## Regras Transversais

- A campanha é o contêiner operacional dos módulos internos.
- Mundo e sistema devem continuar separados da campanha.
- Módulos internos devem ser ativáveis por campanha.
- Arquivamento deve ser preferido a exclusão permanente.
- Conteúdo sugerido por IA não deve virar dado oficial sem aprovação explícita do mestre.
- Dados pessoais devem ser limitados ao necessário e tratados conforme política de privacidade futura.
- Relações entre entidades devem ter utilidade operacional antes de receber visualização gráfica.

