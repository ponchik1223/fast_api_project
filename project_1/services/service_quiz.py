
from typing import TYPE_CHECKING
import schemas as _schemas
import requests
from database import models, repository
from fastapi import HTTPException

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


# сервис для обработки заданного количества вопросов, ответом будет последний вопрос в бд
class QuizService():
    def __init__(self, quiz_repository: models.QuizQuestion_db,  db: "Session"):
        self.quiz_repository = quiz_repository
        self.db = db
    
    async def get_question(self,
            questions_num: _schemas.Question, 
            ) -> str:
        
        questions_num = questions_num.dict()["questions_num"]
        # Получение предыдущего сохраненного вопроса
        unique_questions = repository.QuizRepository(db=self.db)
        previous_question = unique_questions.get_last_question()
        
        total_unique_questions = 0

        
        while total_unique_questions < questions_num:
            # Отправить запрос к публичному API для получения случайных вопросов
            api_url = f"https://jservice.io/api/random?count={questions_num}"
            response = requests.get(api_url)

            if response.status_code == 200:
                quiz_data = response.json()

                for question in quiz_data:
                    # отправляем вопросы в репу, возвращает 0 или 1 в зависимости от уникальности вопроса
                    total_unique_questions += unique_questions.create_quiz(question=question)
                
        return previous_question
        
        
        
        
        
