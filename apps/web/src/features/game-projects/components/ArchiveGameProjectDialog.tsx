import { Archive, Loader2, X } from "lucide-react";

import { Button } from "../../../components/ui/Button";
import type { GameProjectListItem } from "../types";

const ICON_STROKE = 1.75;

type ArchiveGameProjectDialogProps = {
  isArchiving: boolean;
  onCancel: () => void;
  onConfirm: () => void;
  project: GameProjectListItem;
};

export function ArchiveGameProjectDialog({
  isArchiving,
  onCancel,
  onConfirm,
  project
}: ArchiveGameProjectDialogProps) {
  return (
    <div className="project-form-overlay project-form-overlay--compact" role="presentation">
      <div
        aria-labelledby="archive-project-title"
        aria-modal="true"
        className="archive-dialog"
        role="dialog"
      >
        <button
          aria-label="Cancelar arquivamento"
          className="icon-button archive-dialog-close"
          disabled={isArchiving}
          onClick={onCancel}
          type="button"
        >
          <X className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
        </button>

        <span className="archive-dialog-icon" aria-hidden="true">
          <Archive className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
        </span>
        <div>
          <p className="section-kicker">Acao de biblioteca</p>
          <h2 id="archive-project-title">Arquivar campanha?</h2>
          <p>
            Ela será removida da biblioteca principal, mas poderá ser recuperada
            futuramente.
          </p>
          <span className="sr-only">Campanha selecionada: {project.name}</span>
        </div>

        <div className="archive-dialog-actions">
          <Button disabled={isArchiving} onClick={onCancel} type="button" variant="ghost">
            Cancelar
          </Button>
          <Button disabled={isArchiving} onClick={onConfirm} type="button">
            {isArchiving ? (
              <Loader2 className="ui-icon icon-sm form-spinner" strokeWidth={ICON_STROKE} />
            ) : (
              <Archive className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            )}
            Arquivar campanha
          </Button>
        </div>
      </div>
    </div>
  );
}
