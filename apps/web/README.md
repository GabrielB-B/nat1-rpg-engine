# Nat 1 Web

Frontend foundation for Nat 1 RPG Engine.

This stage starts `apps/web` with React, TypeScript, Vite, Tailwind CSS, React Router and TanStack Query. The current interface also includes the first visual design system foundation for the Cartographer theme, a mocked "Workspace do Mestre" dashboard shell, the initial frontend authentication flow, and the base API integration layer.

It does not implement password recovery, OAuth, permissions, real dashboard data, real CRUD flows, AI, upload, players or advanced maps yet.

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
  features/     Domain modules for auth and API integration
  layouts/      Route layouts
  lib/          API client and shared libraries
  pages/        Route pages
  styles/       Global CSS and theme tokens
```

## API Client

`src/lib/api/client.ts` exposes a typed `fetch` wrapper using:

```txt
VITE_API_BASE_URL
```

The default fallback is:

```txt
http://127.0.0.1:8000/api/v1
```

The API layer supports:

- JSON requests.
- OAuth2 form login using `application/x-www-form-urlencoded`.
- Bearer token requests through the `token` option or configured token provider.
- Automatic Authorization header for protected domain services.
- Centralized `ApiError` and `ApiNetworkError` handling.
- API validation error parsing from FastAPI `detail` payloads.
- Optional `onUnauthorized` handler for `401` responses.
- Query string creation through `withQueryParams`.

The integration files live in:

```txt
src/lib/api/
  client.ts
  errors.ts
  http.ts
```

TanStack Query is configured in:

```txt
src/lib/queryClient.ts
```

The default query policy disables refetch on window focus, keeps a short stale time, retries transient failures once, and avoids retrying `401`, `403` and `404` API responses.

## Authentication

Frontend auth lives in:

```txt
src/features/auth/
```

Implemented routes:

- `/login`
- `/register`
- `/` protected by the frontend auth guard

Implemented flow:

- Register with `POST /auth/register`.
- Login with `POST /auth/login` using OAuth2 form data where `username` is the e-mail.
- Validate the current user with `GET /auth/me`.
- Store the access token in `localStorage` under `nat1.auth.access_token`.
- Redirect unauthenticated users from `/` to `/login`.
- Redirect authenticated users away from `/login` and `/register`.
- Provide a simple logout action in the topbar.
- Clear protected query cache on logout.
- Configure the API client with the stored token and unauthorized handler.

Local API expected:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1
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
- `AuthLayout`
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

## Domain API Modules

Initial domain services and hooks are prepared for protected backend reads.

```txt
src/features/auth/
  api/authApi.ts
  hooks/useCurrentUser.ts
  types.ts

src/features/game-projects/
  api/gameProjectsApi.ts
  hooks/useGameProjects.ts
  hooks/useGameProjectSummary.ts
  types.ts

src/features/worlds/
  api/worldsApi.ts
  hooks/useWorlds.ts
  types.ts

src/features/system-templates/
  api/systemTemplatesApi.ts
  hooks/useSystemTemplates.ts
  types.ts
```

Prepared read hooks:

- `useCurrentUser`
- `useGameProjects`
- `useGameProjectSummary`
- `useWorlds`
- `useSystemTemplates`

The Home do Mestre remains mocked in this stage. The prepared hooks are available for the next product screens and controlled API integration.

## Notes

- The current `HomePage` is a mocked visual shell for the Home do Mestre.
- Sidebar buttons, search and dashboard actions are visual only in this stage.
- Auth pages consume the real local API; the dashboard still does not consume real API data.
- Domain hooks are implemented but not wired into the dashboard yet.
- The Cartographer dashboard is intentionally compact and should stay close to the approved reference: narrow sidebar, small stats, horizontal active campaign card, side sessions and lower NPC/map/notes cards.
- ESLint is intentionally left for a later frontend quality pass.
