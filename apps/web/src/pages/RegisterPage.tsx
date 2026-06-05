import { useState, type FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";

import { getAuthErrorMessage } from "../features/auth/authErrors";
import { useAuth } from "../features/auth/AuthContext";
import { AuthFormShell } from "../features/auth/components/AuthFormShell";

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function RegisterPage() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);

    if (!name.trim() || !email.trim() || !password) {
      setError("Preencha nome, e-mail e senha para criar sua conta.");
      return;
    }

    if (!emailPattern.test(email.trim())) {
      setError("Informe um e-mail válido.");
      return;
    }

    if (password.length < 8) {
      setError("A senha precisa ter pelo menos 8 caracteres.");
      return;
    }

    setIsSubmitting(true);

    try {
      await register({ email, name, password });
      navigate("/", { replace: true });
    } catch (requestError) {
      setError(
        getAuthErrorMessage(requestError, "Não foi possível criar a conta agora.")
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <AuthFormShell
      description="Crie seu acesso para proteger campanhas, mundos e sessões futuras."
      footer={
        <>
          Já tem conta? <Link to="/login">Entrar</Link>
        </>
      }
      title="Criar conta"
    >
      <form className="auth-form" noValidate onSubmit={handleSubmit}>
        <label className="auth-field">
          <span>Nome</span>
          <input
            autoComplete="name"
            onChange={(event) => setName(event.target.value)}
            placeholder="Gabriel"
            type="text"
            value={name}
          />
        </label>

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
            autoComplete="new-password"
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Mínimo de 8 caracteres"
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
          {isSubmitting ? "Criando conta..." : "Criar conta"}
        </button>
      </form>
    </AuthFormShell>
  );
}
