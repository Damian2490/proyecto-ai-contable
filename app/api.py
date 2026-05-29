from fastapi import FastAPI,Body
from app.routes.contabilidad import router
from app.routes.transacciones import router as transacciones_router

app = FastAPI()

app.include_router(router)
app.include_router(transacciones_router)
