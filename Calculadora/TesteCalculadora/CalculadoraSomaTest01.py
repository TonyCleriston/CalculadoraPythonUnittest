import unittest
from Calculadora import Calculadora

class CalculadoraSomaTest(unittest.TestCase):
    def test_soma(self):
        calc = Calculadora()
        resultado = calc.soma(2, 3)
        self.assertEqual(resultado, 5)

    def test_soma2(self):
        calc = Calculadora()
        resultado = calc.soma(-2, 3)
        self.assertEqual(resultado, 1)

    def test_soma3(self):
        calc = Calculadora()
        resultado = calc.soma(-2, 2)
        self.assertTrue(resultado == 0, "Tem que dar 0")

if __name__ == '__main__':
    unittest.main()