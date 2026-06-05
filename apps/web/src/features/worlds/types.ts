export type World = {
  id: string;
  owner_user_id: string;
  name: string;
  slug: string;
  description: string | null;
  status: string;
  metadata_json: Record<string, unknown>;
  created_at: string;
  updated_at: string;
  archived_at: string | null;
};

export type ListWorldsParams = {
  includeArchived?: boolean;
};
