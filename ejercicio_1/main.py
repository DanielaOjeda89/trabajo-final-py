import pandas 
#Punto A: Normalización de Lecturas 

def limpiar_registro_sensor(registro_raw: dict) -> dict: 
    datos_df = pandas.DataFrame([registro_raw])

    datos_df["sensor_id"] = datos_df["sensor_id"].str.strip()
    datos_df["temperatura"] = datos_df["temperatura"].str.lower()
    datos_df["temperatura"] = datos_df["temperatura"].str.replace("c", "") 
    datos_df["temperatura"] = datos_df["temperatura"].str.replace(",", ".")
    datos_df["temperatura"] = datos_df["temperatura"].str.strip()
    datos_df["temperatura"] = pandas.to_numeric(datos_df["temperatura"])
    datos_df["ubicacion"] = datos_df["ubicacion"].str.strip()
    datos_df["ubicacion"] = datos_df["ubicacion"].replace(" ", pandas.NA).fillna("Planta Principal")

    return datos_df.to_dict(orient="records")[0]

#Punto B: Monitoreo y Mapeo Estadístico

def generar_resumen_sensores(lista_sensores_limpios: list[dict], umbral_temperatura: float) -> tuple:
    temperaturas_acum = 0
    ids_devol = []
    for sensor in lista_sensores_limpios:
        temperaturas_acum += sensor.get("temperatura")
        if umbral_temperatura < sensor.get("temperatura"):
            ids_devol.append(sensor.get("sensor_id"))

    promedio_temperatura = temperaturas_acum / len(lista_sensores_limpios)
    return (ids_devol, promedio_temperatura)

lista_registros = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": None
    },
    {
        "sensor_id": "SENSOR-002 ",
        "temperatura": "25.3C",
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": " SENSOR-003",
        "temperatura": "26.8C",
        "ubicacion": "Planta Sur"
    },
]

registro_normalizado = []
for registro in lista_registros:
    registro_normalizado.append(limpiar_registro_sensor(registro))


print(f"\nREPORTE DE SENSORES\n")
print("Limpieza de registros crudos de sensores:")
print(registro_normalizado)
print(f"\nResumen de sensores con temperatura mayor a 25.0: ")
print(generar_resumen_sensores(registro_normalizado, 25.0))


#Comentario: Tuve inconvenientes cuando cree la lista_registros al colocar los [] para los datos de cada diccionario,
# ya que no me funcionaba. Por lo que tuve que eliminar los [] y dejar solo {} para cada diccionario.