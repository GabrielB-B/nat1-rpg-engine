# Plano De Trabalho

Documento complementar de direcao de produto: `Docs/ControleDeProjeto/PLANO_PRODUTO_E_REFERENCIAS.md`.

## Prioridade Direcional Atual

1. Home do Mestre.
2. Campanhas & Crônicas.
3. Modulos relacionais dentro da campanha.
4. Mundo / Cenario amplo para worldbuilding.
5. Sistema / Template separado de mundo.
6. IA e PDF inteligente com aprovacao do mestre.

Proxima fase recomendada: `front/home-master-real-data`.

Este plano organiza as fases práticas do Nat 1 RPG Engine para manter escopo, validação e continuidade entre tarefas.

## Fase A - Fundação Do Repositório E Backend

Objetivo: criar a base inicial do backend e do repositório.

Entregáveis:
- Estrutura `apps/api`.
- FastAPI configurado.
- Endpoint `GET /api/v1/health`.
- Settings por ambiente.
- SQLAlchemy base/session.
- Alembic preparado.
- README inicial e `.gitignore`.

Fora de escopo:
- Frontend.
- CRUD de negócio.
- Autenticação completa.
- IA, RAG, upload inteligente, jogadores e mapas avançados.

Critérios de aceite:
- `uvicorn app.main:app --reload` sobe a API.
- `GET /api/v1/health` retorna `{"status":"ok","service":"nat1-api"}`.
- `pytest` passa.
- `ruff check .` passa.

## Fase B - Modelagem Central E Alembic

Objetivo: criar a fundação de banco do MVP 1.

Entregáveis:
- Models centrais: `User`, `World`, `SystemTemplate`, `GameProject`, `ProjectModuleSetting`.
- Constraints centrais.
- Metadata reconhecida pelo Alembic.
- Migration inicial.
- Testes básicos de import/metadata dos models.

Fora de escopo:
- CRUD.
- Rotas autenticadas.
- Seeders completos.
- Models de todos os módulos internos.

Critérios de aceite:
- Alembic gera SQL válido para PostgreSQL.
- Alembic aplica e reverte migration em ambiente de validação.
- `pytest` passa.
- `ruff check .` passa.

## Fase C - Autenticação Básica

Objetivo: permitir cadastro, login e identificação de usuário autenticado.

Entregáveis:
- Schemas de autenticação.
- Hash seguro de senha.
- JWT access token.
- Endpoints de cadastro, login e usuário atual.
- Proteção inicial de rotas privadas.

Fora de escopo:
- OAuth.
- Recuperação de senha.
- Refresh token avançado.
- Permissões de jogadores.

Critérios de aceite:
- Usuário pode cadastrar com nome, email e senha.
- Email duplicado é bloqueado.
- Login retorna token válido.
- Senha não é salva em texto puro.
- Testes de autenticação passam.

## Fase D - CRUD De Projetos De Jogo

Objetivo: permitir gerenciar Campanhas & Crônicas como Projetos de Jogo.

Entregáveis:
- Endpoints para criar, listar, detalhar, atualizar e arquivar Projetos de Jogo.
- Isolamento por usuário autenticado.
- Validação de slug por usuário.
- Tema padrão Cartógrafo.

Fora de escopo:
- Dashboard visual.
- CRUD dos módulos internos.
- Compartilhamento com jogadores.

Critérios de aceite:
- Usuário lista apenas seus próprios Projetos.
- Projeto pode ser criado com nome e formato.
- Slug é único por usuário.
- Arquivamento evita exclusão permanente.
- Testes de isolamento passam.

## Fase E - Home Do Mestre API

Objetivo: entregar dados mínimos para a Home do Mestre.

Entregáveis:
- Endpoint de resumo da Home.
- Lista de Projetos recentes.
- Acesso ao último Projeto aberto ou atualizado.
- Contadores básicos quando disponíveis.

Fora de escopo:
- Frontend da Home.
- Busca avançada.
- Notas globais completas se ainda não estiverem modeladas.

Critérios de aceite:
- Endpoint exige autenticação.
- Dados retornados pertencem ao usuário autenticado.
- Estado vazio é representável pela API.
- Testes passam.

## Fase F - Frontend Foundation

Objetivo: iniciar o frontend oficial.

Entregáveis:
- `apps/web` com React, TypeScript e Vite.
- Tailwind CSS configurado.
- React Router.
- TanStack Query.
- React Hook Form e Zod preparados.

Fora de escopo:
- Telas completas.
- Design system final.
- Integração ampla com todos os endpoints.

Critérios de aceite:
- Frontend roda localmente.
- Estrutura de pastas está clara.
- Build inicial passa.
- Nenhum visual genérico ou fora da identidade aprovada.

## Fase G - Design System Inicial

Objetivo: aplicar tokens visuais do tema Cartógrafo.

Entregáveis:
- Tokens de cor, tipografia, espaçamento e superfície.
- Componentes base.
- Estados de loading, erro, vazio e sucesso.
- Preparação para temas Sombrio/Terror e Futurista.

Fora de escopo:
- Implementação completa dos temas alternativos.
- Ilustrações finais.
- Dashboard completo.

Critérios de aceite:
- Tema Cartógrafo é reconhecível.
- Componentes mantêm acessibilidade básica.
- Interface não parece genérica.
- Tokens permitem evolução de temas.

## Fase H - Dashboard Do Projeto

Objetivo: criar a primeira visão funcional dentro de um Projeto de Jogo.

Entregáveis:
- Shell do Dashboard.
- Contexto claro de Projeto ativo.
- Atalhos para módulos ativos.
- Dados básicos de Projeto.

Fora de escopo:
- CRUD completo de todos os módulos.
- IA da campanha.
- Mapas avançados.

Critérios de aceite:
- Dashboard exige autenticação.
- Usuário não acessa Projeto de outro usuário.
- Módulos ocultos não aparecem como destaque.
- Estados vazios são úteis.

## Fase I - Módulos Internos Essenciais

Objetivo: implementar os módulos centrais do MVP 1 por etapas.

Entregáveis:
- Sessões.
- Cenas.
- Personagens & Criaturas.
- Locais / Atlas.
- Organizações / Facções.
- Documentos.
- Notas.
- Relações.

Fora de escopo:
- IA/RAG.
- Eventos, calendários e timelines completos.
- Mapas com pins/camadas.
- Jogadores e permissões.

Critérios de aceite:
- Cada módulo tem CRUD testado.
- Registros pertencem ao usuário e ao contexto correto.
- Arquivamento é preferido a exclusão permanente.
- Relações preservam integridade mínima.

## Fase J - Refinamento, Testes E Documentação

Objetivo: estabilizar o MVP 1 para entrega apresentável.

Entregáveis:
- Revisão de UX.
- Testes de fluxos principais.
- Documentação de instalação, manutenção e entrega.
- Checklist de segurança básica.
- Guia de deploy inicial.

Fora de escopo:
- Expansões de fase 2.
- IA pesada.
- Marketplace, monetização ou integrações externas complexas.

Critérios de aceite:
- Fluxos principais rodam localmente.
- Documentação permite continuidade do projeto.
- Testes críticos passam.
- Escopo do MVP 1 está claro e controlado.
