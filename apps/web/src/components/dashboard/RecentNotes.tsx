import { FileText } from "lucide-react";

import type { QuickRecord } from "../../data/mockWorkspace";

const ICON_STROKE = 1.75;

type RecentNotesProps = {
  records: QuickRecord[];
};

export function RecentNotes({ records }: RecentNotesProps) {
  return (
    <div className="note-stack">
      {records.map((record) => (
        <article className="note-card" key={record.title}>
          <FileText
            aria-hidden="true"
            className="ui-icon icon-sm"
            strokeWidth={ICON_STROKE}
          />
          <div>
            <h3>{record.title}</h3>
            <p>{record.meta}</p>
            <span>{record.detail}</span>
          </div>
        </article>
      ))}
    </div>
  );
}
