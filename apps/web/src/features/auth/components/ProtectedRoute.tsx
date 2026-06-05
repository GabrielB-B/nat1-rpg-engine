import { Navigate, Outlet, useLocation } from "react-router-dom";

import { useAuth } from "../AuthContext";

export function ProtectedRoute() {
  const { status } = useAuth();
  const location = useLocation();

  if (status === "loading") {
    return (
      <main className="auth-route-status" aria-live="polite">
        Validando sessão...
      </main>
    );
  }

  if (status === "anonymous") {
    return <Navigate replace state={{ from: location }} to="/login" />;
  }

  return <Outlet />;
}
