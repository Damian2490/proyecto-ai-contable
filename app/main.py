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
#import csv
#ingresos=0
#vectorgastos=[]
#total=0
#contador=0
#lector = csv.DictReader(open("datos.csv"))
#for fila in lector:
#    contador += 1
#    monto = float(fila["monto"])
#    total += monto
#    if monto>=0:
#        ingresos += monto
#    else:
#        vectorgastos.append(monto)
#print("Ingresos: ",ingresos,
#      "\nGastos: ",sum(vectorgastos),
#      "\nBalance total: ", total,
#      "\nPromedio de gastos: ",sum(vectorgastos)/len(vectorgastos),
#      "\nNum de transacciones: ",contador)

#-------------PROGRAMA CORREGIDO Y OPTIMIZADO
import csv

ingresos = 0
gastos = 0
contador = 0
conteo_gastos = 0

with open("C:/Users/damia/Documents/proyecto_ai_contable/data/datos.csv", newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        contador += 1
        try:
            monto = float(fila["monto"]) #intenta ejecutar este codigo
        except ValueError:
            print("dato ignorado: monto invalido") #si hay error en el dato imprime esto
            continue # luego de imprimir el mensaje la ejecucion continua no se detiene el programa
        except KeyError:
            print("dato ignorado: columna 'monto' no se encuentra")
            continue
        if monto >= 0:
            ingresos += monto
        else:
            gastos += monto
            conteo_gastos += 1
# Cálculo del balance (forma correcta en sistemas contables)
balance = round(ingresos + gastos, 2)
# Promedio de gastos con control de error de division por cero
if conteo_gastos > 0:
    promedio_gastos = round(gastos / conteo_gastos, 2)
else:
    promedio_gastos = 0
print("Ingresos: $", round(ingresos, 2))
print("Gastos: $", round(gastos, 2))
print("Balance total: $", balance)
print("Promedio de gastos: $", promedio_gastos)
print("Num de transacciones:", contador)