from fastapi import APIRouter
from app.api.controllers import movies_controller

router = APIRouter()

router.include_router(movies_controller.router)
