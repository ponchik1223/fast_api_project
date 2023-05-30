import pydantic as _pydantic


class UserCreateContact(_pydantic.BaseModel):
    name: str

class UserResponseContact(_pydantic.BaseModel):
    id_name: str
    token: str
    
    class Config:
        orm_mode = True
    