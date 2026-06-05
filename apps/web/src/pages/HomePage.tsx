import { CampaignCard } from "../components/dashboard/CampaignCard";
import { DashboardSection } from "../components/dashboard/DashboardSection";
import { MapPreview } from "../components/dashboard/MapPreview";
import { NpcList } from "../components/dashboard/NpcList";
import { RecentNotes } from "../components/dashboard/RecentNotes";
import { SessionList } from "../components/dashboard/SessionList";
import { StatCard } from "../components/dashboard/StatCard";
import { workspaceMock } from "../data/mockWorkspace";

export function HomePage() {
  return (
    <div className="workspace-dashboard">
      <section className="welcome-panel" aria-labelledby="welcome-title">
        <div className="welcome-copy">
          <h1 id="welcome-title">{workspaceMock.greeting}</h1>
          <p>{workspaceMock.subtitle}</p>
        </div>
      </section>

      <section className="stats-grid" aria-label="Resumo do workspace">
        {workspaceMock.stats.map((stat) => (
          <StatCard key={stat.label} stat={stat} />
        ))}
      </section>

      <div className="dashboard-grid">
        <CampaignCard campaign={workspaceMock.activeCampaign} />

        <DashboardSection
          actionLabel="Ver todas as sessões"
          className="sessions-panel"
          title="Próximas sessões"
        >
          <SessionList records={workspaceMock.sessions} />
        </DashboardSection>

        <DashboardSection
          actionLabel="Ver todos os NPCs"
          className="npc-panel"
          title="Últimos NPCs adicionados"
        >
          <NpcList records={workspaceMock.npcs} />
        </DashboardSection>

        <DashboardSection
          actionLabel="Ver todos os mapas"
          className="map-panel"
          title="Mapa recente"
        >
          <MapPreview {...workspaceMock.recentMap} />
        </DashboardSection>

        <DashboardSection
          actionLabel="Ver todas as notas"
          className="notes-panel"
          title="Notas recentes"
        >
          <RecentNotes records={workspaceMock.notes} />
        </DashboardSection>
      </div>
    </div>
  );
}
