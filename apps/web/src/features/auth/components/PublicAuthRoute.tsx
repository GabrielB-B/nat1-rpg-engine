import { Navigate, Outlet } from "react-router-dom";

import { useAuth } from "../AuthContext";

export function PublicAuthRoute() {
  const { status } = useAuth();

  if (status === "loading") {
    return (
      <main className="auth-route-status" aria-live="polite">
        Preparando acesso...
      </main>
    );
  }

  if (status === "authenticated") {
    return <Navigate replace to="/" />;
  }

  return <Outlet />;
}
