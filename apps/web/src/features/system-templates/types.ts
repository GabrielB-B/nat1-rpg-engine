export type SystemTemplate = {
  id: string;
  owner_user_id: string | null;
  name: string;
  slug: string;
  type: string;
  description: string | null;
  is_builtin: boolean;
  metadata_json: Record<string, unknown>;
  created_at: string;
  updated_at: string;
  archived_at: string | null;
};

export type ListSystemTemplatesParams = {
  includeArchived?: boolean;
};
