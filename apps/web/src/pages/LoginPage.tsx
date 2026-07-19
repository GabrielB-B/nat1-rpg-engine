import { useRef, useState, type FormEvent } from "react";
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
const formErrorId = "login-form-error";

type LoginField = "email" | "password";

export function LoginPage() {
  const { login } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [invalidFields, setInvalidFields] = useState<LoginField[]>([]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  const locationState = location.state as LoginLocationState | null;
  const redirectTo = locationState?.from?.pathname ?? "/";

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    setInvalidFields([]);

    if (!email.trim() || !password) {
      const nextInvalidFields: LoginField[] = [];

      if (!email.trim()) nextInvalidFields.push("email");
      if (!password) nextInvalidFields.push("password");

      setInvalidFields(nextInvalidFields);
      setError("Preencha e-mail e senha para entrar.");
      (nextInvalidFields[0] === "email" ? emailRef : passwordRef).current?.focus();
      return;
    }

    if (!emailPattern.test(email.trim())) {
      setInvalidFields(["email"]);
      setError("Informe um e-mail válido.");
      emailRef.current?.focus();
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
            aria-describedby={invalidFields.includes("email") ? formErrorId : undefined}
            aria-invalid={invalidFields.includes("email")}
            autoCapitalize="none"
            autoComplete="email"
            inputMode="email"
            name="email"
            onChange={(event) => setEmail(event.target.value)}
            placeholder="gabriel@email.com"
            ref={emailRef}
            spellCheck={false}
            type="email"
            value={email}
          />
        </label>

        <label className="auth-field">
          <span>Senha</span>
          <input
            aria-describedby={invalidFields.includes("password") ? formErrorId : undefined}
            aria-invalid={invalidFields.includes("password")}
            autoComplete="current-password"
            name="password"
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Sua senha"
            ref={passwordRef}
            type="password"
            value={password}
          />
        </label>

        {error ? (
          <p className="auth-error" id={formErrorId} role="alert">
            {error}
          </p>
        ) : null}

        <button className="button button--primary auth-submit" disabled={isSubmitting} type="submit">
          {isSubmitting ? "Entrando…" : "Entrar"}
        </button>
      </form>
    </AuthFormShell>
  );
}
