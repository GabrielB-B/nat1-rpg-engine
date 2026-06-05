export type ApiErrorPayload = {
  detail?: unknown;
  message?: unknown;
};

export class ApiError extends Error {
  details: unknown;
  status: number;

  constructor(status: number, message: string, details?: unknown) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.details = details;
  }
}

export class ApiNetworkError extends Error {
  constructor(message = "Unable to connect to the API.") {
    super(message);
    this.name = "ApiNetworkError";
  }
}

export function isApiError(error: unknown): error is ApiError {
  return error instanceof ApiError;
}

function getDetailMessage(detail: unknown) {
  if (typeof detail === "string") {
    return detail;
  }

  if (Array.isArray(detail)) {
    return detail
      .map((item) => {
        if (typeof item === "string") {
          return item;
        }

        if (item && typeof item === "object" && "msg" in item) {
          return String(item.msg);
        }

        return null;
      })
      .filter(Boolean)
      .join(" ");
  }

  return "";
}

export async function parseApiError(response: Response) {
  const fallbackMessage = `API request failed with status ${response.status}`;
  const contentType = response.headers.get("Content-Type") ?? "";

  try {
    if (contentType.includes("application/json")) {
      const payload = (await response.json()) as ApiErrorPayload;
      const detailMessage = getDetailMessage(payload.detail);

      if (detailMessage) {
        return new ApiError(response.status, detailMessage, payload.detail);
      }

      if (typeof payload.message === "string") {
        return new ApiError(response.status, payload.message, payload);
      }

      return new ApiError(response.status, fallbackMessage, payload);
    }

    const text = await response.text();
    return new ApiError(response.status, text || fallbackMessage);
  } catch {
    return new ApiError(response.status, fallbackMessage);
  }
}
