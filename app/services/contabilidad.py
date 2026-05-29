from app.routes.transacciones import transacciones

def calcular_balance():
    ingresos = 0
    gastos = 0
    for transaccion in transacciones:
        if "descripcion" not in transaccion:
            continue                          #error no existe descripcion
        if not isinstance(transaccion["descripcion"],str):
            continue                          #error descripcion no es tipo str
        if transaccion["descripcion"]=="":
            continue                          #error descripcion esta vacia
        if "monto" not in transaccion:
            continue                          #error monto no existe
        if not isinstance(transaccion["monto"],(int,float)):
            continue                          #error monto no es tipo numero
        if transaccion["monto"] > 0:
            ingresos += transaccion["monto"]
        else:
            gastos += transaccion["monto"]
    return {
        "ingresos": ingresos,
        "gastos": gastos,
        "balance": ingresos + gastos
    }
