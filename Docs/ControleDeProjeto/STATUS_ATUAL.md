# Status Atual

## Identificacao

Projeto: Nat 1 RPG Engine
Fase atual: MVP 1 - Frontend Foundation
Data da ultima atualizacao: 2026-06-05
Branch atual: `front/setup-foundation`

## Tarefa Atual

Criar a fundacao inicial do frontend em `apps/web` com React, TypeScript, Vite, Tailwind CSS, React Router, TanStack Query e tokens iniciais de tema.

## Ultima Tarefa Concluida

- Frontend foundation criado com estrutura profissional, tema padrao `cartographer`, tokens CSS preparados para os tres temas oficiais e uma tela tecnica inicial para validar que o frontend esta funcionando.
- Documentacao dos temas aprovados consolidada em `Docs/IdentidadeVisual/TEMAS_APROVADOS.md`, com destaque para a correcao do Tema Futurista Humanista para evitar repeticao indevida do Cartografo.

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

Frontend iniciado nesta etapa:

- `apps/web`;
- React;
- TypeScript;
- Vite;
- Tailwind CSS;
- React Router;
- TanStack Query;
- API client base com `fetch`;
- CSS variables para `cartographer`, `dark_horror` e `humanist_futuristic`.

## Arquivos Principais Alterados

- `apps/web/package.json`
- `apps/web/package-lock.json`
- `apps/web/index.html`
- `apps/web/tsconfig.json`
- `apps/web/vite.config.ts`
- `apps/web/tailwind.config.ts`
- `apps/web/postcss.config.js`
- `apps/web/.env.example`
- `apps/web/src/app/App.tsx`
- `apps/web/src/app/router.tsx`
- `apps/web/src/app/providers.tsx`
- `apps/web/src/layouts/RootLayout.tsx`
- `apps/web/src/lib/api/client.ts`
- `apps/web/src/lib/queryClient.ts`
- `apps/web/src/pages/HomePage.tsx`
- `apps/web/src/pages/NotFoundPage.tsx`
- `apps/web/src/styles/globals.css`
- `apps/web/src/styles/themes.css`
- `apps/web/README.md`
- `README.md`
- `Docs/IdentidadeVisual/TEMAS_APROVADOS.md`
- `Docs/ControleDeProjeto/STATUS_ATUAL.md`
- `Docs/ControleDeProjeto/HISTORICO_TECNICO.md`
- `Docs/ControleDeProjeto/PROXIMAS_TAREFAS_CODEX.md`

## Resultado Da Tarefa

- `apps/web` criado.
- `npm install` executado com sucesso.
- `npm run typecheck` passou.
- `npm run build` passou.
- HomePage inicial renderiza uma tela tecnica de validacao.
- Tela inicial nao representa ainda a Home final do Mestre.
- `VITE_API_BASE_URL` documentado em `apps/web/.env.example`.
- `cartographer` e o tema inicial via `data-theme`.
- `dark_horror` e `humanist_futuristic` nasceram previstos em CSS variables.
- O tema Futurista Humanista usa paleta sci-fi elegante e nao repete o Cartografo.
- ESLint nao foi configurado nesta etapa; fica para uma tarefa futura de qualidade frontend.

## Ultimos Comandos Executados

```powershell
cd apps/web
npm install
npm run typecheck
npm run build
```

## Proxima Tarefa Recomendada

```txt
front/design-system-foundation
front/auth-pages
```

## Bloqueios Atuais

Nenhum bloqueio tecnico registrado.

## Observacoes Importantes

- Backend nao foi alterado.
- Banco nao foi alterado.
- Nenhuma migration foi criada.
- Nenhuma imagem nova foi criada.
- Login funcional completo ainda nao foi implementado no frontend.
- Dashboard completo ainda nao foi implementado.
- CRUD visual de campanhas ainda nao foi implementado.
- Toda tarefa futura do Codex deve atualizar este arquivo ao final.
