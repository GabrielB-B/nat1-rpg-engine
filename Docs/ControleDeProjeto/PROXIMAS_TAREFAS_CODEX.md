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
| 5 | `front/setup-foundation` | concluida | Iniciar React + Vite + TypeScript + Tailwind. |
| 6 | `back/session-scene-foundation` | pendente | Criar fundacao backend de Sessoes e Cenas. |
| 7 | `front/design-system-foundation` | concluida | Aplicar tokens visuais do tema Cartografo. |
| 8 | `front/auth-pages` | pendente | Criar telas de login e cadastro. |
| 9 | `front/home-master-shell` | pendente | Criar shell da Home do Mestre. |

## Regra De Uso

- Antes de iniciar uma tarefa, confirmar branch ativa e escopo.
- Durante a tarefa, nao ultrapassar o prompt aprovado.
- Ao finalizar, atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md`.
- Ao finalizar, registrar testes executados e proxima tarefa recomendada.

## Observacoes Recentes

- Em 2026-06-05, a fase `front/design-system-foundation` recebeu uma rodada adicional de refinamento visual profundo da Home do Mestre no tema `cartographer`.
- Essa rodada nao iniciou nova fase, nao alterou backend e manteve dados mockados.
- Em seguida, a Home recebeu refinamento cirurgico para aproximar saudacao, fundo, topbar, grid e mapa CSS da referencia visual aprovada.
- Apos reprova visual por tela pequena/centralizada, a Home foi corrigida para layout desktop fluido ocupando toda a largura util.
- Apos nova reprova por esticamento excessivo, a Home foi ajustada para largura maxima ampla, ancorada a esquerda, mantendo respiro cartografico a direita em telas grandes.
- Apos refinamento final, a Home teve tipografia, cards de estatistica, altura desktop, breakpoint intermediario e documentacao do menu mockado ajustados sem alterar backend.
- Apos correcao de fidelidade, Campanha ativa e Mapa recente voltaram ao padrao da referencia, com imagem no topo e informacoes abaixo; ajustes restantes ficaram restritos a proporcao, largura, padding e legibilidade.
- Apos nova correcao obrigatoria de densidade, Campanha ativa recebeu `Resumo da campanha`, cards inferiores passaram a mostrar detalhes curtos e o fundo cartographer recebeu topografia sutil em CSS.
