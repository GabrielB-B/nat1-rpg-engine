# Padroes De Engenharia

Projeto: Nat 1 RPG Engine

Data de referencia: 2026-06-21

Fase relacionada: `docs/architecture-roadmap-checkpoints`

## Objetivo

Definir padrões obrigatórios para manter o Nat 1 RPG Engine legível, testável, seguro, documentado e sustentável entre fases.

## Codigo Legivel E Manutenivel

- Usar nomes claros para variáveis, funções, componentes, services, repositories e schemas.
- Manter funções pequenas e com responsabilidade explícita.
- Manter componentes React com responsabilidade única.
- Evitar componentes gigantes e arquivos com múltiplos domínios misturados.
- Isolar regra de negócio em services no backend.
- Isolar acesso a dados em repositories no backend.
- Usar schemas Pydantic para entrada e saída da API.
- Usar hooks de domínio para integração assíncrona no frontend.
- Manter helpers compartilhados em `lib` apenas quando forem realmente genéricos.
- Evitar abstrações prematuras sem repetição ou complexidade real.

## Comentarios

Comentários devem explicar decisões, regras de negócio ou trechos não óbvios.

Evitar comentários que repetem o código.

Exemplo inadequado:

```py
# incrementa contador
counter += 1
```

Exemplo adequado:

```py
# Mantém resposta genérica para evitar enumeração de e-mails no login.
raise InvalidCredentialsError()
```

## Backend

- Endpoints devem permanecer finos.
- Services concentram regras de negócio e validações de domínio.
- Repositories concentram queries e persistência.
- Schemas definem contrato público de entrada e saída.
- Models representam persistência, não fluxo de tela.
- Toda rota protegida deve validar usuário autenticado.
- Todo recurso pertencente a usuário deve aplicar isolamento por dono.
- Toda alteração de model deve ter migration Alembic quando aplicável.
- Testes devem cobrir regras de isolamento, autenticação e regressões de domínio.

## Frontend

- Páginas roteáveis ficam em `src/pages`.
- Domínios ficam em `src/features`.
- Componentes compartilhados ficam em `src/components`.
- Integrações HTTP ficam em `src/lib/api` ou em APIs de domínio.
- Dados assíncronos devem usar TanStack Query quando houver cache, loading e invalidação.
- Telas conectadas à API devem exibir loading, erro, vazio e sucesso.
- Formulários devem validar campos obrigatórios antes do envio.
- Tokens de tema devem ser consumidos via CSS variables sempre que possível.
- Estados visuais devem preservar acessibilidade básica de foco, contraste e área clicável.

## Seguranca

- Nenhum secret deve ser versionado.
- Arquivos `.env` devem permanecer fora do Git.
- Senhas devem ser armazenadas somente com hash.
- Tokens não devem aparecer em logs.
- Rotas privadas devem exigir JWT.
- Backend deve validar dados de entrada mesmo quando o frontend já valida.
- Erros para usuário não devem expor stack trace.
- Ações destrutivas devem exigir confirmação.
- Arquivamento deve ser preferido a exclusão permanente.
- Permissões e participação de jogadores devem ter fase própria antes de uso real.

## Documentacao

- Atualizar `STATUS_ATUAL.md` ao finalizar fase.
- Atualizar `HISTORICO_TECNICO.md` com data, fase, entregas, decisões e validações.
- Atualizar `PROXIMAS_TAREFAS_CODEX.md` quando a fila do MVP mudar.
- Atualizar `CHECKPOINTS.md` ao concluir fase ou alterar direção relevante.
- Registrar decisões arquiteturais em `DECISOES_TECNICAS.md`.
- Manter tom técnico, objetivo e verificável.
- Não usar tom de conversa, relatório de IA ou texto promocional.
- Não apagar histórico técnico útil.

## Branches E Git

- Usar branches por fase.
- Evitar misturar features independentes no mesmo branch.
- Validar antes de commit.
- Não fazer commit automático.
- Pull Request deve ser usado para integração na branch principal.
- `git diff --check` deve ser executado antes de finalizar alterações relevantes.
- `git status` deve ser informado no fechamento da fase.

## Validacoes

Validações recomendadas por tipo de fase:

| Tipo de fase | Validações mínimas |
| --- | --- |
| Backend | `pytest`, `ruff check .`, migrações quando aplicável. |
| Frontend | `npm.cmd run build`, `npm.cmd run dev` quando houver alteração visual ou de rota. |
| Documentação | `git diff --check`, varredura de tom documental, revisão de links e `git status`. |
| Full stack | Backend, frontend, API local e fluxo manual mínimo. |

Quando uma validação não for aplicável, o motivo deve ser documentado.

## Padrão Obrigatório Para Próximas Fases

Toda fase técnica deve:

1. Ler documentação de controle antes de alterar arquivos.
2. Identificar fase atual e branch.
3. Respeitar escopo da fase.
4. Não apagar histórico.
5. Atualizar checkpoints.
6. Atualizar status atual.
7. Atualizar próximas tarefas.
8. Documentar pendências.
9. Manter código legível e manutenível.
10. Executar validações.
11. Informar arquivos alterados.
12. Não fazer commit automático.

