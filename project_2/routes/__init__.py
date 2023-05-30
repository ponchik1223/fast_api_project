from fastapi import APIRouter

from .users import router as contact_router
from .audio import router as audio_router

router = APIRouter()

router.include_router(contact_router, prefix="/contact", tags=["contact"])
router.include_router(audio_router, prefix="/audio", tags=["audio"])