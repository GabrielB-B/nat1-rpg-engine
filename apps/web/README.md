# Nat 1 Web

Frontend foundation for Nat 1 RPG Engine.

This stage starts `apps/web` with React, TypeScript, Vite, Tailwind CSS, React Router and TanStack Query. The current interface also includes the first visual design system foundation for the Cartographer theme and a mocked "Workspace do Mestre" dashboard shell.

It does not implement complete login, real CRUD flows, real backend consumption, AI, upload, players or advanced maps yet.

The visual shell uses `lucide-react` for lightweight interface icons.

## Requirements

- Node.js 22+
- npm 10+

## Setup

```powershell
cd apps/web
npm install
Copy-Item .env.example .env
```

Check `.env`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

## Run

```powershell
npm run dev
```

Default local URL:

```txt
http://127.0.0.1:5173
```

## Build And Typecheck

```powershell
npm run typecheck
npm run build
```

Preview a production build:

```powershell
npm run preview
```

## Folder Structure

```txt
src/
  app/          App shell, router and providers
  assets/       Static frontend assets
  components/   Shared UI, layout and dashboard components
  data/         Temporary mock data for visual shell
  features/     Future feature modules
  layouts/      Route layouts
  lib/          API client and shared libraries
  pages/        Route pages
  styles/       Global CSS and theme tokens
```

## API Client

`src/lib/api/client.ts` exposes a small `fetch` wrapper using:

```txt
VITE_API_BASE_URL
```

The default fallback is:

```txt
http://127.0.0.1:8000/api/v1
```

## Themes

Theme tokens live in:

```txt
src/styles/themes.css
```

Official theme keys:

- `cartographer`
- `dark_horror`
- `humanist_futuristic`

The app starts with:

```txt
data-theme="cartographer"
```

Future theme switching should update `data-theme` on the document root. Components should consume CSS variables instead of hardcoding a single visual direction.

## Design System Foundation

Current reusable components:

- `Button`
- `Card`
- `Badge`
- `Sidebar`
- `Topbar`
- `ModuleNavItem`
- `StatCard`
- `DashboardSection`
- `CampaignCard`
- `SessionList`
- `RecentNotes`
- `NpcList`
- `MapPreview`

Mock workspace data lives in:

```txt
src/data/mockWorkspace.ts
```

This file is intentionally isolated so future API integration can replace mock data without reshaping the dashboard components.

The current sidebar menu is a visual mock for the global Home do Mestre. The future campaign-internal menu should be generated from backend `ProjectModuleSettings`, using the real campaign modules: Resumo, Sessoes, Cenas, Personagens & Criaturas, Locais / Atlas, Organizacoes & Faccoes, Documentos, Notas, Relacoes and Configuracoes.

## Notes

- The current `HomePage` is a mocked visual shell for the Home do Mestre.
- Sidebar buttons, search and dashboard actions are visual only in this stage.
- No real API request is made by the dashboard yet.
- The Cartographer dashboard is intentionally compact and should stay close to the approved reference: narrow sidebar, small stats, horizontal active campaign card, side sessions and lower NPC/map/notes cards.
- ESLint is intentionally left for a later frontend quality pass.
