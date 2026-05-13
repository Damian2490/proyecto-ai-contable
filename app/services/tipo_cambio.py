import requests

def obtener_tipo_cambio():
    try:
        respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos["rates"]["EUR"]
        else:
            print("Error HTTP:", respuesta.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error conexión:", e)
        return None

        respuesta=requests.get("https://restcountries.com/v3.1/name/ecuador")
        datos=respuesta.json