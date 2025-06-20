from fastapi import FastAPI
from app.routers import auth, notes
from app import models, database

app = FastAPI()
app.include_router(auth.router)
app.include_router(notes.router)

models.Base.metadata.create_all(bind=database.engine)

