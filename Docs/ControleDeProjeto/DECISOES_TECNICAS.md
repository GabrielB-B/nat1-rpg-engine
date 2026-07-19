# Decisoes Tecnicas

Projeto: Nat 1 RPG Engine

Data de referencia original: 2026-06-21

Última atualização: 2026-07-18

Fase relacionada: `docs/architecture-roadmap-checkpoints`

## Objetivo

Registrar decisões técnicas já adotadas para reduzir ambiguidade em fases futuras.

## DT-001 - Backend Com FastAPI

- Status: adotada.
- Contexto: o projeto precisa de API HTTP tipada, documentação automática e boa ergonomia para testes.
- Decisão: usar FastAPI como framework backend.
- Consequência: endpoints ficam versionados em `app/api/v1`, com schemas Pydantic e documentação Swagger.

## DT-002 - PostgreSQL Como Banco Principal

- Status: adotada.
- Contexto: o produto depende de dados relacionais, isolamento por usuário e vínculos entre módulos.
- Decisão: usar PostgreSQL como banco principal.
- Consequência: relações, constraints e migrations devem ser tratadas como parte central da arquitetura.

## DT-003 - SQLAlchemy E Alembic

- Status: adotada.
- Contexto: o backend precisa de ORM e versionamento de schema.
- Decisão: usar SQLAlchemy para models e sessão, com Alembic para migrations.
- Consequência: alterações de model devem ser acompanhadas de migration quando afetarem o banco.

## DT-004 - Camadas De Endpoint, Service E Repository

- Status: adotada.
- Contexto: regras de negócio e acesso a dados não devem ficar acoplados às rotas.
- Decisão: endpoints recebem requisições, services aplicam regras e repositories acessam dados.
- Consequência: novas features devem seguir a separação de responsabilidades existente.

## DT-005 - Autenticação Com JWT E Hash De Senha Migrável

- Status: adotada; revisada em 2026-07-18.
- Contexto: o MVP precisa de autenticação local funcional sem aceitar o truncamento silencioso de 72 bytes do bcrypt direto.
- Decisão: usar JWT Bearer token e `bcrypt_sha256` como hash primário; manter `bcrypt` apenas para compatibilidade legada e rehash oportunístico após login válido. Senhas novas aceitam de 8 a 128 caracteres; uma tentativa legada acima de 72 bytes é recusada genericamente.
- Consequência: rotas privadas dependem do usuário atual, nunca retornam `password_hash` e contas legadas migram sem troca forçada de senha quando a credencial puder ser verificada com segurança; recuperação/reset permanece necessária para o caso legado recusado.

## DT-006 - Login OAuth2 Form No Backend

- Status: adotada.
- Contexto: Swagger Authorize e fluxo OAuth2PasswordRequestForm exigem `username` e `password`.
- Decisão: login usa `application/x-www-form-urlencoded`, com e-mail enviado no campo `username`.
- Consequência: frontend deve manter suporte a form-urlencoded no login.

## DT-007 - Frontend Com React, TypeScript E Vite

- Status: adotada.
- Contexto: o frontend precisa de base leve, tipada e adequada a evolução incremental.
- Decisão: usar React, TypeScript e Vite.
- Consequência: builds devem passar com `npm.cmd run build` antes de fechamento de fases frontend.

## DT-008 - TanStack Query Para Dados Assincronos

- Status: adotada.
- Contexto: telas protegidas consomem API com cache, loading, erro e invalidação.
- Decisão: usar TanStack Query para hooks de leitura e mutations.
- Consequência: features devem preferir hooks de domínio em vez de chamadas diretas dentro de páginas.

## DT-009 - Tema Cartographer Como Identidade Inicial

- Status: adotada.
- Contexto: o produto precisa de identidade própria alinhada à proposta de organização de campanhas.
- Decisão: usar `cartographer` como tema inicial.
- Consequência: novas telas devem preservar fundo pergaminho, hierarquia controlada, tons cartográficos e componentes consistentes.

## DT-010 - Temas Alternativos Planejados

- Status: planejada.
- Contexto: o produto prevê ambientações visuais diferentes sem quebrar componentes.
- Decisão: manter `dark_horror` e `humanist_futuristic` como chaves oficiais planejadas.
- Consequência: componentes devem consumir tokens e evitar cores fixas sem necessidade.

## DT-011 - Arquivamento Preferido A Exclusao Permanente

- Status: adotada.
- Contexto: campanhas e conteúdos de RPG têm valor histórico e podem ser recuperados.
- Decisão: arquivamento é o fluxo padrão para remoção da biblioteca principal.
- Consequência: exclusão permanente deve exigir escopo explícito, confirmação forte e fase própria.

## DT-012 - Campanha, Mundo E Sistema Separados

- Status: adotada.
- Contexto: campanhas podem compartilhar mundos ou sistemas diferentes.
- Decisão: `GameProject`, `World` e `SystemTemplate` são entidades separadas.
- Consequência: vínculos entre elas devem ser opcionais e controlados por usuário.

## DT-013 - Sessoes Como Entidade Propria

- Status: planejada.
- Contexto: próxima sessão não deve ser apenas texto solto na campanha.
- Decisão: sessões serão modeladas como entidade própria vinculada a `GameProject`.
- Consequência: Home real e cards podem exibir ausência de próxima sessão até o módulo existir.

## DT-014 - Calendario Real Separado De Calendario Ficticio

- Status: planejada.
- Contexto: agenda do mestre e calendário do mundo têm funções diferentes.
- Decisão: agendamento real de sessão deve ser separado de calendários e timelines ficcionais.
- Consequência: `Calendar Scheduling` e worldbuilding temporal devem evoluir em módulos distintos.

## DT-015 - IA/RAG Com Aprovacao Do Mestre

- Status: planejada para fase futura.
- Contexto: IA pode auxiliar criação, resumo e organização, mas não deve controlar cânone.
- Decisão: sugestões de IA devem exigir revisão e aprovação do mestre antes de persistir conteúdo oficial.
- Consequência: upload, indexação, revisão e trilha de aprovação precisam de fases próprias.

## DT-016 - Referencias De Produto Como Inspiracao, Nao Copia

- Status: adotada.
- Contexto: Kanka, World Anvil, LegendKeeper, Campfire, Notion, Obsidian e Roll20 orientam análise de produto.
- Decisão: referências são usadas para princípios de organização, não para cópia visual ou terminológica.
- Consequência: o Nat 1 mantém caminho próprio: Home do Mestre, Campanhas & Crônicas, módulos relacionais, mundo amplo, sistema separado e IA futura.

## DT-017 - Branch Por Fase

- Status: adotada.
- Contexto: o projeto evolui por entregas pequenas, revisáveis e documentadas.
- Decisão: cada fase relevante deve usar branch própria.
- Consequência: mudanças de escopo diferente devem evitar mistura no mesmo branch.

## DT-018 - Configuração De Segurança Fail-Closed

- Status: adotada.
- Contexto: inferir ambiente, banco ou secret pode transformar erro de deploy em configuração insegura ou conexão acidental ao banco local.
- Decisão: `ENVIRONMENT`, `DATABASE_URL` e `SECRET_KEY` são obrigatórios em qualquer execução. Fora de local/teste, o secret deve ter ao menos 32 caracteres e não pode ser placeholder; a URL com credenciais locais documentadas é recusada; CORS exige HTTPS e host não-loopback.
- Consequência: a API falha na inicialização quando a configuração está ausente ou inválida; deploys, testes e comandos locais precisam fornecer valores intencionais para ambiente, banco, origem e secret.

## DT-019 - URL De Capa Validada No Backend

- Status: adotada.
- Contexto: o frontend já bloqueia protocolos inseguros, mas payloads diretos contra a API também precisam ser validados.
- Decisão: aceitar `cover_image_url` apenas com protocolo `http` ou `https`.
- Consequência: URLs vazias são normalizadas para `None` e protocolos como `javascript:` retornam erro de validação.

## DT-020 - PostgreSQL E Migrations Como Gate De Integração

- Status: adotada.
- Contexto: testes SQLite com `create_all()` não provam compatibilidade do schema real.
- Decisão: toda mudança de model deve executar migration e smoke em PostgreSQL descartável; reversibilidade nunca usa o banco persistente local.
- Consequência: CI sobe PostgreSQL 16 e valida `upgrade`, `check`, integração, `downgrade` e novo `upgrade`.

## DT-021 - MVP Vertical De Continuidade

- Status: adotada.
- Contexto: o roadmap horizontal ampliava módulos antes de validar valor operacional.
- Decisão: o primeiro vertical é `Session`, `Scene`, `SessionOccurrence`, `SessionRecap` e `PendingItem`.
- Consequência: personagens, locais, facções, relações, documentos, PDF e IA ficam bloqueados até o piloto com mestres.

## DT-022 - Autorização Herdada Da Campanha

- Status: adotada como arquitetura.
- Contexto: recursos filhos não podem ser autorizados apenas por UUID ou por decisão do frontend.
- Decisão: toda ação valida usuário, campanha e pertencimento do recurso; o futuro modelo de membership usa deny-by-default e papéis por campanha.
- Consequência: repositories, services e testes IDOR devem cobrir leitura e cada mutação.

## DT-023 - Hierarquia Documental Única

- Status: adotada.
- Contexto: plano de produto, plano de trabalho, status e fila apontavam para próximas fases diferentes.
- Decisão: `STATUS_ATUAL.md` registra fatos e `PROXIMAS_TAREFAS_CODEX.md` é a única fila executável; documentos datados mais novos prevalecem sobre PDFs e roadmaps históricos.
- Consequência: checkpoints e histórico não governam prioridade e não podem declarar integração inexistente.

## DT-024 - Geometria De Marca Invariante Entre Temas

- Status: adotada como direção de construção; aprovação visual final pendente.
- Contexto: os dois logos anexos possuem atmosferas diferentes e poderiam fragmentar reconhecimento.
- Decisão: chapéu, d20, número 1 e anel cardeal preservam a mesma geometria; temas alteram paleta, textura e acabamento.
- Consequência: Cartógrafo usa a composição clara como base, Horror deriva o acabamento escuro e Futurista mantém o símbolo em linguagem geométrica. A implementação atual materializa uma hipótese candidata e não converte a marca em ativo final ou comercialmente liberado.

## DT-025 - JWT Simétrico Sem Dependência ECDSA

- Status: adotada.
- Contexto: `python-jose` trazia `ecdsa`, afetada por [CVE-2024-23342 / GHSA-wj6h-64fc-37mp](https://github.com/advisories/GHSA-wj6h-64fc-37mp) e sem versão corrigida; o Nat 1 usa exclusivamente `HS256`.
- Decisão: substituir `python-jose` por `PyJWT==2.13.0`, sem extra criptográfico, manter allowlist explícita de `HS256` e exigir claims `sub` e `exp` na decodificação.
- Consequência: `ecdsa`, `rsa` e `pyasn1` deixam o lock, a superfície de dependências diminui e uma futura adoção de algoritmo assimétrico exigirá nova decisão e threat review.

## DT-026 - Gate Visual Exige Especificação, Implementação, QA E Aprovação

- Status: adotada.
- Contexto: a definição resumida de G1 permitia interpretar a especificação documental como suficiente, enquanto a fila executável exigia ativos, contraste e QA visual.
- Decisão: G1 visual só pode ser encerrado quando especificação, implementação candidata rastreável, QA com evidências e aprovação explícita de Gabriel estiverem registrados.
- Consequência: `front/cartographer-brand-tokens` permanece em andamento enquanto houver QA ou decisão visual pendente; presença de SVGs ou tokens no repositório, isoladamente, não autoriza declarar marca final nem iniciar G2.

## DT-027 - Ornamentação E Limite Operacional Usam Contratos Distintos

- Status: adotada.
- Contexto: a borda dourada suave funcionava como decoração Cartógrafo, mas ficava abaixo de 3:1 quando reutilizada para identificar campos e botões contornados.
- Decisão: manter `--border-default` como divisão ornamental e exigir `--control-border` opaca para limites interativos, validada contra superfície e página nos três temas.
- Consequência: o produto preserva leveza visual sem sacrificar WCAG 1.4.11; novos controles não podem usar borda decorativa como único limite perceptível.
