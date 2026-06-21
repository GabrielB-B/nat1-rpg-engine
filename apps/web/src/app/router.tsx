import { createBrowserRouter } from "react-router-dom";

import { PublicAuthRoute } from "../features/auth/components/PublicAuthRoute";
import { ProtectedRoute } from "../features/auth/components/ProtectedRoute";
import { AuthLayout } from "../layouts/AuthLayout";
import { RootLayout } from "../layouts/RootLayout";
import { GameProjectsPage } from "../pages/GameProjectsPage";
import { HomePage } from "../pages/HomePage";
import { LoginPage } from "../pages/LoginPage";
import { NotFoundPage } from "../pages/NotFoundPage";
import { RegisterPage } from "../pages/RegisterPage";

export const router = createBrowserRouter([
  {
    element: <PublicAuthRoute />,
    children: [
      {
        element: <AuthLayout />,
        children: [
          {
            path: "/login",
            element: <LoginPage />
          },
          {
            path: "/register",
            element: <RegisterPage />
          }
        ]
      }
    ]
  },
  {
    element: <ProtectedRoute />,
    children: [
      {
        path: "/",
        element: <RootLayout />,
        children: [
          {
            index: true,
            element: <HomePage />
          },
          {
            path: "campaigns",
            element: <GameProjectsPage />
          },
          {
            path: "*",
            element: <NotFoundPage />
          }
        ]
      }
    ]
  }
]);
