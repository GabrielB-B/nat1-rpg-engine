# Status Atual

Projeto: Nat 1 RPG Engine

Fase atual: `docs/architecture-roadmap-checkpoints`

Branch: `docs/architecture-roadmap-checkpoints`

Status: concluída em validação local

Data da última atualização: 2026-06-21

## Últimas Entregas

- Criado plano de arquitetura em `Docs/ControleDeProjeto/PLANO_ARQUITETURA.md`.
- Criado mapa de módulos atuais e planejados em `Docs/ControleDeProjeto/MODULOS_DO_SISTEMA.md`.
- Criado controle de checkpoints em `Docs/ControleDeProjeto/CHECKPOINTS.md`.
- Criado guia de padrões de engenharia em `Docs/ControleDeProjeto/PADROES_DE_ENGENHARIA.md`.
- Criado registro de decisões técnicas em `Docs/ControleDeProjeto/DECISOES_TECNICAS.md`.
- Atualizada fila técnica do MVP com a fase documental atual.
- Preservados histórico técnico, plano de produto, temas aprovados e roadmap existente.
- Nenhuma funcionalidade de backend ou frontend foi implementada nesta fase.
- Nenhuma migration, dependência ou alteração de banco foi adicionada nesta fase.

## Estado Técnico Do Produto

Backend concluído até esta etapa:

- Fundação FastAPI com PostgreSQL local via Docker.
- SQLAlchemy, Alembic e settings com `pydantic-settings`.
- Autenticação com JWT.
- Hash de senha com bcrypt.
- Swagger Authorize com OAuth2PasswordRequestForm usando `username` como e-mail.
- CRUD de GameProject / Campanhas & Crônicas.
- Workspace foundation com Worlds, SystemTemplates, ProjectModuleSettings e GameProject Summary.
- Testes automatizados com `pytest`.
- Validação estática com `ruff`.

Frontend concluído até esta etapa:

- React, TypeScript, Vite, Tailwind CSS, React Router e TanStack Query.
- API client centralizado em `apps/web/src/lib/api/client.ts`.
- Tratamento de erro em `apps/web/src/lib/api/errors.ts`.
- Helper HTTP em `apps/web/src/lib/api/http.ts`.
- Design system inicial com componentes de UI, layout e dashboard.
- Home do Mestre mockada no tema `cartographer`.
- Telas de login e cadastro integradas aos endpoints reais de autenticação local.
- Guardas básicos para rotas públicas e protegidas.
- Tela `/campaigns` integrada a dados reais de GameProjects, Worlds e SystemTemplates.
- Formulário de criação de campanha integrado à API real.
- Arquivamento de campanha integrado ao endpoint real `POST /game-projects/{project_id}/archive`.
- Listagem de arquivadas usando `include_archived=true` e filtro local.

## Documentos De Controle Ativos

- `Docs/ControleDeProjeto/STATUS_ATUAL.md`
- `Docs/ControleDeProjeto/HISTORICO_TECNICO.md`
- `Docs/ControleDeProjeto/PROXIMAS_TAREFAS_CODEX.md`
- `Docs/ControleDeProjeto/PLANO_DE_TRABALHO.md`
- `Docs/ControleDeProjeto/PLANO_PRODUTO_E_REFERENCIAS.md`
- `Docs/ControleDeProjeto/PLANO_ARQUITETURA.md`
- `Docs/ControleDeProjeto/MODULOS_DO_SISTEMA.md`
- `Docs/ControleDeProjeto/CHECKPOINTS.md`
- `Docs/ControleDeProjeto/PADROES_DE_ENGENHARIA.md`
- `Docs/ControleDeProjeto/DECISOES_TECNICAS.md`
- `Docs/ControleDeProjeto/PROTOCOLO_DE_BRANCHES.md`

## Validações Executadas

- `git diff --check`
- Varredura textual de tom documental proibido.
- Varredura de espaços finais nos documentos.
- Revisão de arquivos alterados para confirmar ausência de código funcional.
- `npm.cmd run build`
- `pytest`
- `git status --short --branch`

## Resultado Das Validações

- Build do frontend concluído com sucesso.
- Testes automatizados do backend concluídos com `25 passed, 1 warning`.
- Varredura de tom documental proibido sem ocorrências.
- Varredura de espaços finais sem ocorrências.
- Alterações funcionais de backend e frontend ausentes no diff.
- Arquivos novos restritos à documentação de controle.
- `git diff --check` executado após correção de linha em branco final.

## Pendências Conhecidas

- Home do Mestre permanece mockada.
- CTA "Abrir campanha" permanece visual porque a shell interna da campanha ainda não existe.
- Gênero/tom narrativo não é enviado para a API por falta de campo explícito no backend.
- Jogadores ativos não são exibidos como dado real porque o backend ainda não possui campo ou relação de participantes.
- Próxima sessão não é exibida como dado real porque sessões ainda não possuem entidade no backend.
- Sem edição visual de campanha.
- Sem restauração visual de campanha.
- Sem exclusão permanente.
- Sem refresh token.
- Sem recuperação de senha.
- Sem OAuth externo.
- Sem permissões avançadas.
- Sem script `lint` configurado em `apps/web/package.json`.
- Segurança de produção, observabilidade e deploy ainda exigem fases próprias.

## Próxima Etapa Recomendada

Fase recomendada: `front/home-master-real-data`

Objetivo: conectar a Home do Mestre aos dados reais já disponíveis, usando as campanhas criadas pelo frontend.

Justificativa técnica: o fluxo cadastro, login, listagem, criação e arquivamento de campanha já existe. A Home do Mestre pode deixar de depender exclusivamente de mocks e passar a refletir o estado real da conta.

Alternativa técnica posterior: `front/game-project-dashboard-shell`, para criar a entrada interna de cada campanha com summary e módulos ativos.

## Bloqueios Atuais

Nenhum bloqueio técnico registrado.
