import { Archive, BookOpenCheck, Compass, Plus } from "lucide-react";

import { Button } from "../../../components/ui/Button";

const ICON_STROKE = 1.75;

type GameProjectsEmptyStateProps = {
  actionLabel?: string;
  description?: string;
  onCreate?: () => void;
  onSecondaryAction?: () => void;
  secondaryActionLabel?: string;
  subtitle?: string;
  title?: string;
  variant?: "welcome" | "compact";
};

export function GameProjectsEmptyState({
  actionLabel = "Criar primeira campanha",
  description = "Registre nome, formato, sistema, tom e uma descrição inicial. Depois, o Nat 1 ajuda a organizar sessões, personagens, notas e mapas.",
  onCreate,
  onSecondaryAction,
  secondaryActionLabel,
  subtitle = "Crie sua primeira campanha e transforme uma ideia em mundo jogável.",
  title = "Toda mesa lendária começou com uma página em branco.",
  variant = "welcome"
}: GameProjectsEmptyStateProps) {
  const className = `projects-empty-state projects-empty-state--${variant}`;

  if (variant === "compact") {
    return (
      <section className={className} aria-labelledby="projects-empty-title">
        <span className="projects-empty-compact-icon" aria-hidden="true">
          <BookOpenCheck className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
        </span>
        <div className="projects-empty-copy">
          <p className="section-kicker">Biblioteca arquivada</p>
          <h2 id="projects-empty-title">{title}</h2>
          <p>{description}</p>
        </div>
        {onCreate ? (
          <Button onClick={onCreate}>
            <Plus className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            {actionLabel}
          </Button>
        ) : null}
      </section>
    );
  }

  return (
    <section className={className} aria-labelledby="projects-empty-title">
      <div className="projects-empty-copy">
        <p className="section-kicker">Abertura da biblioteca</p>
        <h2 id="projects-empty-title">{title}</h2>
        <p className="projects-empty-lede">{subtitle}</p>
        <p className="projects-empty-description">{description}</p>
        {onCreate ? (
          <div className="projects-empty-actions">
            <Button onClick={onCreate}>
              <Plus className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
              {actionLabel}
            </Button>
            {onSecondaryAction && secondaryActionLabel ? (
              <Button onClick={onSecondaryAction} variant="secondary">
                <Archive className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
                {secondaryActionLabel}
              </Button>
            ) : null}
          </div>
        ) : null}
      </div>
      <div className="projects-empty-visual" aria-hidden="true">
        <span className="projects-empty-sigil">N1</span>
        <span className="projects-empty-compass">
          <Compass className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
        </span>
        <span className="projects-empty-marker projects-empty-marker--one" />
        <span className="projects-empty-marker projects-empty-marker--two" />
        <div className="projects-empty-tome">
          <span className="projects-empty-page projects-empty-page--left" />
          <span className="projects-empty-page projects-empty-page--right" />
          <BookOpenCheck className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
        </div>
      </div>
    </section>
  );
}
