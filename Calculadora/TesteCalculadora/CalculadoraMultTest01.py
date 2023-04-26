import unittest
from Calculadora import Calculadora

class CalculadoraMultTest(unittest.TestCase):
    def test_mult(self):
        calc = Calculadora()
        resultado = calc.mult(2, 3)
        self.assertEqual(resultado, 6)

    def test_mult2(self):
        calc = Calculadora()
        resultado = calc.mult(7, 7)
        self.assertTrue(resultado == 49, "Tem que dar 49")

    def test_mult3(self):
        calc = Calculadora()
        resultado = calc.mult(-3, 3)
        self.assertEqual(resultado, -9)

if __name__ == '__main__':
    unittest.main()