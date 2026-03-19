import requests

url_api = "https://fakestoreapi.com/products"


def extraer_productos(url_api):
    try:
        respuesta = requests.get(url_api)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return []
    except requests.exceptions.RequestException:
        return []
