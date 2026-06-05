import { apiRequest } from "../../../lib/api/client";
import { withQueryParams } from "../../../lib/api/http";
import type { ListSystemTemplatesParams, SystemTemplate } from "../types";

export function getSystemTemplates(params: ListSystemTemplatesParams = {}) {
  return apiRequest<SystemTemplate[]>(
    withQueryParams("/system-templates", {
      include_archived: params.includeArchived
    })
  );
}

export function getSystemTemplate(templateId: string) {
  return apiRequest<SystemTemplate>(`/system-templates/${templateId}`);
}
