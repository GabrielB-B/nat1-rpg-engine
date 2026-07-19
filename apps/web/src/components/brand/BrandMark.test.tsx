import { readFileSync } from "node:fs";
import { resolve } from "node:path";

import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { BrandMark } from "./BrandMark";

function pathsFromFile(relativePath: string) {
  const source = readFileSync(resolve(process.cwd(), relativePath), "utf8");
  return [...source.matchAll(/<path\b[^>]*\sd="([^"]+)"/g)].map(
    (match) => match[1]
  );
}

function pathsFromMark(mark: HTMLElement) {
  return [...mark.querySelectorAll("path")].map((path) =>
    path.getAttribute("d")
  );
}

describe("BrandMark", () => {
  it("exposes one accessible image label by default", () => {
    render(<BrandMark variant="lockup-horizontal" />);

    const mark = screen.getByRole("img", { name: "Nat 1 RPG" });
    expect(mark).toHaveAttribute("data-brand-variant", "lockup-horizontal");
    expect(mark.querySelector("svg")).toHaveAttribute("aria-hidden", "true");
  });

  it("stays out of the accessibility tree when decorative", () => {
    const { container } = render(<BrandMark decorative variant="micro" />);

    expect(screen.queryByRole("img")).not.toBeInTheDocument();
    expect(container.firstChild).toHaveAttribute("aria-hidden", "true");
    expect(container.firstChild).toHaveAttribute("data-brand-variant", "micro");
  });

  it("supports a contextual accessible label", () => {
    render(<BrandMark label="Símbolo do Nat 1 RPG" />);

    expect(
      screen.getByRole("img", { name: "Símbolo do Nat 1 RPG" })
    ).toBeInTheDocument();
  });

  it("keeps the detailed React geometry aligned with the public SVG", () => {
    render(<BrandMark variant="symbol" />);

    expect(pathsFromMark(screen.getByRole("img"))).toEqual(
      pathsFromFile("public/brand/nat1-symbol-cartographer-candidate.svg")
    );
  });

  it("keeps the micro mark geometry aligned across React, SVG and favicon", () => {
    render(<BrandMark variant="micro" />);

    const componentPaths = pathsFromMark(screen.getByRole("img"));
    const publicPaths = pathsFromFile("public/brand/nat1-micro-mark.svg");
    const faviconPaths = pathsFromFile("public/favicon.svg");

    expect(componentPaths).toEqual(publicPaths);
    expect(faviconPaths).toEqual(publicPaths);
  });
});
