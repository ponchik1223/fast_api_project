from typing import TYPE_CHECKING
import fastapi as _fastapi
import schemas as _schemas
import sqlalchemy.orm as _orm
import services as _service
from database.repository import QuizRepository


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = _fastapi.APIRouter()


# эндпоинт для обработки вопросов
@router.post("/quiz_question")
async def get_question(
     questions_num: _schemas.Question, 
     db: _orm.Session = _fastapi.Depends(_service.get_db),
     ): 
              
        if questions_num.questions_num < 0:
              raise _fastapi.HTTPException(status_code=422, detail="Указано отрицательное число")     
        
        quiz_service_download_answer = _service.QuizService(quiz_repository=QuizRepository, db=db)
        return await quiz_service_download_answer.get_question(questions_num=questions_num)
 