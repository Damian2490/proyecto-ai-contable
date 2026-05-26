from fastapi import APIRouter
from app.services.tipo_cambio import obtener_tipo_cambio

router=APIRouter()

@router.get("/balance")
def obtener_balance():
    return {"balance":30}

@router.get("/calcular")
def calc_bal(ing:float,gast:float):
    return {"balance2":ing-gast}

@router.get("/cambio")
def dol2eur():
    euros=obtener_tipo_cambio()
    return {"eur":euros}