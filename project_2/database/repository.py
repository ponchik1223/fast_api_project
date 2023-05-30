from .models import Audio, Contact
from sqlalchemy.orm import Session

# добавление данных в таблицу contact
class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, id_name: str, token: str, name: str) -> Contact:
        user = Contact(
            id_name=id_name, 
            name=name, 
            token=token)
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
# добавление/выгрузка данных в/из таблицы audio   
class AudioRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def upload_audio(self,id_audio: str, url_audio: str,user_id: str,token_access: str, path_audio: str):
        add_audio = Audio(
            id_audio=id_audio,
            url_audio=url_audio,
            user_id=user_id,
            token_access=token_access,
            path_audio=path_audio
        )
        self.db.add(add_audio)
        self.db.commit()
        self.db.refresh(add_audio)
        
        return add_audio.url_audio
    
    def download_audio(self, user_id: str, id_audio: str):

        audio_record_path = self.db.query(Audio).filter(
        Audio.user_id == user_id,
        Audio.id_audio == id_audio
    ).first()
        
        return audio_record_path.path_audio


    

