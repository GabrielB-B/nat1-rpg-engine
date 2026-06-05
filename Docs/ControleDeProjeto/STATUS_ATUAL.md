# Status Atual

## Identificacao

Projeto: Nat 1 RPG Engine
Fase atual: Documentacao visual antes do frontend
Data da ultima atualizacao: 2026-06-05
Branch atual: `docs/fix-approved-visual-themes`

## Tarefa Atual

Corrigir e consolidar os tres temas visuais oficiais antes do inicio do frontend.

## Ultima Tarefa Concluida

Documentacao dos temas aprovados consolidada em `Docs/IdentidadeVisual/TEMAS_APROVADOS.md`, com destaque para a correcao do Tema Futurista Humanista para evitar repeticao indevida do Cartografo.

## Estado Tecnico Do Produto

Backend concluido ate esta etapa:

- backend foundation;
- PostgreSQL local via Docker;
- SQLAlchemy + Alembic;
- autenticacao com JWT;
- Swagger Authorize com OAuth2PasswordRequestForm usando `username` como e-mail;
- CRUD de GameProject / Campanhas & Cronicas;
- criacao automatica de modulos padrao de GameProject;
- workspace foundation com Worlds, SystemTemplates, ProjectModuleSettings e GameProject Summary;
- testes automatizados com `pytest`;
- validacao com `ruff`.

Frontend:

- ainda nao iniciado.

## Arquivos Principais Alterados

- `Docs/IdentidadeVisual/TEMAS_APROVADOS.md`
- `Docs/ControleDeProjeto/STATUS_ATUAL.md`
- `Docs/ControleDeProjeto/HISTORICO_TECNICO.md`
- `Docs/ControleDeProjeto/PROXIMAS_TAREFAS_CODEX.md`

## Temas Oficiais Consolidados

```txt
cartographer
dark_horror
humanist_futuristic
```

## Resultado Da Tarefa

- Tema Cartografo / Modelo C documentado como tema principal e padrao inicial.
- Tema Sombrio/Terror / Modelo II documentado como tema escuro atmosferico.
- Tema Futurista Humanista / Modelo II documentado como tema tecnico, elegante, espacial e humanista.
- Paleta Futurista Humanista aprovada registrada.
- Alertas incluidos para nao repetir Cartografo no Futurista Humanista.
- Alertas incluidos para nao transformar o Futurista Humanista em cyberpunk pesado.
- Notas para frontend futuro registram tokens por tema e troca por `theme_key`.

## Ultimos Testes Executados

Nenhum teste automatizado foi executado nesta tarefa, pois o escopo foi exclusivamente documental.

Ultima validacao tecnica registrada da etapa anterior:

```powershell
cd apps/api
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest
```

Resultado anterior: `ruff` passou e `pytest` passou com 25 testes.

## Proxima Tarefa Recomendada

Apos merge desta documentacao visual:

```txt
front/setup-foundation
```

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado.

## Observacoes Importantes

- Esta tarefa nao alterou backend.
- Esta tarefa nao alterou banco.
- Esta tarefa nao alterou endpoints.
- Esta tarefa nao iniciou frontend.
- Esta tarefa nao criou imagens novas.
- O frontend deve nascer com tokens preparados para `cartographer`, `dark_horror` e `humanist_futuristic`.
- O Tema Futurista Humanista nao deve repetir estetica medieval, pergaminho, mapa antigo ou paleta Cartografo.
- Toda tarefa futura do Codex deve atualizar este arquivo ao final.
