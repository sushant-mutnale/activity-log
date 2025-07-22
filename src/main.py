from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title='Enterprise Backend API')
app.include_router(router, prefix='/api/v1')
