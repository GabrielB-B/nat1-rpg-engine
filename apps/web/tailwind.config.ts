import type { Config } from "tailwindcss";

export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        page: "var(--page-bg)",
        surface: "var(--surface-1)",
        "surface-2": "var(--surface-2)",
        "surface-raised": "var(--surface-raised)",
        border: "var(--border-default)",
        "border-strong": "var(--border-strong)",
        "control-border": "var(--control-border)",
        text: "var(--text-primary)",
        "text-secondary": "var(--text-secondary)",
        "text-disabled": "var(--text-disabled)",
        "action-primary": "var(--action-primary-bg)",
        "action-primary-text": "var(--action-primary-text)",
        "action-secondary": "var(--action-secondary-bg)",
        "action-secondary-text": "var(--action-secondary-text)",
        link: "var(--link)",
        focus: "var(--focus-ring)",
        danger: "var(--status-danger)",
        success: "var(--status-success)",
        warning: "var(--status-warning)"
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
