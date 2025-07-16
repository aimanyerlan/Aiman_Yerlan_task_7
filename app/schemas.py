from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    text: str

class NoteUpdate(BaseModel):
    text: str

class NoteOut(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True