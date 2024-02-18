import unittest
from main import Dia

class TestDia(unittest.TestCase):
    def test_valores_predeterminados(self):
        # Prueba para verificar si los valores personalizados se establecen correctamente
        d = Dia()
        self.assertEqual(d.anyo, 1970)
        self.assertEqual(d.mes, 1)
        self.assertEqual(d.dia, 1)

    def test_valores_personalizados(self):
        # Prueba para verificar si los valores personalizados se establecen correctamente
        d = Dia(1970, 4, 7)
        self.assertEqual(d.anyo, 1970)
        self.assertEqual(d.mes, 4)
        self.assertEqual(d.dia, 7)

    def test_es_bisiesto(self):
        # Prueba para verificar si el método es_bisiesto() funciona correctamente
        self.assertTrue(Dia(2020).es_bisiesto()) 
        # Año no bisiesto
        self.assertFalse(Dia(2021).es_bisiesto())
        # Año no bisiesto divisible por 100 pero no por 400
        self.assertFalse(Dia(1900).es_bisiesto())
        # Año bisiesto divisible por 100 y por 400
        self.assertTrue(Dia(2000).es_bisiesto())

    def test_dias_x_mes(self):
        # Prueba para verificar si el método mes_X_dia() devuelve el número correcto de días en un mes
        d = Dia(1970, 4)
        d1 = Dia(2024, 2)
        d2 = Dia(2023, 12)
        # 
        self.assertEqual(d.mes_X_dia(), 30)
        self.assertEqual(d1.mes_X_dia(), 29)
        self.assertEqual(d2.mes_X_dia(), 31)
    
    def test_ajustar_mes_anyo(self):
        # Prueba para verificar si el método ajustar_mes_anyo() ajusta correctamente el mes y el año
        d = Dia(1970, 2, 1)
        d.ajustar_mes_anyo() 
        self.assertEqual((d.anyo, d.mes), (1969, 14))
        
    def test_calcular_dia_semana(self):
        # Prueba para verificar si el método calcular_dia_semana() devuelve el día de la semana correcto
        d = Dia(1900, 3, 12)
        d2 = Dia(1999, 3, 12)
        d3 = Dia(2000, 3, 12)
        d4 = Dia(2012, 2, 12)
      
        d.calcular_dia_semana()
        d2.calcular_dia_semana()
        d3.calcular_dia_semana()
        d4.calcular_dia_semana()
       
        self.assertEqual(d.calcular_dia_semana(),2)
        self.assertEqual(d2.calcular_dia_semana(),6)
        self.assertEqual(d3.calcular_dia_semana(),1)
        self.assertEqual(d4.calcular_dia_semana(),1)