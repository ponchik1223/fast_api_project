from typing import TYPE_CHECKING
import schemas as _schemas
from .settings import *
import fastapi as _fastapi
from .utils import generate_uuid
from database.repository import UserRepository

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# сервис для создания пользователя
class UserService:

    def __init__(self, user_repository: UserRepository, db: "Session"):
        self.user_repository = user_repository
        self.db = db

    async def create_contact(self,
        contact: _schemas.UserCreateContact
        ) -> _schemas.UserResponseContact:
    
        if not contact.name:
            raise _fastapi.HTTPException(status_code=401, detail="Вы не указали имя")
        
        if ' ' in contact.name:
            raise _fastapi.HTTPException(status_code=401, detail="Укажите имя без пробела")



        contact = {
            "id_name": generate_uuid(),
            "token": generate_uuid(),
            "name": contact.dict()["name"]
        }
        create_repo = UserRepository(self.db)
        contact = create_repo.create_user(**contact)
    
        return _schemas.UserResponseContact.from_orm(contact)
