from fastapi import FastAPI
from app.routes import router
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="NibblePy – Python Snippets API", version="1.0")

app.include_router(router)
