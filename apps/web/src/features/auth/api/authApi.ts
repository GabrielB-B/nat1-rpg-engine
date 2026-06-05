import { apiRequest } from "../../../lib/api/client";
import type {
  AuthToken,
  AuthUser,
  LoginCredentials,
  RegisterPayload
} from "../types";

export function login(credentials: LoginCredentials) {
  const body = new URLSearchParams();
  body.set("username", credentials.email.trim().toLowerCase());
  body.set("password", credentials.password);

  return apiRequest<AuthToken>("/auth/login", {
    body,
    method: "POST",
    skipAuth: true
  });
}

export function register(payload: RegisterPayload) {
  return apiRequest<AuthUser>("/auth/register", {
    body: JSON.stringify({
      email: payload.email.trim().toLowerCase(),
      name: payload.name.trim(),
      password: payload.password
    }),
    method: "POST",
    skipAuth: true
  });
}

export function getCurrentUser(token?: string) {
  return apiRequest<AuthUser>("/auth/me", {
    method: "GET",
    token
  });
}
