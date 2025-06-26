from fastapi import FastAPI
from src.core.routers import router as app_router

app = FastAPI(docs_url="/api/docs")
app.include_router(app_router)

