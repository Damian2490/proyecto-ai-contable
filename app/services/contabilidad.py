from app.database import get_connection

def calcular_balance():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT 
                   COALESCE(SUM(CASE WHEN monto > 0 THEN monto ELSE 0 END), 0) ingresos,
                   COALESCE(SUM(CASE WHEN monto < 0 THEN monto ELSE 0 END), 0) gastos,
                   COALESCE(SUM(monto), 0) balance
                   FROM transacciones;"""
                   )
    ingresos,gastos,balance=cursor.fetchone()
    cursor.close()
    conn.close()
    return {
        "ingresos": ingresos,
        "gastos": gastos,
        "balance": balance
    }
