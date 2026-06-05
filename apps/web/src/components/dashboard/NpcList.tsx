import type { QuickRecord } from "../../data/mockWorkspace";

type NpcListProps = {
  records: QuickRecord[];
};

export function NpcList({ records }: NpcListProps) {
  return (
    <div className="npc-list">
      {records.map((record) => (
        <article className="npc-item" key={record.title}>
          <span className="npc-avatar" aria-hidden="true">
            {record.avatar}
          </span>
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
