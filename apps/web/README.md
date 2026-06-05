# Nat 1 Web

Frontend foundation for Nat 1 RPG Engine.

This stage starts `apps/web` with React, TypeScript, Vite, Tailwind CSS, React Router and TanStack Query. It does not implement complete login, the final Home do Mestre, visual CRUD flows or full backend integration yet.

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
  components/   Shared UI components
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

## Notes

- The current `HomePage` is a technical validation screen only.
- It is not the final Home do Mestre.
- ESLint is intentionally left for a later frontend quality pass.
