const authTokenKey = "nat1.auth.access_token";

function canUseStorage() {
  return typeof window !== "undefined" && "localStorage" in window;
}

export function getStoredAuthToken() {
  if (!canUseStorage()) {
    return null;
  }

  return window.localStorage.getItem(authTokenKey);
}

export function storeAuthToken(token: string) {
  if (!canUseStorage()) {
    return;
  }

  window.localStorage.setItem(authTokenKey, token);
}

export function clearStoredAuthToken() {
  if (!canUseStorage()) {
    return;
  }

  window.localStorage.removeItem(authTokenKey);
}
