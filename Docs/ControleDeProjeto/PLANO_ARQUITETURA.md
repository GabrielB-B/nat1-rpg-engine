# Plano De Arquitetura

Projeto: Nat 1 RPG Engine

Data de referencia: 2026-06-21

Fase relacionada: `docs/architecture-roadmap-checkpoints`

## Objetivo

Registrar a arquitetura atual do Nat 1 RPG Engine, os limites entre camadas, os fluxos principais e os pontos que devem orientar as próximas fases de desenvolvimento.

## Visao Geral

O Nat 1 RPG Engine é organizado como uma aplicação web com backend FastAPI, frontend React e documentação técnica versionada no repositório.

Estrutura principal:

- `apps/api`: API HTTP, regras de negócio, persistência e testes de backend.
- `apps/web`: interface web, autenticação frontend, design system, rotas e integrações com a API.
- `Docs`: documentação de produto, identidade visual, controle de projeto, arquitetura e decisões técnicas.

## Backend

Stack atual:

- FastAPI.
- PostgreSQL.
- SQLAlchemy.
- Alembic.
- Pydantic.
- JWT Bearer token.
- bcrypt para hash de senha.
- pytest.
- ruff.

Organização principal:

| Diretório | Responsabilidade |
| --- | --- |
| `app/api/v1/endpoints` | Rotas HTTP versionadas. |
| `app/api/deps.py` | Dependências compartilhadas, incluindo autenticação do usuário atual. |
| `app/core` | Configuração, segurança e utilitários centrais. |
| `app/db` | Base declarativa e sessão de banco. |
| `app/models` | Models SQLAlchemy. |
| `app/repositories` | Acesso a dados e consultas persistentes. |
| `app/schemas` | Schemas Pydantic de entrada e saída. |
| `app/services` | Regras de negócio e orquestração entre repositories. |
| `tests` | Testes automatizados de backend. |

Fluxo padrão de requisição:

1. Endpoint recebe a requisição.
2. Dependências validam autenticação e sessão de banco quando necessário.
3. Service aplica regra de negócio.
4. Repository executa leitura ou escrita no banco.
5. Schema Pydantic define a resposta.

## Endpoints Atuais

| Domínio | Endpoints principais | Status |
| --- | --- | --- |
| Health | `GET /health` | Implementado. |
| Auth | `POST /auth/register`, `POST /auth/login`, `GET /auth/me` | Implementado. |
| GameProjects | Criar, listar, detalhar, atualizar, arquivar e restaurar | Implementado. |
| ProjectModuleSettings | Listar e atualizar módulos por campanha | Implementado. |
| Worlds | Criar, listar, detalhar, atualizar, arquivar e restaurar | Implementado. |
| SystemTemplates | Criar, listar, detalhar, atualizar e arquivar | Implementado. |
| GameProject Summary | `GET /game-projects/{project_id}/summary` | Implementado com contadores básicos. |

## Modelo De Dados Atual

Entidades atuais:

- `User`: conta do usuário autenticado.
- `GameProject`: unidade principal do produto, exibida como Campanhas & Crônicas.
- `World`: mundo ou cenário reutilizável.
- `SystemTemplate`: sistema ou template de regras.
- `ProjectModuleSetting`: configuração de módulos ativos por campanha.

Regras estruturais:

- Entidades de usuário devem respeitar isolamento por `owner_user_id`.
- `GameProject` usa slug único por usuário.
- Arquivamento é preferido a exclusão permanente.
- Mundos e templates podem ser vinculados a campanhas.
- Templates internos do produto podem não pertencer a um usuário específico.

## Frontend

Stack atual:

- React.
- TypeScript.
- Vite.
- Tailwind CSS.
- React Router.
- TanStack Query.
- lucide-react.

Organização principal:

| Diretório | Responsabilidade |
| --- | --- |
| `src/app` | App, router e providers. |
| `src/layouts` | Layouts de rotas públicas, autenticadas e shell principal. |
| `src/pages` | Páginas roteáveis. |
| `src/features` | Domínios de produto e integração. |
| `src/lib/api` | Client HTTP, erros e helpers de requisição. |
| `src/components` | Componentes compartilhados de UI, layout e dashboard. |
| `src/styles` | CSS global e tokens de tema. |
| `src/data` | Dados mockados isolados para a Home do Mestre. |

Rotas atuais:

| Rota | Proteção | Função |
| --- | --- | --- |
| `/login` | Pública | Login com API real. |
| `/register` | Pública | Cadastro com API real. |
| `/` | Protegida | Home do Mestre mockada. |
| `/campaigns` | Protegida | Campanhas & Crônicas com dados reais. |
| `*` | Pública | Not found. |

Fluxo de autenticação frontend:

1. Token JWT é salvo em `localStorage`.
2. API client injeta `Authorization: Bearer TOKEN`.
3. `GET /auth/me` valida o usuário atual.
4. Rotas protegidas redirecionam usuários não autenticados para `/login`.
5. Rotas públicas redirecionam usuários autenticados para a Home.
6. Logout remove token e limpa cache protegido.

## Design System E Temas

Tema ativo:

- `cartographer`.

Temas planejados:

- `dark_horror`.
- `humanist_futuristic`.

Diretrizes atuais:

- Componentes devem consumir variáveis CSS de tema.
- Telas de produto devem preservar a identidade cartográfica aprovada.
- Componentes compartilhados devem manter estados de loading, erro, vazio e sucesso.
- Ícones devem usar escala consistente e stroke visual coerente.

## Infraestrutura Local

Itens atuais:

- Docker Compose para PostgreSQL local.
- `.env.example` para configuração esperada.
- `.gitignore` cobrindo `.env`, ambientes virtuais, caches, builds e artefatos locais.
- Branches por fase.
- Pull Requests para integração na branch principal.

Comandos principais:

- Backend: `pytest`, `ruff check .`, `alembic upgrade head`, `uvicorn app.main:app --reload`.
- Frontend: `npm.cmd run build`, `npm.cmd run dev`, `npm.cmd run typecheck`.
- Git: `git status`, `git diff --check`.

## Riscos E Lacunas

- Home do Mestre ainda usa dados mockados.
- Shell interna de campanha ainda não existe.
- Sessões, cenas, personagens, locais, facções, notas, documentos, mapas e relações ainda não possuem CRUD completo.
- Participantes e permissões avançadas ainda não foram modelados.
- Refresh token, recuperação de senha e OAuth externo permanecem fora do escopo atual.
- Upload, ingestão de documentos e IA/RAG dependem de fases próprias de segurança, armazenamento, revisão e aprovação do mestre.
- Observabilidade, deploy e checklist de produção ainda precisam de fases dedicadas.

## Regras De Continuidade Arquitetural

- Toda nova entidade deve definir dono, escopo e regra de isolamento.
- Toda nova rota protegida deve validar usuário autenticado e acesso ao recurso.
- Toda alteração de model deve vir acompanhada de migration e teste aplicável.
- Toda tela conectada à API deve ter loading, erro, vazio e sucesso.
- Toda integração assíncrona no frontend deve preferir hooks de domínio com TanStack Query.
- Toda decisão arquitetural relevante deve ser registrada em `DECISOES_TECNICAS.md`.

