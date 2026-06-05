import { useQuery } from "@tanstack/react-query";

import { getGameProjectSummary } from "../api/gameProjectsApi";

export const gameProjectSummaryQueryKey = (projectId: string | null | undefined) =>
  ["game-projects", projectId, "summary"] as const;

export function useGameProjectSummary(projectId: string | null | undefined) {
  return useQuery({
    enabled: Boolean(projectId),
    queryFn: () => getGameProjectSummary(projectId as string),
    queryKey: gameProjectSummaryQueryKey(projectId)
  });
}
