# Proximas Tarefas Codex

Status possiveis:

- `pendente`
- `em andamento`
- `concluida`
- `bloqueada`

## Fila Inicial

| Ordem | Branch | Status | Objetivo |
| --- | --- | --- | --- |
| 1 | `back/database-foundation` | concluida | Criar models centrais e migration inicial. |
| 2 | `back/auth-foundation` | concluida | Criar autenticacao basica com usuario, hash de senha e JWT. |
| 3 | `back/game-project-crud` | concluida | Criar CRUD de Projetos de Jogo. |
| 4 | `back/workspace-foundation` | concluida | Criar Worlds, SystemTemplates, modulos de projeto e summary de GameProject. |
| 5 | `docs/fix-approved-visual-themes` | concluida | Consolidar os temas oficiais `cartographer`, `dark_horror` e `humanist_futuristic`. |
| 6 | `front/setup-foundation` | concluida | Iniciar React + Vite + TypeScript + Tailwind. |
| 7 | `front/design-system-foundation` | pendente | Aplicar componentes base e tokens visuais dos tres temas aprovados. |
| 8 | `front/auth-pages` | pendente | Criar telas de login e cadastro. |
| 9 | `front/master-home-shell` | pendente | Criar shell da Home do Mestre. |
| 10 | `back/session-scene-foundation` | pendente | Criar fundacao backend de Sessoes e Cenas. |

## Regra De Uso

- Antes de iniciar uma tarefa, confirmar branch ativa e escopo.
- Durante a tarefa, nao ultrapassar o prompt aprovado.
- Ao finalizar, atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md`.
- Ao finalizar, registrar testes executados e proxima tarefa recomendada.
