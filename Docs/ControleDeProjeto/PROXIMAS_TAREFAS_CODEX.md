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
| 5 | `docs/fix-approved-visual-themes` | concluida | Consolidar os tres temas visuais oficiais antes do frontend. |
| 6 | `front/setup-foundation` | pendente | Iniciar React + Vite + TypeScript + Tailwind. |
| 7 | `back/session-scene-foundation` | pendente | Criar fundacao backend de Sessoes e Cenas. |
| 8 | `front/design-system-foundation` | pendente | Aplicar tokens visuais dos temas aprovados. |
| 9 | `front/auth-pages` | pendente | Criar telas de login e cadastro. |
| 10 | `front/home-master-shell` | pendente | Criar shell da Home do Mestre. |

## Regra De Uso

- Antes de iniciar uma tarefa, confirmar branch ativa e escopo.
- Durante a tarefa, nao ultrapassar o prompt aprovado.
- Ao finalizar, atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md`.
- Ao finalizar, registrar testes executados e proxima tarefa recomendada.
