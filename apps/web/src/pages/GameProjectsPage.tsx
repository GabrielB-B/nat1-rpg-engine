import { useEffect, useMemo, useState } from "react";
import { AlertCircle, BookOpen, Loader2, Plus, ShieldAlert } from "lucide-react";

import { Button } from "../components/ui/Button";
import { ArchiveGameProjectDialog } from "../features/game-projects/components/ArchiveGameProjectDialog";
import { CreateGameProjectForm } from "../features/game-projects/components/CreateGameProjectForm";
import { GameProjectCard } from "../features/game-projects/components/GameProjectCard";
import { GameProjectsEmptyState } from "../features/game-projects/components/GameProjectsEmptyState";
import { useArchiveGameProject } from "../features/game-projects/hooks/useArchiveGameProject";
import { useGameProjects } from "../features/game-projects/hooks/useGameProjects";
import type { GameProject, GameProjectListItem } from "../features/game-projects/types";
import { useSystemTemplates } from "../features/system-templates/hooks/useSystemTemplates";
import { useWorlds } from "../features/worlds/hooks/useWorlds";

const ICON_STROKE = 1.75;
type LibraryView = "active" | "archived";
type FeedbackState = {
  message: string;
  tone: "success" | "warning";
};

export function GameProjectsPage() {
  const [isCreateFormOpen, setIsCreateFormOpen] = useState(false);
  const [libraryView, setLibraryView] = useState<LibraryView>("active");
  const [feedback, setFeedback] = useState<FeedbackState | null>(null);
  const [projectToArchive, setProjectToArchive] = useState<GameProjectListItem | null>(
    null
  );
  const gameProjectsQuery = useGameProjects({ includeArchived: true });
  const worldsQuery = useWorlds();
  const systemTemplatesQuery = useSystemTemplates();
  const archiveGameProject = useArchiveGameProject();

  const systemTemplateById = useMemo(
    () =>
      new Map(
        (systemTemplatesQuery.data ?? []).map((template) => [template.id, template])
      ),
    [systemTemplatesQuery.data]
  );
  const worldById = useMemo(
    () => new Map((worldsQuery.data ?? []).map((world) => [world.id, world])),
    [worldsQuery.data]
  );

  const allProjects = gameProjectsQuery.data ?? [];
  const activeProjects = useMemo(
    () => allProjects.filter((project) => !project.archived_at),
    [allProjects]
  );
  const archivedProjects = useMemo(
    () => allProjects.filter((project) => project.archived_at),
    [allProjects]
  );
  const projects = libraryView === "active" ? activeProjects : archivedProjects;
  const isListLoading = gameProjectsQuery.isLoading;
  const hasArchivedProjects = archivedProjects.length > 0;
  const shouldShowTopCreateButton =
    libraryView !== "active" || activeProjects.length > 0;
  const hasSupportingDataWarning = worldsQuery.isError || systemTemplatesQuery.isError;
  const shouldUseFocusedList = !isListLoading && projects.length > 0 && projects.length < 3;
  const activeEmptyTitle = hasArchivedProjects
    ? "Nenhuma campanha ativa no momento."
    : "Toda mesa lendária começou com uma página em branco.";
  const activeEmptySubtitle = hasArchivedProjects
    ? "Recupere uma crônica arquivada ou comece uma nova história para sua mesa."
    : "Crie sua primeira campanha e transforme uma ideia em mundo jogável.";
  const activeEmptyDescription = hasArchivedProjects
    ? `${archivedProjects.length} ${
        archivedProjects.length === 1 ? "crônica arquivada" : "crônicas arquivadas"
      } disponíveis na biblioteca.`
    : "Registre nome, formato, sistema, tom e uma descrição inicial. Depois, o Nat 1 ajuda a organizar sessões, personagens, notas e mapas.";
  const activeEmptyActionLabel = hasArchivedProjects
    ? "Criar nova campanha"
    : "Criar primeira campanha";

  useEffect(() => {
    if (!feedback) {
      return undefined;
    }

    const timeoutId = window.setTimeout(() => setFeedback(null), 4200);
    return () => window.clearTimeout(timeoutId);
  }, [feedback]);

  function openCreateForm() {
    setFeedback(null);
    setIsCreateFormOpen(true);
  }

  function handleProjectCreated(project: GameProject) {
    setIsCreateFormOpen(false);
    setLibraryView("active");
    setFeedback({
      message: `Campanha "${project.name}" criada com sucesso.`,
      tone: "success"
    });
  }

  function requestArchiveProject(project: GameProjectListItem) {
    setProjectToArchive(project);
    setFeedback(null);
  }

  async function confirmArchiveProject() {
    if (!projectToArchive) {
      return;
    }

    try {
      const archivedProject = await archiveGameProject.mutateAsync(projectToArchive.id);
      setProjectToArchive(null);
      setFeedback({
        message: `Campanha "${archivedProject.name}" arquivada.`,
        tone: "success"
      });
    } catch {
      setFeedback({
        message: "Nao foi possivel arquivar a campanha agora.",
        tone: "warning"
      });
    }
  }

  return (
    <div className="projects-page">
      <section className="projects-hero" aria-labelledby="projects-title">
        <div className="projects-hero-copy">
          <p className="section-kicker">Biblioteca do Mestre</p>
          <h1 id="projects-title">Campanhas & Crônicas</h1>
          <p>
            Organize seus mundos jogaveis, one-shots e campanhas em andamento.
          </p>
        </div>
        {shouldShowTopCreateButton ? (
          <Button onClick={openCreateForm}>
            <Plus className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
            Nova campanha
          </Button>
        ) : null}
      </section>

      {feedback ? (
        <p
          className={`projects-toast projects-toast--${feedback.tone}`}
          role="status"
        >
          <BookOpen className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
          {feedback.message}
        </p>
      ) : null}

      <div className="projects-toolbar" aria-label="Filtros de biblioteca">
        <div className="segmented-control" role="tablist" aria-label="Tipo de campanha">
          <button
            aria-selected={libraryView === "active"}
            className={libraryView === "active" ? "is-active" : ""}
            onClick={() => setLibraryView("active")}
            role="tab"
            type="button"
          >
            Ativas
            <span>{activeProjects.length}</span>
          </button>
          <button
            aria-selected={libraryView === "archived"}
            className={libraryView === "archived" ? "is-active" : ""}
            onClick={() => setLibraryView("archived")}
            role="tab"
            type="button"
          >
            Arquivadas
            <span>{archivedProjects.length}</span>
          </button>
        </div>
      </div>

      {hasSupportingDataWarning ? (
        <p className="projects-feedback projects-feedback--warning" role="status">
          <ShieldAlert className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
          Mundos ou sistemas nao puderam ser carregados agora. A campanha ainda pode
          ser criada com esses campos para definir depois.
        </p>
      ) : null}

      {gameProjectsQuery.isError ? (
        <section className="projects-state-card" role="alert">
          <AlertCircle className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
          <div>
            <h2>Nao foi possivel carregar as campanhas.</h2>
            <p>
              Verifique a conexao com a API local e tente novamente. Detalhes tecnicos
              nao sao exibidos nesta tela.
            </p>
          </div>
          <Button onClick={() => gameProjectsQuery.refetch()} variant="secondary">
            Tentar novamente
          </Button>
        </section>
      ) : null}

      {isListLoading ? (
        <section className="projects-state-card" aria-live="polite">
          <Loader2 className="ui-icon icon-lg form-spinner" strokeWidth={ICON_STROKE} />
          <div>
            <h2>Carregando biblioteca.</h2>
            <p>Consultando campanhas reais vinculadas a sua conta.</p>
          </div>
        </section>
      ) : null}

      {!isListLoading && !gameProjectsQuery.isError && projects.length === 0 ? (
        <div className="projects-library-layout projects-library-layout--empty">
          <GameProjectsEmptyState
            actionLabel={
              libraryView === "active" ? activeEmptyActionLabel : undefined
            }
            description={
              libraryView === "active"
                ? activeEmptyDescription
                : "Campanhas arquivadas aparecerão aqui depois que forem removidas da biblioteca principal."
            }
            onCreate={libraryView === "active" ? openCreateForm : undefined}
            onSecondaryAction={
              libraryView === "active" && hasArchivedProjects
                ? () => setLibraryView("archived")
                : undefined
            }
            secondaryActionLabel={
              libraryView === "active" && hasArchivedProjects
                ? "Ver arquivadas"
                : undefined
            }
            subtitle={
              libraryView === "active"
                ? activeEmptySubtitle
                : undefined
            }
            title={
              libraryView === "active"
                ? activeEmptyTitle
                : "Nenhuma campanha arquivada."
            }
            variant={libraryView === "active" ? "welcome" : "compact"}
          />
        </div>
      ) : null}

      {!isListLoading && projects.length > 0 ? (
        <section
          className={
            shouldUseFocusedList
              ? "projects-library-layout projects-library-layout--focused"
              : "projects-library-layout projects-library-layout--dense"
          }
          aria-label="Campanhas cadastradas"
        >
          <div
            className={
              shouldUseFocusedList ? "projects-feature-stack" : "projects-grid"
            }
          >
            {projects.map((project) => (
              <GameProjectCard
                canArchive={libraryView === "active"}
                isFeatured={shouldUseFocusedList}
                key={project.id}
                onArchive={requestArchiveProject}
                project={project}
                systemTemplate={
                  project.system_template_id
                    ? systemTemplateById.get(project.system_template_id)
                    : undefined
                }
                world={project.world_id ? worldById.get(project.world_id) : undefined}
              />
            ))}
          </div>
        </section>
      ) : null}

      {isCreateFormOpen ? (
        <div className="project-form-overlay" role="presentation">
          <div
            aria-labelledby="create-project-dialog-title"
            aria-modal="true"
            className="project-form-dialog"
            role="dialog"
          >
            <span className="sr-only" id="create-project-dialog-title">
              Criar campanha
            </span>
            <CreateGameProjectForm
              isSupportingDataLoading={
                worldsQuery.isLoading || systemTemplatesQuery.isLoading
              }
              onCancel={() => setIsCreateFormOpen(false)}
              onCreated={handleProjectCreated}
              systemTemplates={systemTemplatesQuery.data ?? []}
              worlds={worldsQuery.data ?? []}
            />
          </div>
        </div>
      ) : null}

      {projectToArchive ? (
        <ArchiveGameProjectDialog
          isArchiving={archiveGameProject.isPending}
          onCancel={() => setProjectToArchive(null)}
          onConfirm={confirmArchiveProject}
          project={projectToArchive}
        />
      ) : null}
    </div>
  );
}
