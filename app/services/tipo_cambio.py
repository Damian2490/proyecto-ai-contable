import requests

def obtener_tipo_cambio():
    try:
        respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/USD",timeout=3)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos["rates"]["EUR"]
        else:
            print("Error HTTP:", respuesta.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error conexión:", e)
        return None
    except requests.exceptions.Timeout:
        print("La solicitud tardó demasiado")
