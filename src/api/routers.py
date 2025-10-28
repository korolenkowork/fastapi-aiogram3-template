from fastapi import APIRouter

from src.api.controllers.start import router as start_router


def get_apps_router():
    router = APIRouter()
    router.include_router(start_router)
    return router
