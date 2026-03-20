from extractor import extraer_productos
from transformador import limpiar_datos

url_api = "https://fakestoreapi.com/products"

datos_crudos = extraer_productos(url_api)
df_final = limpiar_datos(datos_crudos)

df_final.to_excel("reporte.xlsx", index=False)
