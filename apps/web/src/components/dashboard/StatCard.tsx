import {
  BookOpen,
  CalendarDays,
  LucideIcon,
  MapPin,
  Sparkles,
  Users
} from "lucide-react";

import type { WorkspaceStat } from "../../data/mockWorkspace";
import { Card } from "../ui/Card";

const ICON_STROKE = 1.75;

type StatCardProps = {
  stat: WorkspaceStat;
};

const statIcons: Record<string, LucideIcon> = {
  "book-open": BookOpen,
  "calendar-days": CalendarDays,
  "map-pin": MapPin,
  sparkles: Sparkles,
  users: Users
};

export function StatCard({ stat }: StatCardProps) {
  const Icon = statIcons[stat.iconKey] ?? BookOpen;

  return (
    <Card className={`stat-card stat-card--${stat.tone}`}>
      <div className="stat-card-topline">
        <span className="stat-card-icon" aria-hidden="true">
          <Icon className="ui-icon icon-lg" strokeWidth={ICON_STROKE} />
        </span>
        <span className="stat-card-label">{stat.label}</span>
      </div>
      <div className="stat-card-body">
        <strong>{stat.value}</strong>
        <p>{stat.detail}</p>
      </div>
    </Card>
  );
}
