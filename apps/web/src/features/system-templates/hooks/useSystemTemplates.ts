import { useQuery } from "@tanstack/react-query";

import { getSystemTemplates } from "../api/systemTemplatesApi";
import type { ListSystemTemplatesParams } from "../types";

export const systemTemplatesQueryKey = (params: ListSystemTemplatesParams = {}) =>
  ["system-templates", { includeArchived: Boolean(params.includeArchived) }] as const;

export function useSystemTemplates(params: ListSystemTemplatesParams = {}) {
  return useQuery({
    queryFn: () => getSystemTemplates(params),
    queryKey: systemTemplatesQueryKey(params)
  });
}
