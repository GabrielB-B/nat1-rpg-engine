# Status Atual

Projeto: Nat 1 RPG Engine

Data da última atualização: 2026-07-18

Fase atual: G0 — `security/baseline-hardening`

Branch: `security/baseline-hardening`

Status: publicação autorizada; commit, Pull Request, CI remoto e integração em execução

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

## Estado técnico implementado em `main`

Esta branch partiu do commit `7cd56d7` de `main`. Enquanto o Pull Request não for
integrado, os fatos abaixo representam o produto já versionado antes desta branch:

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
- Home ainda integralmente mockada;
- nenhuma shell contextual de campanha;
- nenhum domínio de sessão/cena implementado.

## Verdade sobre o MVP

Implementado:

- conta e autenticação baseline;
- biblioteca de Campanhas & Crônicas;
- fundações de mundo, template e módulos;
- integração frontend/API;
- identidade Cartógrafo inicial.

Não implementado:

- Home real;
- logo final e ativos vetoriais padronizados;
- troca real de tema por campanha;
- shell `/campaigns/:projectId`;
- Session, Scene, SessionOccurrence, SessionRecap e PendingItem;
- agenda completa;
- membership e papéis por campanha;
- personagens, locais, facções, relações, documentos, PDF e IA;
- deployment público e observabilidade.

## Validações executadas em 2026-07-18

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
- backend local executado em Python `3.12.6`; a baseline canônica usa `3.12.13` e
  depende do CI remoto para comprovação nesse patch runtime;
- frontend local executado em Node `22.16.0`; a baseline canônica usa `22.23.1` e
  depende do CI remoto para comprovação nesse patch LTS;
- auditorias online explícitas locais: não executadas porque o ambiente bloqueou o envio de metadados de dependência a serviço externo;
- auditorias remotas: configuradas e pendentes de comprovação no Pull Request.

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
- `PROXIMAS_TAREFAS_CODEX.md`
- `STATUS_ATUAL.md`

## Pendências e bloqueios

### Para concluir G0

- criar e publicar o commit autorizado por Gabriel;
- abrir o Pull Request;
- comprovar CI remoto, inclusive auditorias;
- integrar após CI verde e revisão final.

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

A instalação/liberação do Figma foi solicitada pelo usuário, porém o conector não ficou
exposto entre as ferramentas desta sessão. A especificação de marca foi consolidada sem
bloquear o gate. Ativos vetoriais e aplicação visual permanecem para branch própria.

## Próxima ação obrigatória

Não iniciar Home, shell ou vertical nesta branch.

1. publicar e integrar G0 conforme autorização concedida;
2. concluir a marca/tokens em branch visual;
3. implementar Home real;
4. implementar shell contextual;
5. entregar o vertical;
6. validar com mestres;
7. somente então avaliar expansão.

Gabriel autorizou explicitamente a publicação e a conclusão do G0 em 2026-07-18.
