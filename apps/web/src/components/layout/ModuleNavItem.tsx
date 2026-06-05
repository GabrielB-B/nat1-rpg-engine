import {
  BookOpen,
  CalendarDays,
  Landmark,
  LayoutDashboard,
  Library,
  LucideIcon,
  Map,
  MapPin,
  NotebookText,
  Package,
  Sparkles,
  UserRound,
  Users
} from "lucide-react";

import type { NavigationItem } from "../../data/mockWorkspace";

const ICON_STROKE = 1.75;

type ModuleNavItemProps = {
  item: NavigationItem;
  isActive?: boolean;
};

const iconMap: Record<string, LucideIcon> = {
  "book-open": BookOpen,
  "calendar-days": CalendarDays,
  landmark: Landmark,
  "layout-dashboard": LayoutDashboard,
  library: Library,
  map: Map,
  "map-pin": MapPin,
  notebook: NotebookText,
  "notebook-text": NotebookText,
  package: Package,
  pin: MapPin,
  sparkles: Sparkles,
  "user-round": UserRound,
  users: Users
};

export function ModuleNavItem({ item, isActive = false }: ModuleNavItemProps) {
  const classes = ["module-nav-item", isActive ? "is-active" : ""]
    .filter(Boolean)
    .join(" ");
  const Icon = iconMap[item.iconKey] ?? LayoutDashboard;

  return (
    <button
      aria-current={isActive ? "page" : undefined}
      className={classes}
      disabled={!item.isEnabled}
      type="button"
    >
      <span aria-hidden="true" className="module-nav-symbol">
        <Icon className="ui-icon icon-md" strokeWidth={ICON_STROKE} />
      </span>
      <span className="module-nav-copy">
        <span className="module-nav-label">{item.label}</span>
      </span>
    </button>
  );
}
