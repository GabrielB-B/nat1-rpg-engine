import { useState, type FormEvent } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

import { getAuthErrorMessage } from "../features/auth/authErrors";
import { useAuth } from "../features/auth/AuthContext";
import { AuthFormShell } from "../features/auth/components/AuthFormShell";

type LoginLocationState = {
  from?: {
    pathname?: string;
  };
};

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function LoginPage() {
  const { login } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const locationState = location.state as LoginLocationState | null;
  const redirectTo = locationState?.from?.pathname ?? "/";

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);

    if (!email.trim() || !password) {
      setError("Preencha e-mail e senha para entrar.");
      return;
    }

    if (!emailPattern.test(email.trim())) {
      setError("Informe um e-mail válido.");
      return;
    }

    setIsSubmitting(true);

    try {
      await login({ email, password });
      navigate(redirectTo, { replace: true });
    } catch (requestError) {
      setError(
        getAuthErrorMessage(requestError, "Não foi possível entrar agora.")
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <AuthFormShell
      description="Entre para acessar sua Home do Mestre e continuar suas campanhas."
      footer={
        <>
          Ainda não tem conta? <Link to="/register">Criar conta</Link>
        </>
      }
      title="Entrar no Nat 1"
    >
      <form className="auth-form" noValidate onSubmit={handleSubmit}>
        <label className="auth-field">
          <span>E-mail</span>
          <input
            autoComplete="email"
            inputMode="email"
            onChange={(event) => setEmail(event.target.value)}
            placeholder="gabriel@email.com"
            type="email"
            value={email}
          />
        </label>

        <label className="auth-field">
          <span>Senha</span>
          <input
            autoComplete="current-password"
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Sua senha"
            type="password"
            value={password}
          />
        </label>

        {error ? (
          <p className="auth-error" role="alert">
            {error}
          </p>
        ) : null}

        <button className="button button--primary auth-submit" disabled={isSubmitting} type="submit">
          {isSubmitting ? "Entrando..." : "Entrar"}
        </button>
      </form>
    </AuthFormShell>
  );
}
