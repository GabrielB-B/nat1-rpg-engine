# Protocolo De Branches

Este protocolo define o fluxo mínimo para manter tarefas pequenas, rastreáveis e dentro do escopo.

## Padrão De Branches

Use branches por tarefa:

```txt
back/nome-da-tarefa
front/nome-da-tarefa
docs/nome-da-tarefa
chore/nome-da-tarefa
```

Exemplos:

```txt
back/auth-foundation
front/setup-foundation
docs/project-control
chore/update-dependencies
```

## Padrão De Commits

Use mensagens objetivas:

```txt
chore: ...
feat: ...
fix: ...
docs: ...
refactor: ...
test: ...
```

Exemplos:

```txt
docs: add project control workflow
feat: add health endpoint
test: add model metadata tests
```

## Validação Obrigatória Antes De Commit Backend

```powershell
cd apps/api
.\.venv\Scripts\Activate.ps1
ruff check .
pytest
```

Quando a tarefa envolver Alembic, validar também:

```powershell
alembic upgrade head --sql
```

Aplicar migration em banco real somente quando a tarefa pedir explicitamente ou Gabriel autorizar.

## Regras De Escopo

- Nenhuma tarefa do Codex deve implementar escopo fora do prompt.
- Não misturar backend, frontend e documentação na mesma branch sem necessidade explícita.
- Não iniciar frontend antes da fase aprovada.
- Não implementar IA, RAG, jogadores, chat ou mapas avançados no MVP 1 inicial.
- Não fazer commit automaticamente.

## Encerramento De Tarefa

Toda tarefa deve:

- Atualizar `Docs/ControleDeProjeto/STATUS_ATUAL.md` ao final.
- Informar o que foi alterado.
- Informar quais testes foram rodados.
- Informar o resultado dos testes.
- Informar a próxima tarefa recomendada.
