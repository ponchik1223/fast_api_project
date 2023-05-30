import fastapi as _fastapi
from typing import TYPE_CHECKING
import sqlalchemy.orm as _orm
import services as _services
from starlette.exceptions import HTTPException


from database.repository import AudioRepository

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = _fastapi.APIRouter()

# эндпоинт для загрузки audio
@router.post("/upload_record", response_model=str)

async def create_record(
    user_id: str,
    token_access: str,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
    audio_file: _fastapi.UploadFile = _fastapi.File(...)
    ):
    audio_service_create = _services.AudioService(audio_repository=AudioRepository, db=db)
    new_audio = audio_service_create.create_audio(audio_file=audio_file, user_id=user_id,token_access=token_access)
    try:
        return await new_audio
    except Exception:
        # Обработка ошибки конвертирования
        raise HTTPException(status_code=400, detail="Ошибка конвертирования файла, проверьте формат")

# эндпоинт для выгрузки audio
@router.get("/download_record")
async def download_record(
    id: str = _fastapi.Query(...),
    user: str = _fastapi.Query(...),
    db: _orm.Session = _fastapi.Depends(_services.get_db)
    )-> _fastapi.responses.FileResponse:

    audio_service_download = _services.AudioService(audio_repository=AudioRepository, db=db)
    audio_file = audio_service_download.download_audio(id_record=id,id_user=user)
    return await audio_file

