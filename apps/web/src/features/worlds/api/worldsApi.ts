import { apiRequest } from "../../../lib/api/client";
import { withQueryParams } from "../../../lib/api/http";
import type { ListWorldsParams, World } from "../types";

export function getWorlds(params: ListWorldsParams = {}) {
  return apiRequest<World[]>(
    withQueryParams("/worlds", {
      include_archived: params.includeArchived
    })
  );
}

export function getWorld(worldId: string) {
  return apiRequest<World>(`/worlds/${worldId}`);
}
