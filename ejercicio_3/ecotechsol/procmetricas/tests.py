import unittest
from .funcs import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):
    def test_consumo_por_defecto(self):
        consumo_kwh = 100
        factor_emision = 0.4

        resultado_esperado = consumo_kwh * factor_emision
        self.assertEqual(calcular_emisiones_carbono(consumo_kwh), resultado_esperado)

    def test_consumo_personalizado(self):
        consumo_kwh = 100
        factor_emision_personalizado = 0.3

        resultado_esperado = consumo_kwh * factor_emision_personalizado
        self.assertEqual(calcular_emisiones_carbono(consumo_kwh, factor_emision_personalizado), resultado_esperado)

    def test_consumo_cero(self):
        resultado_esperado = 0
        self.assertEqual(calcular_emisiones_carbono(0, 0.4), resultado_esperado)

    def test_consumo_decimales(self):
        resultado_esperado = 43.68

        self.assertAlmostEqual(calcular_emisiones_carbono(124.8, 0.35), resultado_esperado, places=3)
        

    def test_consumo_negativo(self):
        
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)