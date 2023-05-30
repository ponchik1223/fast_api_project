from database import SessionLocal
from uuid import uuid4

# вспомогательные функции для получения бд и генерации uuid
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_uuid() -> str:
    return str(uuid4())
