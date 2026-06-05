export type QueryParamValue = boolean | number | string | null | undefined;

export type QueryParams = Record<string, QueryParamValue>;

export function withQueryParams(path: string, params?: QueryParams) {
  if (!params) {
    return path;
  }

  const searchParams = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value === undefined || value === null || value === "") {
      return;
    }

    searchParams.set(key, String(value));
  });

  const queryString = searchParams.toString();

  if (!queryString) {
    return path;
  }

  return `${path}?${queryString}`;
}
