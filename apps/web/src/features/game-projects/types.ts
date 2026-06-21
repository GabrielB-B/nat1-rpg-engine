export type ProjectModuleSetting = {
  id: string;
  module_key: string;
  display_name: string;
  is_enabled: boolean;
  order_index: number;
  icon_key: string | null;
  created_at: string;
  updated_at: string;
};

export type GameProjectFormat =
  | "campaign"
  | "one_shot"
  | "mini_series"
  | "short_adventure"
  | "sandbox";

export type GameProjectStatus =
  | "preparation"
  | "active"
  | "paused"
  | "completed"
  | "archived";

export type GameProjectListItem = {
  id: string;
  owner_user_id: string;
  name: string;
  slug: string;
  format: string;
  description: string | null;
  status: string;
  system_template_id: string | null;
  world_id: string | null;
  theme: string;
  cover_image_url: string | null;
  metadata_json: Record<string, unknown>;
  created_at: string;
  updated_at: string;
  archived_at: string | null;
};

export type GameProject = GameProjectListItem & {
  module_settings: ProjectModuleSetting[];
};

export type GameProjectSummaryLinkedResource = {
  id: string;
  name: string;
};

export type GameProjectSummaryCounts = {
  sessions_count: number;
  scenes_count: number;
  characters_creatures_count: number;
  locations_count: number;
  organizations_factions_count: number;
  documents_count: number;
  notes_count: number;
  relationships_count: number;
};

export type GameProjectSummary = {
  id: string;
  name: string;
  slug: string;
  format: string;
  description: string | null;
  status: string;
  theme: string;
  archived_at: string | null;
  world: GameProjectSummaryLinkedResource | null;
  system_template: GameProjectSummaryLinkedResource | null;
  active_modules: ProjectModuleSetting[];
  counters: GameProjectSummaryCounts;
};

export type ListGameProjectsParams = {
  includeArchived?: boolean;
};

export type CreateGameProjectPayload = {
  name: string;
  format: GameProjectFormat;
  description?: string;
  status?: GameProjectStatus;
  system_template_id?: string;
  world_id?: string;
  theme?: "cartographer" | "dark_horror" | "humanist_futuristic";
  cover_image_url?: string;
};
