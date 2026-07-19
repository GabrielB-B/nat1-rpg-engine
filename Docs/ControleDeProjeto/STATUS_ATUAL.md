# Status Atual

Projeto: Nat 1 RPG Engine

Data da última atualização: 2026-07-18

Fase atual: G1 em andamento — `front/cartographer-brand-tokens`

Branch de fechamento de G0: `security/baseline-hardening`

Status canônico em `main`: G0 concluído pela integração do PR #13

## Regra de leitura

- este arquivo registra fatos verificados do estado atual;
- `PROXIMAS_TAREFAS_CODEX.md` é a única fila executável;
- `CHECKPOINTS.md` e `HISTORICO_TECNICO.md` preservam histórico;
- PDFs v1 e roadmaps anteriores são subordinados aos adendos datados mais recentes;
- código planejado não é apresentado como implementado.

## Entregas da continuação de G0

### Segurança e backend

- preservadas as alterações anteriores de `.gitignore`, URL de capa e testes IDOR;
- `ENVIRONMENT`, `DATABASE_URL` e `SECRET_KEY` são obrigatórios; ausência ou configuração inválida interrompe a inicialização da API;
- a URL/credencial documentada do PostgreSQL local permanece alinhada ao Docker Compose, mas é recusada fora de local/teste;
- ambientes não locais exigem secret com ao menos 32 caracteres;
- CORS aceita HTTP somente em ambientes locais; fora deles exige HTTPS e host não-loopback;
- expiração de access token aceita somente intervalo positivo e limitado;
- métodos e headers CORS foram restringidos;
- middleware adiciona headers baseline de conteúdo, frame, referência e permissões;
- login com usuário inexistente executa verificação de hash dummy para reduzir enumeração temporal;
- novos hashes usam `bcrypt_sha256`, login válido migra bcrypt legado oportunisticamente e senhas novas aceitam até 128 caracteres;
- entrada acima de 128 caracteres ou bcrypt legado acima de 72 bytes recebe erro genérico; o segundo caso requer futuro reset de senha;
- dependências diretas Python foram fixadas;
- `requirements.lock` registra o ambiente reproduzível;
- `pydantic-settings` foi atualizado para `2.14.2` e Starlette para `1.3.1` após o primeiro `pip-audit` remoto identificar versões vulneráveis;
- `python-jose` foi substituída por `PyJWT==2.13.0` sem extra criptográfico: o projeto usa somente `HS256` e removeu `ecdsa` vulnerável e dependências assimétricas não utilizadas;
- `pip-audit` foi incluído no gate de CI.

### PostgreSQL e migrations

- criado teste de integração que não usa `Base.metadata.create_all()`;
- PostgreSQL 16 validado em container descartável, porta `55432`, `tmpfs` e sem volume persistente;
- `alembic upgrade head` aprovado;
- `alembic current` confirmou `d06cbf4b0231 (head)`;
- `alembic check` não detectou drift;
- smoke real de cadastro, login, JSONB e CRUD de campanha aprovado;
- `alembic downgrade base` aprovado somente no banco descartável;
- novo `upgrade head` e novo smoke aprovados;
- container temporário foi parado e removido automaticamente; seus dados eram descartáveis e não recuperáveis;
- o banco persistente local do projeto não foi alterado.

### CI e frontend quality

- criado `.github/workflows/ci.yml`;
- job backend usa PostgreSQL 16, lock, Ruff, Pytest, Alembic `up/check/test/down/up`, `pip check` e `pip-audit`;
- job frontend usa Node 22, `npm ci`, ESLint, TypeScript, Vitest, build e `npm audit`;
- ESLint e Vitest foram adicionados ao frontend;
- criado smoke test do componente `Button`;
- warning real de dependência instável em `GameProjectsPage` foi corrigido com fallback estável;
- export intencional `useAuth` foi documentado na regra de Fast Refresh.
- PR [#13](https://github.com/GabrielB-B/nat1-rpg-engine/pull/13) executou os jobs canônicos de backend e frontend;
- execução [29651420670](https://github.com/GabrielB-B/nat1-rpg-engine/actions/runs/29651420670) aprovou PostgreSQL, migrations, Ruff, Pytest, `pip-audit`, lint, typecheck, Vitest, build e `npm audit`.

### Produto, arquitetura e governança

- anexo recebido foi incorporado integralmente em
  `VALIDACAO_PRODUTO_E_ESTRATEGIA_DADOS.md`;
- problema, ICP, JTBD, antipersonas, monetização, métricas e experimentos agora têm estado de hipótese explícito;
- não objetivos e instrumentação v0 foram alinhados ao vertical;
- criado `ESCOPO_MVP_VERTICAL_E_GATES.md`;
- criado `ARQUITETURA_C4_E_DEPLOYMENT.md`;
- criado `MODELO_DE_AMEACAS_AUTORIZACAO_E_LGPD.md`;
- criado `PLANO_DE_QUALIDADE_E_CI.md`;
- criado `Docs/IdentidadeVisual/SISTEMA_DE_MARCA_E_DESIGN_TOKENS.md`;
- roadmaps concorrentes foram subordinados à fila única e aos gates;
- o corte canônico passou a ser sessão → cena → acontecimento → recap → pendência;
- Agenda completa ficou no gate opcional G4A, posterior ao vertical e condicionada à validação de H5;
- personagens, locais, facções, relações, documentos, PDF e IA ficaram bloqueados até o piloto.

## Estado funcional preservado

Esta entrega partiu do commit `7cd56d7` de `main` e reforçou segurança, qualidade e
governança sem ampliar os módulos funcionais. Os fatos de produto abaixo permanecem válidos:

### Backend

- FastAPI, SQLAlchemy, Alembic e PostgreSQL;
- cadastro, login JWT e `/auth/me`;
- GameProjects, Worlds, SystemTemplates e ProjectModuleSettings;
- isolamento atual por proprietário;
- summary de campanha com contadores ainda zerados para módulos inexistentes;
- uma migration inicial das tabelas centrais.

### Frontend

- React, TypeScript, Vite, Router e TanStack Query;
- login/cadastro e rotas protegidas;
- biblioteca real de campanhas com criação e arquivamento;
- tema Cartógrafo como fundação visual;
- fundação candidata de marca em elaboração com símbolo, micro marca, favicon, componente
  `BrandMark`, fontes self-hosted e tokens semânticos para os três temas;
- os ativos desta branch são provisórios e ainda não constituem marca final ou liberada
  comercialmente;
- Home ainda integralmente mockada;
- nenhuma shell contextual de campanha;
- nenhum domínio de sessão/cena implementado.

## Verdade sobre o MVP

Implementado:

- conta e autenticação baseline;
- biblioteca de Campanhas & Crônicas;
- fundações de mundo, template e módulos;
- integração frontend/API;
- identidade Cartógrafo inicial;
- implementação candidata/provisória da fundação visual de G1, com QA técnico aprovado
  e QA visual parcial, ainda sujeita às pendências registradas e à aprovação explícita.

Não implementado:

- Home real;
- logo final, aprovação comercial e família completa de ativos finais;
- troca real de tema por campanha;
- shell `/campaigns/:projectId`;
- Session, Scene, SessionOccurrence, SessionRecap e PendingItem;
- agenda completa;
- membership e papéis por campanha;
- personagens, locais, facções, relações, documentos, PDF e IA;
- deployment público e observabilidade.

## Validações de baseline/G0 executadas em 2026-07-18

Este bloco registra a integração de segurança e infraestrutura anterior ao G1. As
validações atuais da fundação visual (3 arquivos/15 testes após o reforço do contrato,
build e QA por viewport) estão consolidadas em
`Docs/IdentidadeVisual/RELATORIO_QA_VISUAL_G1.md`.

- backend Ruff: aprovado;
- backend unitário: `58 passed`, com `1 warning` upstream de Starlette/TestClient;
- migration: `upgrade/current/check/downgrade/upgrade` aprovado;
- PostgreSQL integrado: teste separado `1 passed`, inclusive após o hardening de senha;
- `pip check`: nenhuma dependência quebrada;
- frontend ESLint: aprovado com zero warnings;
- frontend TypeScript: aprovado;
- frontend Vitest: `2 passed`;
- frontend build: aprovado;
- instalação npm: `314 packages`, `0 vulnerabilities` reportadas;
- backend local executado em Python `3.12.6`; a execução remota aprovou a baseline canônica em Python `3.12.13`;
- frontend local executado em Node `22.16.0`; a execução remota aprovou a baseline canônica em Node `22.23.1`;
- auditorias online explícitas locais: não executadas porque o ambiente bloqueou o envio de metadados de dependência a serviço externo;
- auditorias remotas: `pip-audit` e `npm audit --audit-level=high` aprovados no PR #13 após a correção do lock.

Warnings conhecidos:

- Starlette informa depreciação futura do adaptador `httpx` no `TestClient`;
- o warning não quebrou os testes, mas deve ser acompanhado em atualização de dependências.

## Documentos canônicos

- `VALIDACAO_PRODUTO_E_ESTRATEGIA_DADOS.md`
- `ESCOPO_MVP_VERTICAL_E_GATES.md`
- `ARQUITETURA_C4_E_DEPLOYMENT.md`
- `MODELO_DE_AMEACAS_AUTORIZACAO_E_LGPD.md`
- `PLANO_DE_QUALIDADE_E_CI.md`
- `Docs/IdentidadeVisual/SISTEMA_DE_MARCA_E_DESIGN_TOKENS.md`
- `Docs/IdentidadeVisual/INVENTARIO_DE_ATIVOS.md`
- `Docs/IdentidadeVisual/RELATORIO_QA_VISUAL_G1.md`
- `PROXIMAS_TAREFAS_CODEX.md`
- `STATUS_ATUAL.md`

## Pendências e bloqueios

### Encerramento de G0

- a integração deste registro pelo PR #13 materializa o encerramento de G0;
- não restam pendências técnicas do gate; os itens de exposição pública permanecem separados abaixo.

### Antes de beta público

- rate limiting de login/cadastro;
- decisão e implementação da política de sessão/cookie/refresh;
- revogação e rotação;
- CORS HTTPS com host não-loopback validado no domínio real;
- secrets gerenciados;
- logs, métricas, alertas e processo de incidente;
- política de privacidade/termos com revisão jurídica;
- exportação, exclusão, backup e restauração operacionais.

### Ferramentas de design

O plugin Figma e o MCP remoto foram habilitados na configuração global do Codex em
2026-07-18. O OAuth foi concluído anteriormente no host; a revalidação desta rodada ficou
inconclusiva porque o runner isolado não alcança o endpoint externo. As ferramentas não
são carregadas dinamicamente na thread já aberta: é necessário reiniciar a extensão e
continuar em uma nova thread. Nenhum arquivo Figma foi alterado nesta etapa e
o estado do conector não substitui QA nem aprovação visual.

### Saída de G1

G1 permanece em andamento. A fundação documental já existe e a implementação candidata
está nesta branch. O QA técnico passou e há evidências responsivas/temáticas de autenticação,
porém o gate exige cumulativamente:

1. especificação coerente;
2. ativos/tokens aplicados e inventariados;
3. QA técnico e visual com evidências;
4. aprovação explícita de Gabriel.

A liberação comercial da marca é uma decisão posterior e continua condicionada a
proveniência, originalidade, licenças, similaridade e pesquisa marcária.

## Próxima ação obrigatória

Não iniciar Home, shell ou vertical antes do encerramento formal de G1.

1. reiniciar a extensão e produzir no Figma a prancha 16/24/32, lockup vertical e
   revisão de sidebar/empty state;
2. fechar as ressalvas do relatório visual e obter decisão explícita de Gabriel;
3. implementar Home real;
4. implementar shell contextual;
5. entregar o vertical;
6. validar com mestres;
7. somente então avaliar expansão.

Gabriel autorizou explicitamente a publicação e a conclusão do G0 em 2026-07-18.
