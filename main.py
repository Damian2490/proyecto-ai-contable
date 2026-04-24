#print("Hola, este es mi proyecto de IA contable")
#ingreso=1000
#gasto=300
#balance=ingreso-gasto
#print("Balance: ",balance)
#--------------------------------------
#transacciones=[100,-50,-25,200]
#total=sum(transacciones)
#print("Total: ",total)
#--------------------------------------
#transaccion ={"descripcion":"compra supermercado","monto":-50,"categoria":"alimentacion"}
#print(transaccion["monto"])
#--------------------------------------
import csv
ingresos=0
vectorgastos=[]
total=0
contador=0
lector = csv.DictReader(open("datos.csv"))
for fila in lector:
    contador += 1
    monto = float(fila["monto"])
    total += monto
    if monto>=0:
        ingresos += monto
    else:
        vectorgastos.append(monto)
print("Ingresos: ",ingresos,
      "\nGastos: ",sum(vectorgastos),
      "\nBalance total: ", total,
      "\nPromedio de gastos: ",sum(vectorgastos)/len(vectorgastos),
      "\nNum de transacciones: ",contador)