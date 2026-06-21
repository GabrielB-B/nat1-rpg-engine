import { apiRequest } from "../../../lib/api/client";
import { withQueryParams } from "../../../lib/api/http";
import type {
  CreateGameProjectPayload,
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

export function createGameProject(payload: CreateGameProjectPayload) {
  return apiRequest<GameProject>("/game-projects", {
    body: JSON.stringify(payload),
    method: "POST"
  });
}

export function archiveGameProject(projectId: string) {
  return apiRequest<GameProject>(`/game-projects/${projectId}/archive`, {
    method: "POST"
  });
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
