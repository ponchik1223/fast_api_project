import datetime as _dt
import sqlalchemy as _sql
import database as _database


# модель данных для таблицы вопрос
class QuizQuestion_db(_database.Base): 
    __tablename__ = "quiz_questions"
    id = _sql.Column(_sql.Integer, primary_key=True)
    question_id = _sql.Column(_sql.Integer)
    question_text = _sql.Column(_sql.String)
    answer_text = _sql.Column(_sql.String)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.now)