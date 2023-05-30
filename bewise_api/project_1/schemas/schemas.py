import datetime as _dt
import pydantic as _pydantic

# схема получение запроса 
class Question(_pydantic.BaseModel):
    questions_num: int
    
    # class Config:
    #     orm_mode = True
