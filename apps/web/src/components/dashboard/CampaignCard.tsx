import { ArrowRight, CalendarDays, MapPinned } from "lucide-react";

import type { CampaignSummary } from "../../data/mockWorkspace";
import { Badge } from "../ui/Badge";
import { Button } from "../ui/Button";
import { Card } from "../ui/Card";

const ICON_STROKE = 1.75;

type CampaignCardProps = {
  campaign: CampaignSummary;
};

export function CampaignCard({ campaign }: CampaignCardProps) {
  return (
    <Card className="campaign-card" tone="accent">
      <header className="campaign-card-header">
        <h2>Campanha ativa</h2>
      </header>

      <div className="campaign-card-map" aria-hidden="true">
        <span className="map-contour map-contour-a" />
        <span className="map-contour map-contour-b" />
        <span className="map-contour map-contour-c" />
        <span className="map-route map-route-a" />
        <span className="map-route map-route-b" />
        <span className="map-mountains" />
        <span className="map-settlement map-settlement-a" />
        <span className="map-settlement map-settlement-b" />
        <span className="map-compass" />
      </div>

      <div className="campaign-card-content">
        <div className="campaign-card-heading">
          <h3>{campaign.name}</h3>
          <Badge tone="success">{campaign.status}</Badge>
        </div>

        <div className="campaign-meta">
          <span>
            <MapPinned
              aria-hidden="true"
              className="ui-icon icon-xs"
              strokeWidth={ICON_STROKE}
            />
            Próxima sessão: {campaign.nextSession}
          </span>
          <span>
            <CalendarDays
              aria-hidden="true"
              className="ui-icon icon-xs"
              strokeWidth={ICON_STROKE}
            />
            {campaign.dateLabel}
          </span>
        </div>

        <section className="campaign-narrative" aria-label="Resumo da campanha">
          <h4>Resumo da campanha</h4>
          <p>{campaign.summary}</p>
        </section>

        <div className="campaign-card-footer">
          <div className="tag-row" aria-label="Tags da campanha">
            {campaign.tags.map((tag) => (
              <span key={tag}>{tag}</span>
            ))}
          </div>
          <Button>
            Abrir campanha
            <ArrowRight
              aria-hidden="true"
              className="ui-icon icon-sm"
              strokeWidth={ICON_STROKE}
            />
          </Button>
        </div>
      </div>
    </Card>
  );
}
