import type { ReactNode } from "react";

import { Sidebar } from "../components/layout/Sidebar";
import { Topbar } from "../components/layout/Topbar";
import { workspaceMock } from "../data/mockWorkspace";

type AppShellProps = {
  children: ReactNode;
};

export function AppShell({ children }: AppShellProps) {
  return (
    <div className="app-shell">
      <Sidebar
        items={workspaceMock.navigation}
        userName={workspaceMock.userName}
      />
      <div className="workspace-frame">
        <Topbar />
        <main className="workspace-main">{children}</main>
      </div>
    </div>
  );
}
