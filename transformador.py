import pandas as pd

# Simulación de datos extraídos
datos_compras = [
    {"id_compra": 101, "id_producto": 1, "cliente": "Ana", "cantidad": 2},
    {"id_compra": 102, "id_producto": 2, "cliente": "Luis", "cantidad": 1},
    {"id_compra": 103, "id_producto": 1, "cliente": "Carlos", "cantidad": 1},
]

datos_productos = [
    {"id_producto": 1, "nombre_item": "Laptop X", "precio_usd": 1200},
    {"id_producto": 2, "nombre_item": "Mouse Inalámbrico", "precio_usd": 25},
    {"id_producto": 3, "nombre_item": "Teclado Mecánico", "precio_usd": 85},
]


def limpiar_datos(datos_crudos):
    df = pd.DataFrame(datos_crudos)

    df["precio_local"] = df["price"] * 7350

    # Filtrado
    mascara = df["category"] == "electronics"

    df_filtrado = df[mascara]

    return df_filtrado


def generar_reporte_ventas(datos_compras, datos_productos):
    compras = pd.DataFrame(datos_compras)
    productos = pd.DataFrame(datos_productos)

    df_union = pd.merge(compras, productos, on="id_producto", how="inner")
    df_union["total_pagado"] = df_union["cantidad"] * df_union["precio_usd"]
    return df_union


print(generar_reporte_ventas(datos_compras, datos_productos))
