from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="NibblePy – Python Snippets API", version="1.0")

app.include_router(router)
