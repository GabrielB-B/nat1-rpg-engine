import type { HTMLAttributes, ReactNode } from "react";

type CardTone = "default" | "accent" | "quiet";

type CardProps = HTMLAttributes<HTMLDivElement> & {
  children: ReactNode;
  tone?: CardTone;
};

export function Card({
  children,
  className,
  tone = "default",
  ...props
}: CardProps) {
  const classes = ["card", `card--${tone}`, className]
    .filter(Boolean)
    .join(" ");

  return (
    <div className={classes} {...props}>
      {children}
    </div>
  );
}
