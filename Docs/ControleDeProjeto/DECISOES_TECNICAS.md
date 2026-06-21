# Decisoes Tecnicas

Projeto: Nat 1 RPG Engine

Data de referencia: 2026-06-21

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

## DT-005 - Autenticacao Com JWT E bcrypt

- Status: adotada.
- Contexto: o MVP precisa de autenticação local funcional e protegida.
- Decisão: usar JWT Bearer token para sessão e bcrypt para hash de senha.
- Consequência: rotas privadas devem depender do usuário atual e nunca retornar `password_hash`.

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

