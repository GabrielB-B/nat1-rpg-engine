import { useRef, useState, type FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";

import { getAuthErrorMessage } from "../features/auth/authErrors";
import { useAuth } from "../features/auth/AuthContext";
import { AuthFormShell } from "../features/auth/components/AuthFormShell";

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const formErrorId = "register-form-error";

type RegisterField = "name" | "email" | "password";

export function RegisterPage() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [invalidFields, setInvalidFields] = useState<RegisterField[]>([]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const nameRef = useRef<HTMLInputElement>(null);
  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    setInvalidFields([]);

    if (!name.trim() || !email.trim() || !password) {
      const nextInvalidFields: RegisterField[] = [];

      if (!name.trim()) nextInvalidFields.push("name");
      if (!email.trim()) nextInvalidFields.push("email");
      if (!password) nextInvalidFields.push("password");

      const fieldRefs = {
        name: nameRef,
        email: emailRef,
        password: passwordRef
      };

      setInvalidFields(nextInvalidFields);
      setError("Preencha nome, e-mail e senha para criar sua conta.");
      fieldRefs[nextInvalidFields[0]].current?.focus();
      return;
    }

    if (!emailPattern.test(email.trim())) {
      setInvalidFields(["email"]);
      setError("Informe um e-mail válido.");
      emailRef.current?.focus();
      return;
    }

    if (password.length < 8) {
      setInvalidFields(["password"]);
      setError("A senha precisa ter pelo menos 8 caracteres.");
      passwordRef.current?.focus();
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
            aria-describedby={invalidFields.includes("name") ? formErrorId : undefined}
            aria-invalid={invalidFields.includes("name")}
            autoComplete="name"
            name="name"
            onChange={(event) => setName(event.target.value)}
            placeholder="Gabriel"
            ref={nameRef}
            type="text"
            value={name}
          />
        </label>

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
            autoComplete="new-password"
            name="password"
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Mínimo de 8 caracteres"
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
          {isSubmitting ? "Criando conta…" : "Criar conta"}
        </button>
      </form>
    </AuthFormShell>
  );
}
