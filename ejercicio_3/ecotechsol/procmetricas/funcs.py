import pandas 

def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float =0.4) -> float:
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros: list[dict]) -> dict:

    registros_df = pandas.DataFrame(registros)

    total_global_emisiones = 0 
    valores_totales = []

    for indice, registro in registros_df.iterrows():
        try:
            emision_total = calcular_emisiones_carbono(registro["consumo_kwh"], registro["factor_emision"])
            valores_totales.append(emision_total)                                           
            total_global_emisiones+= emision_total
        except ValueError: 
            valores_totales.append(None) 

    registros_df["valores_totales"] = valores_totales

    indice_mayor_consumo = registros_df["consumo_kwh"].idxmax()
    planta_mayor_consumo = registros_df.loc[indice_mayor_consumo, "planta"]

    return {
        "total_global_emisiones": total_global_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "desglose": registros_df.to_dict(orient="records")
    }



