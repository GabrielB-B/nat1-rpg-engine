import { Link } from "react-router-dom";

export function NotFoundPage() {
  return (
    <section className="empty-state">
      <p className="section-kicker">404</p>
      <h1>Rota nao encontrada</h1>
      <Link className="text-link" to="/">
        Voltar para a tela inicial
      </Link>
    </section>
  );
}
