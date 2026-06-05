import type { ReactNode } from "react";

type AuthFormShellProps = {
  children: ReactNode;
  description: string;
  footer: ReactNode;
  title: string;
};

export function AuthFormShell({
  children,
  description,
  footer,
  title
}: AuthFormShellProps) {
  return (
    <section className="auth-form-shell" aria-labelledby="auth-form-title">
      <header className="auth-form-header">
        <p>Conta Nat 1</p>
        <h1 id="auth-form-title">{title}</h1>
        <span>{description}</span>
      </header>
      {children}
      <footer className="auth-form-footer">{footer}</footer>
    </section>
  );
}
