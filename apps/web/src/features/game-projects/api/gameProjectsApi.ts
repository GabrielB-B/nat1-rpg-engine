import { apiRequest } from "../../../lib/api/client";
import { withQueryParams } from "../../../lib/api/http";
import type {
  GameProject,
  GameProjectListItem,
  GameProjectSummary,
  ListGameProjectsParams,
  ProjectModuleSetting
} from "../types";

export function getGameProjects(params: ListGameProjectsParams = {}) {
  return apiRequest<GameProjectListItem[]>(
    withQueryParams("/game-projects", {
      include_archived: params.includeArchived
    })
  );
}

export function getGameProject(projectId: string) {
  return apiRequest<GameProject>(`/game-projects/${projectId}`);
}

export function getGameProjectModules(projectId: string) {
  return apiRequest<ProjectModuleSetting[]>(`/game-projects/${projectId}/modules`);
}

export function getGameProjectSummary(projectId: string) {
  return apiRequest<GameProjectSummary>(`/game-projects/${projectId}/summary`);
}
