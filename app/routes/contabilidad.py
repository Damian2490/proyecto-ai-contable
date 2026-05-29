from fastapi import APIRouter
from app.services.contabilidad import calcular_balance

router = APIRouter()

@router.get("/balance", tags=["Contabilidad"])
def obtener_balance():
    return calcular_balance()