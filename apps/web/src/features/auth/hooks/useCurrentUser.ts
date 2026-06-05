import { useQuery } from "@tanstack/react-query";

import { getStoredAuthToken } from "../authStorage";
import { getCurrentUser } from "../api/authApi";

export const currentUserQueryKey = ["auth", "current-user"] as const;

export function useCurrentUser() {
  return useQuery({
    enabled: Boolean(getStoredAuthToken()),
    queryFn: () => getCurrentUser(),
    queryKey: currentUserQueryKey
  });
}
