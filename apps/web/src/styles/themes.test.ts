import { readFileSync } from "node:fs";
import { resolve } from "node:path";

import { describe, expect, it } from "vitest";

const REQUIRED_TOKENS = [
  "page-bg",
  "surface-1",
  "surface-2",
  "surface-raised",
  "surface-inset",
  "border-default",
  "border-strong",
  "control-border",
  "text-primary",
  "text-secondary",
  "text-disabled",
  "action-primary-bg",
  "action-primary-text",
  "action-secondary-bg",
  "action-secondary-text",
  "link",
  "focus-ring",
  "overlay",
  "status-success",
  "status-warning",
  "status-danger",
  "danger-action-bg",
  "danger-action-text",
  "disabled-bg",
  "disabled-text",
  "brand-ink",
  "brand-paper",
  "brand-hat",
  "brand-hat-shadow",
  "brand-metal",
  "brand-seal",
  "brand-accent-soft",
  "art-line",
  "map-land",
  "map-water",
  "map-route",
  "texture-opacity",
  "shadow-soft",
  "shadow-card",
  "shadow-panel",
  "font-display",
  "font-body"
] as const;

const CONTRAST_PAIRS = [
  ["text-primary", "surface-1", 4.5],
  ["text-secondary", "surface-1", 4.5],
  ["action-primary-text", "action-primary-bg", 4.5],
  ["action-secondary-text", "action-secondary-bg", 4.5],
  ["danger-action-text", "danger-action-bg", 4.5],
  ["link", "surface-1", 4.5],
  ["status-success", "surface-1", 4.5],
  ["status-warning", "surface-1", 4.5],
  ["status-danger", "surface-1", 4.5],
  ["focus-ring", "surface-1", 3],
  ["focus-ring", "page-bg", 3],
  ["control-border", "surface-1", 3],
  ["control-border", "page-bg", 3],
  ["disabled-text", "disabled-bg", 3]
] as const;

const css = readFileSync(resolve(process.cwd(), "src/styles/themes.css"), "utf8");
const globalsCss = readFileSync(
  resolve(process.cwd(), "src/styles/globals.css"),
  "utf8"
);

function parseThemes(source: string) {
  const themes = new Map<string, Map<string, string>>();
  const themePattern = /\[data-theme="([^"]+)"\]\s*\{([\s\S]*?)\n\}/g;

  for (const match of source.matchAll(themePattern)) {
    const declarations = new Map<string, string>();
    const declarationPattern = /--([\w-]+):\s*([^;]+);/g;

    for (const declaration of match[2].matchAll(declarationPattern)) {
      declarations.set(declaration[1], declaration[2].trim());
    }

    themes.set(match[1], declarations);
  }

  return themes;
}

function relativeLuminance(hex: string) {
  const channels = hex
    .slice(1)
    .match(/.{2}/g)
    ?.map((value) => Number.parseInt(value, 16) / 255);

  if (!channels || channels.length !== 3) {
    throw new Error(`Expected a six-digit hex color, received ${hex}`);
  }

  const [red, green, blue] = channels.map((channel) =>
    channel <= 0.04045
      ? channel / 12.92
      : ((channel + 0.055) / 1.055) ** 2.4
  );

  return 0.2126 * red + 0.7152 * green + 0.0722 * blue;
}

function contrastRatio(foreground: string, background: string) {
  const lighter = Math.max(
    relativeLuminance(foreground),
    relativeLuminance(background)
  );
  const darker = Math.min(
    relativeLuminance(foreground),
    relativeLuminance(background)
  );

  return (lighter + 0.05) / (darker + 0.05);
}

describe("semantic theme contract", () => {
  const themes = parseThemes(css);

  it("defines the three approved visual themes", () => {
    expect([...themes.keys()]).toEqual([
      "cartographer",
      "dark_horror",
      "humanist_futuristic"
    ]);
  });

  it.each([...themes.entries()])(
    "%s exposes every required semantic token",
    (_theme, tokens) => {
      for (const token of REQUIRED_TOKENS) {
        expect(tokens.has(token), `Missing --${token}`).toBe(true);
      }
    }
  );

  it.each([...themes.entries()])(
    "%s keeps operational color pairs above their WCAG thresholds",
    (_theme, tokens) => {
      for (const [foregroundToken, backgroundToken, minimum] of CONTRAST_PAIRS) {
        const foreground = tokens.get(foregroundToken);
        const background = tokens.get(backgroundToken);

        expect(foreground).toMatch(/^#[\da-f]{6}$/i);
        expect(background).toMatch(/^#[\da-f]{6}$/i);

        const ratio = contrastRatio(foreground!, background!);
        expect(
          ratio,
          `--${foregroundToken} on --${backgroundToken} is ${ratio.toFixed(2)}:1`
        ).toBeGreaterThanOrEqual(minimum);
      }
    }
  );

  it("uses the semantic overlay token in modal backdrops", () => {
    expect(globalsCss).toMatch(
      /\.project-form-overlay\s*\{[^}]*background:\s*var\(--overlay\);/s
    );
  });
});
