import { ApiError, ApiNetworkError, parseApiError } from "./errors";

const fallbackBaseUrl = "http://127.0.0.1:8000/api/v1";

export const apiBaseUrl =
  import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, "") ?? fallbackBaseUrl;

type ApiAuthConfig = {
  getAccessToken?: () => string | null;
  onUnauthorized?: () => void;
};

type ApiRequestOptions = RequestInit & {
  skipAuth?: boolean;
  token?: string | null;
};

let getConfiguredAccessToken: () => string | null = () => null;
let onUnauthorizedResponse: (() => void) | null = null;

export { ApiError, ApiNetworkError };

export function configureApiClient(config: ApiAuthConfig) {
  getConfiguredAccessToken = config.getAccessToken ?? (() => null);
  onUnauthorizedResponse = config.onUnauthorized ?? null;

  return () => {
    getConfiguredAccessToken = () => null;
    onUnauthorizedResponse = null;
  };
}

function shouldDefaultToJson(body: BodyInit | null | undefined) {
  return body !== undefined && body !== null && !(body instanceof FormData) && !(body instanceof URLSearchParams);
}

function shouldReadJson(response: Response) {
  const contentType = response.headers.get("Content-Type") ?? "";
  return contentType.includes("application/json");
}

export async function apiRequest<TResponse>(
  path: string,
  options: ApiRequestOptions = {}
): Promise<TResponse> {
  const { skipAuth = false, token, headers, ...requestOptions } = options;
  const requestHeaders = new Headers(headers);
  const accessToken = token ?? (!skipAuth ? getConfiguredAccessToken() : null);

  if (!requestHeaders.has("Content-Type") && shouldDefaultToJson(requestOptions.body)) {
    requestHeaders.set("Content-Type", "application/json");
  }

  if (accessToken) {
    requestHeaders.set("Authorization", `Bearer ${accessToken}`);
  }

  let response: Response;

  try {
    response = await fetch(`${apiBaseUrl}${path}`, {
      ...requestOptions,
      headers: requestHeaders
    });
  } catch (error) {
    if (error instanceof Error) {
      throw new ApiNetworkError(error.message);
    }

    throw new ApiNetworkError();
  }

  if (!response.ok) {
    const apiError = await parseApiError(response);

    if (apiError.status === 401 && !skipAuth) {
      onUnauthorizedResponse?.();
    }

    throw apiError;
  }

  if (response.status === 204) {
    return undefined as TResponse;
  }

  if (!shouldReadJson(response)) {
    return undefined as TResponse;
  }

  return (await response.json()) as TResponse;
}
