import unittest
from Calculadora import Calculadora

class CalculadoraDivTest(unittest.TestCase):
    def test_div(self):
        calc = Calculadora()
        resultado = calc.div(10, 5)
        self.assertEqual(resultado, 2)

    def test_div2(self):
        calc = Calculadora()
        resultado = calc.div(1000, 1000)
        self.assertFalse(resultado == 0, "Não pode dar 0")

    def test_div3(self):
        calc = Calculadora()
        resultado = calc.div(0, 1)
        self.assertEqual(resultado, 0)
        
if __name__ == '__main__':
    unittest.main()