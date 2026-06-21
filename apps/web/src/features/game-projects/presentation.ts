import type { GameProjectFormat, GameProjectStatus } from "./types";

export const gameProjectFormatOptions: Array<{
  label: string;
  value: GameProjectFormat;
}> = [
  { label: "Campanha", value: "campaign" },
  { label: "One-shot", value: "one_shot" },
  { label: "Mini-serie", value: "mini_series" },
  { label: "Aventura curta", value: "short_adventure" },
  { label: "Campanha sandbox", value: "sandbox" }
];

export const gameProjectStatusOptions: Array<{
  label: string;
  value: GameProjectStatus;
}> = [
  { label: "Em preparacao", value: "preparation" },
  { label: "Ativa", value: "active" },
  { label: "Pausada", value: "paused" },
  { label: "Concluida", value: "completed" },
  { label: "Arquivada", value: "archived" }
];

const formatLabels = new Map(
  gameProjectFormatOptions.map((option) => [option.value, option.label])
);

const statusLabels = new Map(
  gameProjectStatusOptions.map((option) => [option.value, option.label])
);

export function getGameProjectFormatLabel(format: string) {
  return formatLabels.get(format as GameProjectFormat) ?? format;
}

export function getGameProjectStatusLabel(status: string) {
  return statusLabels.get(status as GameProjectStatus) ?? status;
}

export function getGameProjectStatusTone(status: string) {
  if (status === "active") {
    return "success";
  }

  if (status === "paused" || status === "preparation") {
    return "warning";
  }

  if (status === "archived") {
    return "danger";
  }

  return "neutral";
}
