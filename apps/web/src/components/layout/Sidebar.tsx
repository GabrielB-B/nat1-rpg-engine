import { Settings } from "lucide-react";

import type { NavigationItem } from "../../data/mockWorkspace";
import { ModuleNavItem } from "./ModuleNavItem";

const ICON_STROKE = 1.75;

type SidebarProps = {
  items: NavigationItem[];
  userName: string;
};

export function Sidebar({ items, userName }: SidebarProps) {
  return (
    <aside className="sidebar" aria-label="Navegação principal">
      <div className="sidebar-brand">
        <span className="brand-sigil" aria-hidden="true">
          N1
        </span>
        <div>
          <p>Nat 1</p>
        </div>
      </div>

      <nav className="sidebar-group" aria-label="Workspace do Mestre">
        {items.map((item, index) => (
          <ModuleNavItem key={item.id} item={item} isActive={index === 0} />
        ))}
      </nav>

      <footer className="sidebar-user">
        <span className="sidebar-avatar" aria-hidden="true">
          {userName.slice(0, 1)}
        </span>
        <div>
          <strong>{userName}</strong>
          <span>Nível 12</span>
        </div>
        <button
          className="sidebar-settings"
          type="button"
          aria-label="Configurações"
        >
          <Settings
            aria-hidden="true"
            className="ui-icon icon-md"
            strokeWidth={ICON_STROKE}
          />
        </button>
      </footer>
    </aside>
  );
}
