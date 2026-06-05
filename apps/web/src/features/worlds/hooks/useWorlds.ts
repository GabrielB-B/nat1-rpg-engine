import { useQuery } from "@tanstack/react-query";

import { getWorlds } from "../api/worldsApi";
import type { ListWorldsParams } from "../types";

export const worldsQueryKey = (params: ListWorldsParams = {}) =>
  ["worlds", { includeArchived: Boolean(params.includeArchived) }] as const;

export function useWorlds(params: ListWorldsParams = {}) {
  return useQuery({
    queryFn: () => getWorlds(params),
    queryKey: worldsQueryKey(params)
  });
}
