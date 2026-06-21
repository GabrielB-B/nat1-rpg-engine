export type NavigationItem = {
  id: string;
  label: string;
  description: string;
  iconKey: string;
  isEnabled: boolean;
  path?: string;
};

export type WorkspaceStat = {
  iconKey: string;
  label: string;
  value: string;
  detail: string;
  tone: "primary" | "accent" | "success" | "warning";
};

export type CampaignSummary = {
  name: string;
  system: string;
  status: string;
  world: string;
  nextSession: string;
  summary: string;
  dateLabel: string;
  tags: string[];
};

export type QuickRecord = {
  avatar?: string;
  title: string;
  meta: string;
  detail: string;
};

// Mock visual da Home global do Mestre.
// Futuramente, o menu interno de uma campanha deve vir de ProjectModuleSettings
// com os modulos reais: Resumo, Sessoes, Cenas, Personagens & Criaturas,
// Locais / Atlas, Organizacoes & Faccoes, Documentos, Notas, Relacoes
// e Configuracoes.
export const workspaceMock = {
  userName: "Mestre",
  greeting: "Bem-vindo de volta, Mestre",
  subtitle: "Que histórias vamos escrever hoje?",
  activeCampaign: {
    name: "As Brumas de Eldoria",
    system: "D&D 5e",
    status: "Nível de grupo 5",
    world: "Eldoria",
    nextSession: "O Porto Cinzento",
    summary:
      "Rumores sobre navios desaparecidos voltaram a circular no Porto Cinzento. A trilha aponta para ruínas costeiras e antigos pactos ligados à linhagem dracônica de Eldoria.",
    dateLabel: "18 de Mai, 19:00",
    tags: ["Mistério", "Exploração", "Política", "Marinha"]
  } satisfies CampaignSummary,
  stats: [
    {
      iconKey: "book-open",
      label: "Campanhas",
      value: "3",
      detail: "Ativas",
      tone: "primary"
    },
    {
      iconKey: "calendar-days",
      label: "Sessões",
      value: "12",
      detail: "Realizadas",
      tone: "accent"
    },
    {
      iconKey: "users",
      label: "Personagens",
      value: "7",
      detail: "Jogadores",
      tone: "success"
    },
    {
      iconKey: "map-pin",
      label: "Locais",
      value: "48",
      detail: "Descobertos",
      tone: "primary"
    },
    {
      iconKey: "sparkles",
      label: "Sugestões de IA",
      value: "14",
      detail: "Este mês",
      tone: "warning"
    }
  ] satisfies WorkspaceStat[],
  navigation: [
    {
      id: "home",
      label: "Visão geral",
      description: "Home do mestre",
      iconKey: "layout-dashboard",
      isEnabled: true,
      path: "/"
    },
    {
      id: "campaigns",
      label: "Campanhas",
      description: "Crônicas e mesas",
      iconKey: "book-open",
      isEnabled: true,
      path: "/campaigns"
    },
    {
      id: "sessions",
      label: "Sessões",
      description: "Agenda e recaps",
      iconKey: "calendar-days",
      isEnabled: true
    },
    {
      id: "characters",
      label: "Personagens",
      description: "PJs e fichas",
      iconKey: "users",
      isEnabled: true
    },
    {
      id: "npcs",
      label: "NPCs",
      description: "Elenco vivo",
      iconKey: "user-round",
      isEnabled: true
    },
    {
      id: "locations",
      label: "Locais",
      description: "Atlas da mesa",
      iconKey: "pin",
      isEnabled: true
    },
    {
      id: "items",
      label: "Itens",
      description: "Tesouros e pistas",
      iconKey: "package",
      isEnabled: true
    },
    {
      id: "factions",
      label: "Facções",
      description: "Poder e influência",
      iconKey: "landmark",
      isEnabled: true
    },
    {
      id: "notes",
      label: "Notas",
      description: "Rascunhos rápidos",
      iconKey: "notebook-text",
      isEnabled: true
    },
    {
      id: "maps",
      label: "Mapas",
      description: "Rotas e regiões",
      iconKey: "map",
      isEnabled: true
    },
    {
      id: "compendium",
      label: "Compêndio",
      description: "Regras e lore",
      iconKey: "library",
      isEnabled: true
    },
    {
      id: "ai-master",
      label: "IA do Mestre",
      description: "Sugestões futuras",
      iconKey: "sparkles",
      isEnabled: true
    }
  ] satisfies NavigationItem[],
  sessions: [
    {
      title: "O Porto Cinzento",
      meta: "As Brumas de Eldoria",
      detail: "18 de Mai, 19:00"
    },
    {
      title: "Conselho em Valdior",
      meta: "Reinos em Conflito",
      detail: "25 de Mai, 20:00"
    },
    {
      title: "Ecos do Subterrâneo",
      meta: "Véios da Terra",
      detail: "01 de Jun, 18:00"
    }
  ] satisfies QuickRecord[],
  npcs: [
    {
      avatar: "LS",
      title: "Lady Serena",
      meta: "Nobre / Humana",
      detail: "Regente de Valdior, protege segredos sobre a linhagem real."
    },
    {
      avatar: "TM",
      title: "Thorek Marteloferro",
      meta: "Ferreiro / Anão",
      detail: "Ferreiro anão que reconheceu o metal vindo das ruínas."
    },
    {
      avatar: "VS",
      title: "Veyla Sussurro",
      meta: "Espiã / Meio-elfa",
      detail: "Informante das brumas, sempre chega antes da notícia."
    }
  ] satisfies QuickRecord[],
  notes: [
    {
      title: "História de Valdior",
      meta: "documento",
      detail: "Linha do tempo das casas nobres e do tratado costeiro."
    },
    {
      title: "Linhagem dos Dragões",
      meta: "lore",
      detail: "Nomes antigos reaparecem em mapas e juramentos esquecidos."
    },
    {
      title: "Rumores de Eldoria",
      meta: "nota rápida",
      detail: "Três pistas para inserir durante a viagem ao porto."
    }
  ] satisfies QuickRecord[],
  recentMap: {
    title: "Costa de Veldamar",
    meta: "Atualizado há 2 dias",
    detail: "Rotas marítimas e enseadas ocultas do arco costeiro."
  }
};
