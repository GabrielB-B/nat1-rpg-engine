import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import { Button } from "./Button";


describe("Button", () => {
  it("uses a safe default type and forwards interactions", () => {
    const onClick = vi.fn();

    render(<Button onClick={onClick}>Salvar campanha</Button>);
    const button = screen.getByRole("button", { name: "Salvar campanha" });

    expect(button).toHaveAttribute("type", "button");
    fireEvent.click(button);
    expect(onClick).toHaveBeenCalledOnce();
  });

  it("applies the requested semantic variant", () => {
    render(<Button variant="secondary">Cancelar</Button>);

    expect(screen.getByRole("button", { name: "Cancelar" })).toHaveClass(
      "button--secondary"
    );
  });
});
