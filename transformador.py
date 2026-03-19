import pandas as pd


def limpiar_datos(datos_crudos):
    df = pd.DataFrame(datos_crudos)

    df["precio_local"] = df["price"] * 7350

    # Filtrado
    mascara = df["category"] == "electronics"

    df_filtrado = df[mascara]

    return df_filtrado
