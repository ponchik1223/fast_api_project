from fastapi import FastAPI
import database
from routes import router
import uvicorn


app = FastAPI()
app.include_router(router)


def _add_tables():
    return database.Base.metadata.create_all(bind=database.engine)


if __name__ == "__main__":
    _add_tables()
    uvicorn.run("start_api:app", host="127.0.0.1", port=8000, reload=True)