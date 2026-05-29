from fastapi import APIRouter

router = APIRouter()

transacciones = []

@router.get("/transacciones",tags=["Transacciones"])
def obtener_transacciones():
    return transacciones

@router.post("/transacciones",tags=["Transacciones"])
def crear_transaccion(transaccion: dict):
    transacciones.append(transaccion)
    return {
        "mensaje": "Transacción creada",
        "data": transaccion
    }

@router.delete("/transacciones/{indice}",tags=["Transacciones"])
def eliminar_transaccion(indice: int):
    if indice < 0 or indice >= len(transacciones):
        return {"error": "Indice no encontrado"}
    eliminada=transacciones.pop(indice)
    return {
        "mensaje":"eliminada",
        "data":eliminada
    }

@router.put("/transacciones/{indice}",tags=["Transacciones"])
def modificar_transaccion(indice:int,nueva_transaccion:dict):
    if indice < 0 or indice >= len(transacciones):
        return {"error":"Indice no encontrado"}
    transacciones[indice]=nueva_transaccion
    return {
        "mensaje":"Transaccion actualizada",
        "data":nueva_transaccion
    }