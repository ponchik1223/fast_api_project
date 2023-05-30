from .models import QuizQuestion_db
from sqlalchemy.orm import Session


# репозиторий для работы с базой данных вопросов
class QuizRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_last_question(self):
        previous_question = self.db.query(QuizQuestion_db).order_by(QuizQuestion_db.created_at.desc()).first()
        
        return previous_question.question_text if previous_question else {}

    def create_quiz(self, question: str) -> int:
        total_quiz = 0
        if not self.db.query(QuizQuestion_db).filter_by(question_id=question["id"]).first():
            # Сохранение вопроса в базу данных
            db_question = QuizQuestion_db(
                  question_id=question["id"],
                  question_text=question["question"],
                  answer_text=question["answer"]
                  )
            self.db.add(db_question)
            self.db.commit()
            self.db.refresh(db_question)
            total_quiz += 1

        
        return total_quiz