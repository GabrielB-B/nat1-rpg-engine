type MapPreviewProps = {
  detail: string;
  meta: string;
  title: string;
};

export function MapPreview({ detail, meta, title }: MapPreviewProps) {
  return (
    <article className="map-preview">
      <div className="map-preview-art" aria-hidden="true">
        <span className="map-contour map-contour-a" />
        <span className="map-contour map-contour-b" />
        <span className="map-route map-route-a" />
        <span className="map-mountains" />
        <span className="map-settlement map-settlement-a" />
        <span className="map-compass" />
      </div>
      <div className="map-preview-copy">
        <h3>{title}</h3>
        <p>{meta}</p>
        <span>{detail}</span>
      </div>
    </article>
  );
}
