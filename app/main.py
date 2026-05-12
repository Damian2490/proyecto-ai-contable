import csv
from services.tipo_cambio import obtener_tipo_cambio

ingresos = 0
gastos = 0
contador = 0
conteo_gastos = 0
eur = obtener_tipo_cambio()

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
print("USD -> EUR:", eur)