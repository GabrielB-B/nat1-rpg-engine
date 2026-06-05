import { useQuery } from "@tanstack/react-query";

import { getGameProjects } from "../api/gameProjectsApi";
import type { ListGameProjectsParams } from "../types";

export const gameProjectsQueryKey = (params: ListGameProjectsParams = {}) =>
  ["game-projects", { includeArchived: Boolean(params.includeArchived) }] as const;

export function useGameProjects(params: ListGameProjectsParams = {}) {
  return useQuery({
    queryFn: () => getGameProjects(params),
    queryKey: gameProjectsQueryKey(params)
  });
}
