import { useMutation } from "@tanstack/react-query";

import { queryClient } from "../../../lib/queryClient";
import { archiveGameProject } from "../api/gameProjectsApi";

export function useArchiveGameProject() {
  return useMutation({
    mutationFn: (projectId: string) => archiveGameProject(projectId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["game-projects"] });
    }
  });
}
