import {
  Bell,
  Compass,
  LogOut,
  Plus,
  Search,
  Settings,
  Sparkles
} from "lucide-react";
import { useNavigate } from "react-router-dom";

import { useAuth } from "../../features/auth/AuthContext";
import { Button } from "../ui/Button";

const ICON_STROKE = 1.75;

export function Topbar() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate("/login", { replace: true });
  }

  return (
    <header className="topbar" aria-label="Topo do workspace">
      <form
        className="topbar-search"
        onSubmit={(event) => event.preventDefault()}
        role="search"
      >
        <Search
          aria-hidden="true"
          className="ui-icon icon-md"
          strokeWidth={ICON_STROKE}
        />
        <input
          aria-label="Buscar no workspace"
          placeholder="Buscar em tudo..."
          type="search"
        />
      </form>

      <div className="topbar-actions">
        <button className="icon-button" type="button" aria-label="Explorar">
          <Compass
            aria-hidden="true"
            className="ui-icon icon-md"
            strokeWidth={ICON_STROKE}
          />
        </button>
        <button className="icon-button" type="button" aria-label="Notificações">
          <Bell
            aria-hidden="true"
            className="ui-icon icon-md"
            strokeWidth={ICON_STROKE}
          />
        </button>
        <button className="icon-button" type="button" aria-label="Sugestões">
          <Sparkles
            aria-hidden="true"
            className="ui-icon icon-md"
            strokeWidth={ICON_STROKE}
          />
        </button>
        <Button variant="primary">
          <Plus
            aria-hidden="true"
            className="ui-icon icon-sm"
            strokeWidth={ICON_STROKE}
          />
          Nova sessão
        </Button>
        <button className="icon-button" type="button" aria-label="Configurações">
          <Settings
            aria-hidden="true"
            className="ui-icon icon-md"
            strokeWidth={ICON_STROKE}
          />
        </button>
        <button
          className="icon-button"
          type="button"
          aria-label="Sair"
          onClick={handleLogout}
        >
          <LogOut
            aria-hidden="true"
            className="ui-icon icon-md"
            strokeWidth={ICON_STROKE}
          />
        </button>
      </div>
    </header>
  );
}
