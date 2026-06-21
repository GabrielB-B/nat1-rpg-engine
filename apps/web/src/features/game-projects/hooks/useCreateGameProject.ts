import { useMutation } from "@tanstack/react-query";

import { queryClient } from "../../../lib/queryClient";
import { createGameProject } from "../api/gameProjectsApi";
import type { CreateGameProjectPayload } from "../types";

export function useCreateGameProject() {
  return useMutation({
    mutationFn: (payload: CreateGameProjectPayload) => createGameProject(payload),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["game-projects"] });
    }
  });
}
