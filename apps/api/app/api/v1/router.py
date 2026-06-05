from fastapi import APIRouter

from app.api.v1.endpoints import auth, game_projects, health, system_templates, worlds

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(game_projects.router)
api_router.include_router(health.router)
api_router.include_router(system_templates.router)
api_router.include_router(worlds.router)
