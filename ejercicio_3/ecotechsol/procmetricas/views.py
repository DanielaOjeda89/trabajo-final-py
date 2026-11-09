from django.shortcuts import render, redirect
from django.http import HttpRequest
from procmetricas import funcs 

def vista_panel_sustentabilidad(request: HttpRequest):
    registros_consumos = [
    {"planta": "Norte", "consumo_kwh": 100, "factor_emision": 0.4},
    {"planta": "Sur", "consumo_kwh": 200, "factor_emision": 0.3},
    {"planta": "Principal", "consumo_kwh": 150, "factor_emision": 0.5},
    ]

    metricas = funcs.obtener_metricas_consumo(registros_consumos)

    contexto = {"titulo": "Procesamiento de Métricas", "metricas": metricas}
    return render(request, "sustentabilidad/panel.html", contexto)