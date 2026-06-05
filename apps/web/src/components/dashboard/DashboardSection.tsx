import type { ReactNode } from "react";

type DashboardSectionProps = {
  actionLabel?: string;
  children: ReactNode;
  className?: string;
  eyebrow?: string;
  title: string;
};

export function DashboardSection({
  actionLabel,
  children,
  className,
  eyebrow,
  title
}: DashboardSectionProps) {
  const classes = ["dashboard-section", className].filter(Boolean).join(" ");

  return (
    <section className={classes}>
      <header className="dashboard-section-header">
        <h2>{title}</h2>
        {eyebrow ? <p>{eyebrow}</p> : null}
      </header>
      {children}
      {actionLabel ? (
        <button className="section-link" type="button">
          {actionLabel}
        </button>
      ) : null}
    </section>
  );
}
