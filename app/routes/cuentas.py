from fastapi import APIRouter
from fastapi import HTTPException
from app.database import get_connection

router = APIRouter()

@router.get("/cuentas",tags=["Cuentas"])
def leer_todas_cuentas():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM cuentas")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return {"mensaje":"Cuentas actuales",
            "data":data}

@router.get("/cuentas/{indice}",tags=["Cuentas"])
def leer_una_cuenta(indice:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM cuentas WHERE id=%s",(indice,))
    data=cursor.fetchone()
    cursor.close()
    conn.close()
    if not data:
        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada"
        )
    return {"mensaje":"Cuenta especifica",
            "data":data}

@router.post("/cuentas",tags=["Cuentas"])
def crear_cuentas(cuenta_nueva:dict):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO cuentas (nombre,tipo) VALUES (%s,%s)",(cuenta_nueva["nombre"],cuenta_nueva["tipo"]))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje":"Cuenta creada",
            "data":cuenta_nueva}

@router.delete("/cuentas/{indice}",tags=["Cuentas"])
def eliminar_cuenta(indice:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM cuentas WHERE id=%s",(indice,))
    eliminada=cursor.fetchone()
    if not eliminada:
        raise HTTPException(status_code=404,detail="Cuenta no encontrada")
    cursor.execute("DELETE FROM cuentas WHERE id=%s",(indice,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje":"Cuenta eliminada",
            "data":eliminada}

@router.put("/cuentas/{indice}",tags=["Cuentas"])
def editar_cuenta(indice:int,modificacion:dict):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE cuentas SET nombre=%s,tipo=%s WHERE id=%s",
                   (modificacion["nombre"],modificacion["tipo"],indice)
                   )
    if cursor.rowcount==0:
        raise HTTPException(status_code=404,detail="Cuenta no encontrada")
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje":"Cuenta modificada",
            "data":modificacion}

@router.get("/transaccionesxcuenta",tags=["Cuentas"])
def transacciones_por_cuenta():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT c.nombre, COUNT(t.id)
                   FROM cuentas c
                   LEFT JOIN transacciones t
                   ON c.id=t.cuenta_id
                   GROUP BY c.nombre;""")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return {"mensaje":"Transacciones por cuenta",
            "data":data}

@router.get("/cuentas/tipo/{tipo}",tags=["Cuentas"])
def cuentas_por_tipo(tipo:str):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM cuentas WHERE tipo=%s",(tipo,))
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return {"mensaje":"Cuentas por tipo",
            "data":data}

@router.get("/resumen-cuentas",tags=["Cuentas"])
def resumen_cuentas():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT tipo,COUNT(*) 
                   FROM cuentas 
                   GROUP BY tipo;""")
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return {"mensaje":"Resumen de cuentas por tipo",
            "data":data}