from fastapi import APIRouter
from fastapi import HTTPException
from app.database import get_connection

router = APIRouter()

@router.get("/transacciones",tags=["Transacciones"])
def obtener_todas_transacciones():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM transacciones")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return {
    "mensaje": "Transacciones obtenidas",
    "data": data
    }

@router.get("/transacciones/{indice}",tags=["Transacciones"])
def obtener_una_transaccion(indice:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM transacciones WHERE id=%s",(indice,))
    data=cursor.fetchone()
    cursor.close()
    conn.close()
    if not data:
        raise HTTPException(
            status_code=404,
            detail="Transacción no encontrada"
        )
    return {
    "mensaje": "Transacciones especifica",
    "data": data
    }

@router.post("/transacciones",tags=["Transacciones"])
def crear_transaccion(transaccion: dict):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO transacciones (descripcion,monto,cuenta_id) VALUES (%s,%s,%s)",
                   (transaccion["descripcion"],transaccion["monto"],transaccion["cuenta_id"])
                   )
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "mensaje": "Transacción creada",
        "data": transaccion
    }

@router.delete("/transacciones/{indice}",tags=["Transacciones"])
def eliminar_transaccion(indice: int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM transacciones WHERE id=%s",(indice,))
    eliminada=cursor.fetchone()
    cursor.execute("DELETE FROM transacciones WHERE id=%s",(indice,))
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "mensaje":"eliminada",
        "data":eliminada
    }

@router.put("/transacciones/{indice}",tags=["Transacciones"])
def modificar_transaccion(indice:int,new_data:dict):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE transacciones SET descripcion=%s,monto=%s,cuenta_id=%s WHERE id=%s",
                   (new_data["descripcion"],new_data["monto"],new_data["cuenta_id"], indice)
                   )
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "mensaje":"Transaccion actualizada",
        "data":new_data
    }