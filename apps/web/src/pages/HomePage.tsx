const foundationItems = [
  {
    label: "Backend foundation",
    status: "concluido",
    detail: "FastAPI, PostgreSQL, SQLAlchemy e Alembic"
  },
  {
    label: "Auth foundation",
    status: "concluido",
    detail: "JWT, Swagger Authorize e usuario atual"
  },
  {
    label: "GameProject CRUD",
    status: "concluido",
    detail: "Campanhas & Cronicas com modulos padrao"
  },
  {
    label: "Workspace foundation",
    status: "concluido",
    detail: "Worlds, SystemTemplates, modulos e summary"
  },
  {
    label: "Frontend foundation",
    status: "em andamento",
    detail: "React, Vite, Tailwind e temas aprovados"
  }
];

const themeKeys = ["cartographer", "dark_horror", "humanist_futuristic"];

export function HomePage() {
  return (
    <section className="home-grid">
      <div className="intro-panel">
        <p className="section-kicker">Workspace do mestre</p>
        <h1>Nat 1 RPG Engine</h1>
        <p className="intro-copy">
          Ferramenta para mestres organizarem campanhas, cronicas e mundos
          vivos.
        </p>
        <div className="theme-row" aria-label="Temas preparados">
          {themeKeys.map((themeKey) => (
            <span key={themeKey} className="theme-chip">
              {themeKey}
            </span>
          ))}
        </div>
      </div>

      <div className="status-board" aria-label="Estado tecnico da fundacao">
        {foundationItems.map((item, index) => (
          <article className="status-card" key={item.label}>
            <span className="status-index">{String(index + 1).padStart(2, "0")}</span>
            <div>
              <h2>{item.label}</h2>
              <p>{item.detail}</p>
            </div>
            <strong>{item.status}</strong>
          </article>
        ))}
      </div>
    </section>
  );
}
