# Relatorio De Seguranca Baseline

Projeto: Nat 1 RPG Engine

Início: 2026-06-21

Validação complementar: 2026-07-18

Fase: `security/baseline-hardening`

Branch: `security/baseline-hardening`

Status: baseline preparada e checks locais executáveis aprovados; auditorias online, revisão, CI remoto e integração pendentes

## Escopo Analisado

- Backend FastAPI: configuração, JWT, dependências de autenticação, endpoints v1, services, repositories, models, schemas e testes.
- Frontend React/Vite: fluxo de login/cadastro, storage de token, API client, rotas protegidas, tratamento de `401`, formulário de campanhas e validação de URL de capa.
- Configuração local: `.gitignore`, `.env.example`, `docker-compose.yml`, dependências backend e dependências frontend.
- Documentação de controle do projeto.

## Comandos executados na validação inicial — 2026-06-21

- `git switch security/baseline-hardening`
- `git merge --ff-only main`
- `pytest`
- `ruff check .`
- `.\.venv\Scripts\python.exe -m pytest`
- `.\.venv\Scripts\python.exe -m ruff check .`
- `.\.venv\Scripts\python.exe -m pip check`
- `npm.cmd run build`
- `npm.cmd audit`
- `git status --short --branch`
- Varreduras locais com `rg` para secrets, tokens, logs, `dangerouslySetInnerHTML`, storage, URLs e arquivos sensíveis versionados.

## Resultados da validação inicial — 2026-06-21

- `pytest`: falhou no Python global por ausência de `psycopg`.
- `ruff check .`: falhou no shell global porque `ruff` não está no `PATH`.
- `.\.venv\Scripts\python.exe -m pytest`: aprovado com `33 passed, 1 warning`.
- `.\.venv\Scripts\python.exe -m ruff check .`: aprovado.
- `.\.venv\Scripts\python.exe -m pip check`: aprovado sem dependências quebradas.
- `npm.cmd run build`: aprovado.
- `npm.cmd audit`: aprovado com `0 vulnerabilities`.
- Varredura de arquivos sensíveis versionados: apenas `.env.example` permitido.
- Varredura de `dangerouslySetInnerHTML`: sem ocorrências.
- Varredura de token/senha: ocorrências esperadas em código de autenticação, testes e documentação; nenhum token real identificado.

## Achados Corrigidos

### Alto - Placeholder De Secret Em Ambiente Não Local

- Risco: ambiente não local poderia iniciar com `SECRET_KEY` de exemplo caso a variável não fosse substituída.
- Correção: adicionada validação em `Settings` para rejeitar placeholders de `SECRET_KEY` fora de ambientes locais/teste.
- Arquivos:
  - `apps/api/app/core/config.py`
  - `apps/api/.env.example`
  - `apps/api/tests/test_security_baseline.py`

### Médio - Backend Aceitava URL De Capa Com Protocolo Não Seguro

- Risco: `cover_image_url` poderia armazenar protocolos como `javascript:` em payloads enviados diretamente para a API.
- Correção: adicionada validação backend para aceitar apenas URLs `http` e `https`, com normalização de string vazia para `None`.
- Arquivos:
  - `apps/api/app/schemas/game_project.py`
  - `apps/api/tests/test_game_projects.py`

### Médio - Cobertura Insuficiente Contra IDOR Em Mutações De Campanha

- Risco: regressão futura poderia permitir update, archive ou restore de campanha pertencente a outro usuário.
- Correção: adicionados testes para bloquear update, archive e restore cross-user com resposta `404`.
- Arquivo:
  - `apps/api/tests/test_game_projects.py`

### Baixo - Cobertura Insuficiente Para Token Inválido E Enumeração No Login

- Risco: regressão futura poderia retornar erro diferente para e-mail inexistente ou aceitar token inválido.
- Correção: adicionados testes para token inválido em `/auth/me` e erro genérico no login com e-mail inexistente.
- Arquivo:
  - `apps/api/tests/test_auth.py`

### Baixo - `.gitignore` Sem Artefatos Locais Comuns

- Risco: caches, relatórios de teste, bancos locais e artefatos temporários poderiam entrar no controle de versão.
- Correção: adicionadas entradas para `.mypy_cache`, `.cache`, `coverage`, `test-results`, `playwright-report`, `tmp`, `temp`, `*.sqlite`, `*.sqlite3` e `*.db`.
- Arquivo:
  - `.gitignore`

## Achados Pendentes E Resolvidos Na Continuação

### Médio - Token JWT Armazenado Em `localStorage`

- Contexto: o frontend armazena o access token em `localStorage`.
- Risco: exposição do token em caso de XSS.
- Recomendação: avaliar cookies `HttpOnly`, `Secure` e `SameSite` com refresh token em fase dedicada de autenticação avançada.

### Médio - Ausência De Rate Limiting Em Login/Cadastro

- Contexto: endpoints de autenticação não possuem limitação de tentativas.
- Risco: brute force ou abuso automatizado em ambiente exposto.
- Recomendação: adicionar rate limiting por IP/e-mail e estratégia de lockout suave em fase futura.

### Médio - CORS De Produção Depende De Configuração Operacional

- Estado: mitigação de configuração implementada; domínio real ainda depende do deploy.
- Correção: HTTP é aceito apenas em local/teste; fora desses ambientes, toda origem CORS deve usar HTTPS e host não-loopback. Métodos e headers também foram restringidos.
- Pendência: configurar e testar a origem HTTPS real antes de produção.

### Resolvido - Dependências Backend Sem Lock Completo

- Correção: dependências diretas foram fixadas, `requirements.lock` foi criado e `pip-audit` entrou no gate de CI.
- Governança: updates exigem revisão, testes e regeneração intencional do lock.

### Resolvido - Biblioteca JWT Trazia ECDSA Vulnerável Sem Necessidade

- Achado: `python-jose` trazia `ecdsa`, afetada por [CVE-2024-23342 / GHSA-wj6h-64fc-37mp](https://github.com/advisories/GHSA-wj6h-64fc-37mp), sem versão corrigida disponível.
- Contexto de uso: o Nat 1 assina e valida access tokens somente com `HS256`; algoritmos assimétricos não fazem parte do contrato atual.
- Correção: substituição por `PyJWT==2.13.0` sem extra criptográfico, allowlist explícita de `HS256` e exigência das claims `sub` e `exp`.
- Efeito: `ecdsa`, `rsa` e `pyasn1` foram removidas do lock, reduzindo a superfície de dependências.
- Validação: testes, `pip check` e lock devem ser comprovados no fechamento; `pip-audit` permanece pendente e não é declarado verde neste relatório.

### Resolvido - Ambiente, Banco E Secret Possuíam Defaults Implícitos

- Risco: uma execução fora do fluxo documentado poderia inferir ambiente local, conectar ao banco local ou usar secret implícito.
- Correção: `ENVIRONMENT`, `DATABASE_URL` e `SECRET_KEY` passaram a ser campos obrigatórios de `Settings`; ausência ou valor inválido impede a inicialização.
- Regras adicionais fora de local/teste: `SECRET_KEY` exige ao menos 32 caracteres e rejeita placeholders; a URL/credencial local documentada é recusada; CORS exige HTTPS e host não-loopback.

### Resolvido - Limite De 72 Bytes Do bcrypt Direto

- Risco: bcrypt direto trunca entradas acima de 72 bytes e não atende sozinho ao limite funcional de 128 caracteres adotado no cadastro.
- Correção: novos hashes usam `bcrypt_sha256`; o contexto mantém bcrypt legado como algoritmo depreciado para migração.
- Migração: login legado válido executa rehash oportunístico e persiste `bcrypt_sha256` na mesma transação de autenticação.
- Limites: senha nova aceita de 8 a 128 caracteres; entrada acima de 128 caracteres ou senha bcrypt legada acima de 72 bytes recebe o mesmo erro genérico de credencial inválida.
- Pendência: conta legada que atingir o limite de 72 bytes dependerá do futuro fluxo seguro de reset de senha.

### Resolvido Como Baseline - Headers De Segurança HTTP

- Correção: middleware adiciona `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy` e `Permissions-Policy`.
- Pendência de produção: CSP, HSTS e política final devem considerar domínio, proxy, Swagger e estratégia de frontend.

### Controlado Em Desenvolvimento - Credenciais Locais No `docker-compose.yml`

- Contexto: compose usa usuário e senha locais previsíveis para PostgreSQL.
- Controle: a URL correspondente é dev-only e a API a recusa quando `ENVIRONMENT` não é local/teste.
- Pendência operacional: ambientes compartilhados ou produção exigem banco e secrets externos próprios.

## Revisão De Autenticação

- Novos hashes usam `bcrypt_sha256` via `passlib`; bcrypt direto é aceito somente para migração legada.
- Login legado válido regrava o hash oportunisticamente; limites recusados não expõem a causa ao cliente.
- `password_hash` não aparece em `UserRead`.
- Login retorna erro genérico para credenciais inválidas.
- `/auth/me` exige Bearer token.
- JWT usa `SECRET_KEY` via settings e possui expiração.
- Endpoints protegidos usam `get_current_user`.
- `ENVIRONMENT`, `DATABASE_URL` e `SECRET_KEY` são explícitos em todo ambiente; placeholder, secret curto e URL local documentada são bloqueados fora de local/teste.
- JWT usa `PyJWT` sem extra criptográfico e aceita somente `HS256` no contrato atual.

## Revisão De Autorização

- GameProject usa filtro por `owner_user_id` para listagem, leitura, update, archive, restore e summary.
- World usa filtro por `owner_user_id` para listagem, leitura, update, archive e restore.
- ProjectModuleSettings exige projeto pertencente ao usuário autenticado.
- SystemTemplates permite templates built-in globais e bloqueia update/archive de built-ins.
- Testes de IDOR foram reforçados para mutações de GameProject.

## Revisão Do Frontend

- Token não é exibido na UI.
- Senha não é armazenada em storage.
- Logout remove token e limpa cache do TanStack Query.
- Respostas `401` em chamadas protegidas disparam logout no API client.
- Rotas protegidas exibem estado de validação antes de renderizar conteúdo.
- Não foram encontradas ocorrências de `dangerouslySetInnerHTML`.
- Formulário de campanha valida URL de capa como `http` ou `https`.
- Erros de formulário usam mensagens amigáveis sem stack trace.

## Itens Fora De Escopo

- Pentest agressivo.
- Fuzzing pesado.
- OWASP ZAP automático.
- Migração para cookies `HttpOnly`.
- Refresh token.
- MFA.
- Permissões avançadas.
- Upload de arquivos.
- IA.
- Calendário e sessões.

## Validação Complementar Com PostgreSQL E CI

- PostgreSQL 16 executado em container descartável `nat1_postgres_validation`, porta `55432`, armazenamento `tmpfs` e sem volume persistente.
- `alembic upgrade head`, `current` e `check` aprovados.
- Teste integrado executou cadastro, login, JSONB e ciclo de campanha com criação,
  leitura, atualização, listagem, arquivamento e restauração sobre o schema migrado.
- `alembic downgrade base` e novo `upgrade head` aprovados no banco descartável.
- Smoke PostgreSQL repetido e aprovado após a reaplicação.
- Ruff aprovado; unitários `58 passed`, com `1 warning` upstream de Starlette/TestClient; integração PostgreSQL separada `1 passed`; `pip check` sem dependências quebradas.
- Frontend ESLint, TypeScript, Vitest `2 passed` e build aprovados.
- CI adicionado com PostgreSQL, migration, backend, frontend e auditorias.
- Chamadas locais explícitas a serviços externos de auditoria foram bloqueadas pela política do ambiente; esses gates precisam ser comprovados no Pull Request.
- O resultado inicial de `npm audit` acima pertence à execução de 2026-06-21. Na
  validação complementar, nenhuma auditoria online foi declarada verde localmente.

## Próxima Ação Recomendada

Fase: concluir G0 por revisão, commit autorizado, Pull Request, CI verde e integração.

Antes de beta público, executar `security/public-auth-session-hardening` com rate limiting,
estratégia de cookie/refresh, revogação, CORS HTTPS/não-loopback no domínio real,
secrets gerenciados e observabilidade.
