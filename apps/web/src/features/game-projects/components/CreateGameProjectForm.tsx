import { useMemo, useState, type FormEvent } from "react";
import { AlertCircle, Loader2, ScrollText, X } from "lucide-react";

import { Button } from "../../../components/ui/Button";
import { ApiNetworkError } from "../../../lib/api/client";
import { isApiError } from "../../../lib/api/errors";
import type { SystemTemplate } from "../../system-templates/types";
import type { World } from "../../worlds/types";
import { gameProjectFormatOptions, gameProjectStatusOptions } from "../presentation";
import { useCreateGameProject } from "../hooks/useCreateGameProject";
import type {
  CreateGameProjectPayload,
  GameProject,
  GameProjectFormat,
  GameProjectStatus
} from "../types";

const ICON_STROKE = 1.75;
const MAX_NAME_LENGTH = 255;
const MAX_DESCRIPTION_LENGTH = 420;
const MAX_COVER_URL_LENGTH = 2048;

const narrativeToneOptions = [
  "fantasia sombria",
  "fantasia epica",
  "terror",
  "investigacao",
  "intriga politica",
  "aventura maritima",
  "ficcao cientifica",
  "cyberpunk",
  "horror cosmico"
];

type CreateGameProjectFormProps = {
  isSupportingDataLoading: boolean;
  onCancel: () => void;
  onCreated: (project: GameProject) => void;
  systemTemplates: SystemTemplate[];
  worlds: World[];
};

type FormValues = {
  coverImageUrl: string;
  description: string;
  format: GameProjectFormat;
  name: string;
  narrativeTone: string;
  status: GameProjectStatus;
  systemTemplateId: string;
  worldId: string;
};

type FormErrors = Partial<Record<keyof FormValues, string>>;

const initialValues: FormValues = {
  coverImageUrl: "",
  description: "",
  format: "campaign",
  name: "",
  narrativeTone: "",
  status: "preparation",
  systemTemplateId: "",
  worldId: ""
};

function isSafeCoverUrl(value: string) {
  const trimmedValue = value.trim();

  if (!trimmedValue) {
    return true;
  }

  try {
    const url = new URL(trimmedValue);
    return url.protocol === "http:" || url.protocol === "https:";
  } catch {
    return false;
  }
}

function getFriendlyMutationError(error: unknown) {
  if (error instanceof ApiNetworkError) {
    return "Nao foi possivel conectar com a API. Verifique se o backend local esta em execucao.";
  }

  if (isApiError(error)) {
    if (error.status === 401) {
      return "Sessao expirada. Faca login novamente.";
    }

    if (error.status === 403 || error.status === 404) {
      return "Nao foi possivel acessar um recurso selecionado.";
    }

    if (error.status === 409) {
      return "Ja existe uma campanha com identificador semelhante. Ajuste o nome e tente novamente.";
    }

    if (error.status === 422) {
      return "Revise os campos obrigatorios antes de criar a campanha.";
    }
  }

  return "Nao foi possivel criar a campanha agora. Tente novamente em instantes.";
}

function validateValues(values: FormValues) {
  const errors: FormErrors = {};
  const trimmedName = values.name.trim();
  const trimmedDescription = values.description.trim();
  const trimmedCoverUrl = values.coverImageUrl.trim();

  if (!trimmedName) {
    errors.name = "Informe o nome da campanha.";
  } else if (trimmedName.length > MAX_NAME_LENGTH) {
    errors.name = `Use ate ${MAX_NAME_LENGTH} caracteres.`;
  }

  if (!values.format) {
    errors.format = "Escolha um formato.";
  }

  if (trimmedDescription.length > MAX_DESCRIPTION_LENGTH) {
    errors.description = `Use ate ${MAX_DESCRIPTION_LENGTH} caracteres.`;
  }

  if (trimmedCoverUrl.length > MAX_COVER_URL_LENGTH) {
    errors.coverImageUrl = `Use ate ${MAX_COVER_URL_LENGTH} caracteres.`;
  } else if (!isSafeCoverUrl(trimmedCoverUrl)) {
    errors.coverImageUrl = "Use uma URL http ou https valida.";
  }

  return errors;
}

function buildPayload(values: FormValues): CreateGameProjectPayload {
  const description = values.description.trim();
  const coverImageUrl = values.coverImageUrl.trim();

  return {
    name: values.name.trim(),
    format: values.format,
    status: values.status,
    theme: "cartographer",
    ...(description ? { description } : {}),
    ...(values.systemTemplateId ? { system_template_id: values.systemTemplateId } : {}),
    ...(values.worldId ? { world_id: values.worldId } : {}),
    ...(coverImageUrl ? { cover_image_url: coverImageUrl } : {})
  };
}

export function CreateGameProjectForm({
  isSupportingDataLoading,
  onCancel,
  onCreated,
  systemTemplates,
  worlds
}: CreateGameProjectFormProps) {
  const [values, setValues] = useState<FormValues>(initialValues);
  const [fieldErrors, setFieldErrors] = useState<FormErrors>({});
  const [formError, setFormError] = useState<string | null>(null);
  const createGameProject = useCreateGameProject();

  const sortedSystemTemplates = useMemo(
    () => [...systemTemplates].sort((first, second) => first.name.localeCompare(second.name)),
    [systemTemplates]
  );
  const sortedWorlds = useMemo(
    () => [...worlds].sort((first, second) => first.name.localeCompare(second.name)),
    [worlds]
  );

  function updateValue<K extends keyof FormValues>(key: K, value: FormValues[K]) {
    setValues((currentValues) => ({ ...currentValues, [key]: value }));
    setFieldErrors((currentErrors) => ({ ...currentErrors, [key]: undefined }));
    setFormError(null);
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const nextErrors = validateValues(values);
    setFieldErrors(nextErrors);

    if (Object.keys(nextErrors).length > 0) {
      return;
    }

    try {
      const createdProject = await createGameProject.mutateAsync(buildPayload(values));
      setValues(initialValues);
      setFormError(null);
      onCreated(createdProject);
    } catch (error) {
      setFormError(getFriendlyMutationError(error));
    }
  }

  const isCreating = createGameProject.isPending;

  return (
    <form className="create-project-form" onSubmit={handleSubmit}>
      <div className="create-project-form-header">
        <div>
          <p className="section-kicker">Ficha rapida</p>
          <h2>Criar campanha</h2>
        </div>
        <button
          aria-label="Cancelar criacao"
          className="icon-button"
          disabled={isCreating}
          onClick={onCancel}
          type="button"
        >
          <X className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
        </button>
      </div>

      {formError ? (
        <p className="form-alert" role="alert">
          <AlertCircle className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
          {formError}
        </p>
      ) : null}

      <label className="form-field">
        <span>Nome da campanha *</span>
        <input
          aria-invalid={Boolean(fieldErrors.name)}
          disabled={isCreating}
          maxLength={MAX_NAME_LENGTH}
          onChange={(event) => updateValue("name", event.target.value)}
          placeholder="As Brumas de Eldoria"
          value={values.name}
        />
        {fieldErrors.name ? <small>{fieldErrors.name}</small> : null}
      </label>

      <div className="form-grid two-columns">
        <label className="form-field">
          <span>Formato *</span>
          <select
            aria-invalid={Boolean(fieldErrors.format)}
            disabled={isCreating}
            onChange={(event) =>
              updateValue("format", event.target.value as GameProjectFormat)
            }
            value={values.format}
          >
            {gameProjectFormatOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
          {fieldErrors.format ? <small>{fieldErrors.format}</small> : null}
        </label>

        <label className="form-field">
          <span>Status</span>
          <select
            disabled={isCreating}
            onChange={(event) =>
              updateValue("status", event.target.value as GameProjectStatus)
            }
            value={values.status}
          >
            {gameProjectStatusOptions
              .filter((option) => option.value !== "archived")
              .map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
          </select>
        </label>
      </div>

      <div className="form-grid two-columns">
        <label className="form-field">
          <span>Sistema/template</span>
          <select
            disabled={isCreating || isSupportingDataLoading}
            onChange={(event) => updateValue("systemTemplateId", event.target.value)}
            value={values.systemTemplateId}
          >
            <option value="">Definir depois</option>
            {sortedSystemTemplates.map((template) => (
              <option key={template.id} value={template.id}>
                {template.name}
              </option>
            ))}
          </select>
        </label>

        <label className="form-field">
          <span>Mundo/cenario</span>
          <select
            disabled={isCreating || isSupportingDataLoading}
            onChange={(event) => updateValue("worldId", event.target.value)}
            value={values.worldId}
          >
            <option value="">Definir depois</option>
            {sortedWorlds.map((world) => (
              <option key={world.id} value={world.id}>
                {world.name}
              </option>
            ))}
          </select>
        </label>
      </div>

      <label className="form-field">
        <span>Genero/tom</span>
        <select
          disabled
          onChange={(event) => updateValue("narrativeTone", event.target.value)}
          value={values.narrativeTone}
        >
          <option value="">Planejado para fase posterior</option>
          {narrativeToneOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label className="form-field">
        <span>Descricao curta</span>
        <textarea
          disabled={isCreating}
          maxLength={MAX_DESCRIPTION_LENGTH}
          onChange={(event) => updateValue("description", event.target.value)}
          placeholder="Uma campanha de fantasia sombria sobre rotas maritimas, pactos antigos e ruinas esquecidas."
          rows={4}
          value={values.description}
        />
        <small>
          {fieldErrors.description ??
            `${values.description.trim().length}/${MAX_DESCRIPTION_LENGTH} caracteres`}
        </small>
      </label>

      <label className="form-field">
        <span>URL da capa</span>
        <input
          aria-invalid={Boolean(fieldErrors.coverImageUrl)}
          disabled={isCreating}
          maxLength={MAX_COVER_URL_LENGTH}
          onChange={(event) => updateValue("coverImageUrl", event.target.value)}
          placeholder="https://exemplo.com/mapa.jpg"
          type="url"
          value={values.coverImageUrl}
        />
        {fieldErrors.coverImageUrl ? (
          <small>{fieldErrors.coverImageUrl}</small>
        ) : (
          <small>Opcional. URLs invalidas usam o placeholder cartografico.</small>
        )}
      </label>

      <div className="create-project-form-footer">
        <Button disabled={isCreating} onClick={onCancel} type="button" variant="ghost">
          Cancelar
        </Button>
        <Button disabled={isCreating} type="submit">
          {isCreating ? (
            <Loader2 className="ui-icon icon-sm form-spinner" strokeWidth={ICON_STROKE} />
          ) : (
            <ScrollText className="ui-icon icon-sm" strokeWidth={ICON_STROKE} />
          )}
          Criar campanha
        </Button>
      </div>
    </form>
  );
}
