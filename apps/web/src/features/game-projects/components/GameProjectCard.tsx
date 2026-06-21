import { useEffect, useRef, useState } from "react";

import {
  Archive,
  ArrowRight,
  BookOpen,
  CalendarDays,
  Compass,
  MapPinned,
  MoreHorizontal,
  Users
} from "lucide-react";

import { Badge } from "../../../components/ui/Badge";
import { Button } from "../../../components/ui/Button";
import type { SystemTemplate } from "../../system-templates/types";
import type { World } from "../../worlds/types";
import {
  getGameProjectFormatLabel,
  getGameProjectStatusLabel,
  getGameProjectStatusTone
} from "../presentation";
import type { GameProjectListItem } from "../types";

const ICON_STROKE = 1.75;

type GameProjectCardProps = {
  canArchive?: boolean;
  isFeatured?: boolean;
  onArchive?: (project: GameProjectListItem) => void;
  project: GameProjectListItem;
  systemTemplate?: SystemTemplate;
  world?: World;
};

function isSafeCoverImageUrl(value: string | null) {
  if (!value) {
    return false;
  }

  try {
    const url = new URL(value);
    return url.protocol === "http:" || url.protocol === "https:";
  } catch {
    return false;
  }
}

function formatUpdatedAt(value: string) {
  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "Atualizacao recente";
  }

  return new Intl.DateTimeFormat("pt-BR", {
    day: "2-digit",
    month: "short",
    year: "numeric"
  }).format(date);
}

export function GameProjectCard({
  canArchive = false,
  isFeatured = false,
  onArchive,
  project,
  systemTemplate,
  world
}: GameProjectCardProps) {
  const actionMenuRef = useRef<HTMLDivElement | null>(null);
  const actionMenuTriggerRef = useRef<HTMLButtonElement | null>(null);
  const [isActionMenuOpen, setIsActionMenuOpen] = useState(false);
  const hasCoverImage = isSafeCoverImageUrl(project.cover_image_url);
  const systemLabel = systemTemplate?.name ?? "Sistema a definir";
  const worldLabel = world?.name ?? "Mundo a definir";
  const classes = [
    "project-card",
    isFeatured ? "project-card--featured" : "",
    project.archived_at ? "project-card--archived" : ""
  ]
    .filter(Boolean)
    .join(" ");

  useEffect(() => {
    if (!isActionMenuOpen) {
      return undefined;
    }

    function isOutsideMenu(target: EventTarget | null) {
      return target instanceof Node && !actionMenuRef.current?.contains(target);
    }

    function handlePointerDown(event: PointerEvent) {
      if (isOutsideMenu(event.target)) {
        setIsActionMenuOpen(false);
      }
    }

    function handleFocusIn(event: FocusEvent) {
      if (isOutsideMenu(event.target)) {
        setIsActionMenuOpen(false);
      }
    }

    function handleKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        setIsActionMenuOpen(false);
        actionMenuTriggerRef.current?.focus();
      }
    }

    document.addEventListener("pointerdown", handlePointerDown, true);
    document.addEventListener("focusin", handleFocusIn, true);
    document.addEventListener("keydown", handleKeyDown);

    return () => {
      document.removeEventListener("pointerdown", handlePointerDown, true);
      document.removeEventListener("focusin", handleFocusIn, true);
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [isActionMenuOpen]);

  function handleArchiveClick() {
    setIsActionMenuOpen(false);
    onArchive?.(project);
  }

  return (
    <article className={classes}>
      <div className="project-cover" aria-hidden={!hasCoverImage}>
        {hasCoverImage ? (
          <img alt={`Capa de ${project.name}`} src={project.cover_image_url ?? ""} />
        ) : (
          <div className="project-cover-placeholder" aria-hidden="true">
            <Compass className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
          </div>
        )}
      </div>

      <div className="project-card-body">
        <div className="project-card-topline">
          <Badge tone="accent">{getGameProjectFormatLabel(project.format)}</Badge>
          <Badge tone={getGameProjectStatusTone(project.status)}>
            {getGameProjectStatusLabel(project.status)}
          </Badge>
        </div>

        <div className="project-card-heading">
          <h2>{project.name}</h2>
          <span>Atualizada em {formatUpdatedAt(project.updated_at)}</span>
        </div>

        <p className="project-card-description">
          {project.description?.trim() ||
            "Cronica pronta para receber sessoes, cenas e personagens nas proximas fases."}
        </p>

        <div className="project-card-meta" aria-label="Dados da campanha">
          <span>
            <BookOpen className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            {systemLabel}
          </span>
          <span>
            <MapPinned className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            {worldLabel}
          </span>
          <span>
            <Users className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            Jogadores a definir
          </span>
          <span>
            <CalendarDays className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            Proxima sessao a definir
          </span>
        </div>

        <div className="project-card-footer">
          <span className="project-card-slug">/{project.slug}</span>
          <div className="project-card-actions">
            <Button disabled variant="secondary">
              Abrir campanha
              <ArrowRight className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            </Button>
            {canArchive && onArchive ? (
              <div className="project-action-menu" ref={actionMenuRef}>
                <button
                  aria-expanded={isActionMenuOpen}
                  aria-haspopup="menu"
                  aria-label={`Acoes de ${project.name}`}
                  className="project-action-menu-trigger"
                  onClick={() => setIsActionMenuOpen((isOpen) => !isOpen)}
                  ref={actionMenuTriggerRef}
                  type="button"
                >
                  <MoreHorizontal
                    className="ui-icon icon-sm"
                    strokeWidth={ICON_STROKE}
                  />
                </button>
                {isActionMenuOpen ? (
                  <div className="project-action-menu-popover" role="menu">
                    <button onClick={handleArchiveClick} role="menuitem" type="button">
                      <Archive
                        className="ui-icon icon-sm"
                        strokeWidth={ICON_STROKE}
                      />
                      Arquivar
                    </button>
                  </div>
                ) : null}
              </div>
            ) : null}
          </div>
        </div>
      </div>
    </article>
  );
}
