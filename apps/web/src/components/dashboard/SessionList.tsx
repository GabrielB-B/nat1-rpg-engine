import { Bookmark, CalendarDays } from "lucide-react";

import type { QuickRecord } from "../../data/mockWorkspace";

const ICON_STROKE = 1.75;

type SessionListProps = {
  records: QuickRecord[];
};

export function SessionList({ records }: SessionListProps) {
  return (
    <div className="record-list">
      {records.map((record) => (
        <article className="record-item" key={record.title}>
          <span aria-hidden="true" className="record-marker">
            <CalendarDays
              className="ui-icon icon-xs"
              strokeWidth={ICON_STROKE}
            />
          </span>
          <div>
            <p>{record.meta}</p>
            <h3>{record.title}</h3>
            <span>{record.detail}</span>
          </div>
          <Bookmark
            aria-hidden="true"
            className="record-bookmark ui-icon icon-xs"
            strokeWidth={ICON_STROKE}
          />
        </article>
      ))}
    </div>
  );
}
