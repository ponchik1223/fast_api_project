from typing import TYPE_CHECKING
import os
from pydub import AudioSegment
from .settings import *
import fastapi as _fastapi
from .utils import generate_uuid
from database.repository import AudioRepository

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# сервис для работы с audio 
class AudioService():
    def __init__(self, audio_repository: AudioRepository, db: "Session"):
        self.user_repository = audio_repository
        self.db = db

    # получение данных (вместе с audio) их конвертирования и сохранения в бд 
    async def create_audio(self,
            user_id: str,
            token_access: str,
            audio_file: _fastapi.UploadFile
            ) -> str:


        if not os.path.exists(UPLOADED_FILES_PATH):
            os.makedirs(UPLOADED_FILES_PATH)
        
        # генерируем uuid для нашей записи
        id_audio = generate_uuid()
        
        # сохраняем наш .wav файл для дальнейшего конвертирования (временно)
        audio_path = f'{UPLOADED_FILES_PATH}{id_audio}.wav'
        with open(audio_path, "wb") as file:
            file.write(await audio_file.read())
        
        
        # конвертируем в .mp3
        audio_mp3_path = f'{UPLOADED_FILES_PATH}{id_audio}.mp3'
        audio = AudioSegment.from_wav(audio_path)
        audio.export(audio_mp3_path, format="mp3")
        
        # удаление временного файла
        os.remove(audio_path)
        
        audio_repo = AudioRepository(self.db)

        download_url = f"http://localhost:9000/audio/download_record?id={id_audio}&user={user_id}"
        
        add_audio = audio_repo.upload_audio(**{
            "id_audio": id_audio,
            "url_audio" : download_url,
            "user_id": user_id,
            "token_access": token_access,
            "path_audio": audio_mp3_path
        })

        return add_audio


    # выгрузка данных (по ссылке) из бд 
    async def download_audio(self,
            id_record: str,
            id_user: str
    ) -> _fastapi.responses.FileResponse:
        

        audio_repo_path = AudioRepository(self.db)

        audio_record = audio_repo_path.download_audio(user_id=id_user,id_audio=id_record)

        if audio_record:
            return _fastapi.responses.FileResponse(audio_record)
        else:
            raise _fastapi.HTTPException(status_code=404, detail="Файл не найден, проверьте ссылку")
