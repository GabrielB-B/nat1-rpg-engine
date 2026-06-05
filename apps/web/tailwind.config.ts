import type { Config } from "tailwindcss";

export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        surface: "var(--surface)",
        "surface-raised": "var(--surface-raised)",
        border: "var(--border)",
        text: "var(--text)",
        "text-muted": "var(--text-muted)",
        primary: "var(--primary)",
        accent: "var(--accent)",
        danger: "var(--danger)",
        success: "var(--success)",
        warning: "var(--warning)"
      },
      boxShadow: {
        panel: "var(--shadow-panel)"
      },
      fontFamily: {
        display: "var(--font-display)",
        body: "var(--font-body)"
      }
    }
  },
  plugins: []
} satisfies Config;
