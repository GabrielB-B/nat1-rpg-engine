type BrandMarkVariant =
  | "symbol"
  | "micro"
  | "lockup-horizontal"
  | "lockup-vertical";

type BrandMarkProps = {
  className?: string;
  decorative?: boolean;
  label?: string;
  variant?: BrandMarkVariant;
};

function DetailedSymbol() {
  return (
    <svg
      aria-hidden="true"
      className="brand-mark__symbol"
      focusable="false"
      viewBox="0 0 160 160"
    >
      <g fill="none" strokeLinecap="round" strokeLinejoin="round">
        <circle className="brand-mark__orbit" cx="80" cy="76" r="61" />
        <circle
          className="brand-mark__orbit-detail"
          cx="80"
          cy="76"
          r="55"
        />
        <path
          className="brand-mark__cardinals"
          d="M80 3l3.4 8.6L92 15l-8.6 3.4L80 27l-3.4-8.6L68 15l8.6-3.4L80 3Zm0 122 3.4 8.6L92 137l-8.6 3.4L80 149l-3.4-8.6L68 137l8.6-3.4L80 125ZM7 76l8.6-3.4L19 64l3.4 8.6L31 76l-8.6 3.4L19 88l-3.4-8.6L7 76Zm122 0 8.6-3.4L141 64l3.4 8.6L153 76l-8.6 3.4L141 88l-3.4-8.6L129 76Z"
        />
        <path
          className="brand-mark__hat"
          d="M40 78c5-12 14-20 27-25 1-16 7-31 16-43 3 15 13 26 27 34-6 5-9 11-10 18 13 3 24 10 31 20-20 9-47 12-70 8-9-2-16-6-21-12Z"
        />
        <path
          className="brand-mark__hat-band"
          d="M53 62c20-5 43-3 58 4l-5 17c-18-5-39-5-59 1l6-22Z"
        />
        <path className="brand-mark__hat-metal" d="M57 67c18-4 36-2 50 3" />
        <path className="brand-mark__hat-highlight" d="M84 10c5 15 4 27-4 36" />
        <path
          className="brand-mark__die"
          d="M48 78h64l15 25-14 33-33 16-33-16-14-33 15-25Z"
        />
        <path
          className="brand-mark__facets"
          d="m48 78 32 20 32-20m-79 25 47-5 47 5m-80 33 33-38 33 38M48 78l-1 58m65-58 1 58M33 103l47 49 47-49"
        />
        <path
          className="brand-mark__one"
          d="m72 105 13-7v30h10v10H67v-10h9v-17l-7 4-4-8 7-2Z"
        />
      </g>
    </svg>
  );
}

function MicroSymbol() {
  return (
    <svg
      aria-hidden="true"
      className="brand-mark__symbol brand-mark__symbol--micro"
      focusable="false"
      viewBox="0 0 64 64"
    >
      <path
        className="brand-mark__die"
        d="M32 3 57 17l-3 30-22 14L10 47 7 17 32 3Z"
      />
      <path
        className="brand-mark__facets"
        d="M7 17 32 28 57 17M10 47l22-19 22 19M32 3v25m0 0v33"
      />
      <path
        className="brand-mark__one"
        d="m27 29 9-5v21h7v8H22v-8h7V36l-5 3-3-7 6-3Z"
      />
    </svg>
  );
}

export function BrandMark({
  className,
  decorative = false,
  label = "Nat 1 RPG",
  variant = "symbol"
}: BrandMarkProps) {
  const isMicro = variant === "micro";
  const isLockup = variant.startsWith("lockup");
  const classes = ["brand-mark", `brand-mark--${variant}`, className]
    .filter(Boolean)
    .join(" ");

  return (
    <span
      aria-hidden={decorative ? true : undefined}
      aria-label={decorative ? undefined : label}
      className={classes}
      data-brand-variant={variant}
      role={decorative ? undefined : "img"}
    >
      {isMicro ? <MicroSymbol /> : <DetailedSymbol />}
      {isLockup ? (
        <span className="brand-mark__wordmark" aria-hidden="true">
          <span className="brand-mark__name">
            <span>NAT</span>
            <span className="brand-mark__name-one">1</span>
            <span>RPG</span>
          </span>
          <span className="brand-mark__descriptor">RPG ENGINE</span>
        </span>
      ) : null}
    </span>
  );
}
