from fastapi import FastAPI,Body
from app.routes.contabilidad import router

app = FastAPI()

app.include_router(router)