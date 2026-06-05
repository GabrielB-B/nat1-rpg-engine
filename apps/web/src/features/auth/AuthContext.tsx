import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode
} from "react";

import {
  clearStoredAuthToken,
  getStoredAuthToken,
  storeAuthToken
} from "./authStorage";
import * as authApi from "./api/authApi";
import { configureApiClient } from "../../lib/api/client";
import { queryClient } from "../../lib/queryClient";
import type {
  AuthStatus,
  AuthUser,
  LoginCredentials,
  RegisterPayload
} from "./types";

type AuthContextValue = {
  login: (credentials: LoginCredentials) => Promise<void>;
  logout: () => void;
  register: (payload: RegisterPayload) => Promise<void>;
  status: AuthStatus;
  token: string | null;
  user: AuthUser | null;
};

const AuthContext = createContext<AuthContextValue | null>(null);

type AuthProviderProps = {
  children: ReactNode;
};

export function AuthProvider({ children }: AuthProviderProps) {
  const [status, setStatus] = useState<AuthStatus>("loading");
  const [token, setToken] = useState<string | null>(() => getStoredAuthToken());
  const [user, setUser] = useState<AuthUser | null>(null);

  const logout = useCallback(() => {
    clearStoredAuthToken();
    queryClient.clear();
    setToken(null);
    setUser(null);
    setStatus("anonymous");
  }, []);

  useEffect(() => {
    return configureApiClient({
      getAccessToken: getStoredAuthToken,
      onUnauthorized: logout
    });
  }, [logout]);

  useEffect(() => {
    let isMounted = true;
    const storedToken = getStoredAuthToken();

    if (!storedToken) {
      setStatus("anonymous");
      return;
    }

    authApi
      .getCurrentUser(storedToken)
      .then((currentUser) => {
        if (!isMounted) {
          return;
        }

        setToken(storedToken);
        setUser(currentUser);
        setStatus("authenticated");
      })
      .catch(() => {
        if (!isMounted) {
          return;
        }

        clearStoredAuthToken();
        setToken(null);
        setUser(null);
        setStatus("anonymous");
      });

    return () => {
      isMounted = false;
    };
  }, []);

  const login = useCallback(async (credentials: LoginCredentials) => {
    const authToken = await authApi.login(credentials);
    const nextUser = await authApi.getCurrentUser(authToken.access_token);

    storeAuthToken(authToken.access_token);
    queryClient.clear();
    setToken(authToken.access_token);
    setUser(nextUser);
    setStatus("authenticated");
  }, []);

  const register = useCallback(async (payload: RegisterPayload) => {
    await authApi.register(payload);
    await login({ email: payload.email, password: payload.password });
  }, [login]);

  const value = useMemo<AuthContextValue>(
    () => ({
      login,
      logout,
      register,
      status,
      token,
      user
    }),
    [login, logout, register, status, token, user]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return context;
}
