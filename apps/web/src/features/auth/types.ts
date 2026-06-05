export type AuthToken = {
  access_token: string;
  token_type: string;
};

export type AuthUser = {
  id: string;
  name: string;
  email: string;
  is_active: boolean;
  created_at: string;
};

export type LoginCredentials = {
  email: string;
  password: string;
};

export type RegisterPayload = LoginCredentials & {
  name: string;
};

export type AuthStatus = "loading" | "authenticated" | "anonymous";
