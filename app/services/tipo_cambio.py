import requests

def obtener_tipo_cambio():
    respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    datos = respuesta.json()
    return datos["rates"]["EUR"]