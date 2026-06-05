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
| 5 | `front/setup-foundation` | pendente | Iniciar React + Vite + TypeScript + Tailwind. |
| 6 | `back/session-scene-foundation` | pendente | Criar fundacao backend de Sessoes e Cenas. |
| 7 | `front/design-system-foundation` | pendente | Aplicar tokens visuais do tema Cartografo. |
| 8 | `front/auth-pages` | pendente | Criar telas de login e cadastro. |
| 9 | `front/home-master-shell` | pendente | Criar shell da Home do Mestre. |

## Regra De Uso

- Antes de iniciar uma tarefa, confirmar branch ativa e escopo.
- Durante a tarefa, nao ultrapassar o prompt aprovado.
- Ao finalizar, atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md`.
- Ao finalizar, registrar testes executados e proxima tarefa recomendada.
