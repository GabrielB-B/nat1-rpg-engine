import { Outlet } from "react-router-dom";

import { BrandMark } from "../components/brand/BrandMark";

export function AuthLayout() {
  return (
    <main className="auth-layout">
      <div className="auth-card">
        <aside className="auth-story" aria-label="Nat 1">
          <div className="auth-brand">
            <BrandMark
              className="auth-brand-mark"
              variant="lockup-horizontal"
            />
          </div>
          <div className="auth-story-copy">
            <p className="section-kicker">Workspace do Mestre</p>
            <h2>Continue sua campanha com clareza.</h2>
            <p>
              Organize crônicas, sessões, mapas e personagens em um espaço
              pensado para mestres que constroem mundos vivos.
            </p>
          </div>
          <ul className="auth-feature-list" aria-label="Recursos principais">
            <li>Campanhas e crônicas protegidas por conta.</li>
            <li>Base pronta para módulos privados do mestre.</li>
            <li>Tema cartográfico oficial desde o primeiro acesso.</li>
          </ul>
        </aside>

        <Outlet />
      </div>
    </main>
  );
}
