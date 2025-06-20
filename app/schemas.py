from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    role: str 
    class Config:
        from_attributes = True

class NoteBase(BaseModel):
    text: str

class NoteCreate(BaseModel):
    pass 

class NoteUpdate(BaseModel):
    pass 

class NoteOut(BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True