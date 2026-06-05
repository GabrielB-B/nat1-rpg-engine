import { ApiNetworkError, isApiError } from "../../lib/api/errors";

export function getAuthErrorMessage(error: unknown, fallback: string) {
  if (isApiError(error)) {
    if (error.status === 401) {
      return "E-mail ou senha inválidos.";
    }

    if (error.status === 409) {
      return "Já existe uma conta com este e-mail.";
    }

    if (error.status === 422) {
      return "Confira os campos e tente novamente.";
    }

    return error.message || fallback;
  }

  if (error instanceof ApiNetworkError || error instanceof TypeError) {
    return "Não foi possível conectar à API local. Confira se o backend está rodando.";
  }

  return fallback;
}
