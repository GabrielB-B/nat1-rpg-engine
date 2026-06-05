import { Outlet } from "react-router-dom";

export function RootLayout() {
  return (
    <div className="min-h-screen bg-background text-text">
      <div className="app-shell">
        <header className="site-header" aria-label="Topo tecnico">
          <div>
            <p className="site-kicker">MVP 1 / Frontend foundation</p>
            <span className="site-title">Nat 1</span>
          </div>
          <div className="theme-pill" aria-label="Tema atual">
            cartographer
          </div>
        </header>
        <main>
          <Outlet />
        </main>
      </div>
    </div>
  );
}
