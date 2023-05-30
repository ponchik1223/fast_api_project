import fastapi as _fastapi
from typing import TYPE_CHECKING
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas
from database.repository import UserRepository


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = _fastapi.APIRouter()

# эндпоинт для создания user
@router.post("/creat_contact", response_model=_schemas.UserResponseContact)
async def create_contact(
    contact: _schemas.UserCreateContact, 
    db: _orm.Session = _fastapi.Depends(_services.get_db),
    ):
     contact_service = _services.UserService(user_repository=UserRepository, db=db)
     new_contact = contact_service.create_contact(contact=contact)
     return await  new_contact
