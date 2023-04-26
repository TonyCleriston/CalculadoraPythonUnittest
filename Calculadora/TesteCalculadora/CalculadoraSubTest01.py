import unittest
from Calculadora import Calculadora

class CalculadoraSubTest(unittest.TestCase):
    def test_sub(self):
        calc = Calculadora()
        resultado = calc.sub(5, 3)
        self.assertEqual(resultado, 2)

    def test_sub2(self):
        calc = Calculadora()
        resultado = calc.sub(400, 401)
        self.assertFalse(resultado == 1, "Não pode dar 1")

    def test_sub3(self):
        calc = Calculadora()
        resultado = calc.sub(0, 3)
        self.assertEqual(resultado, -3)

if __name__ == '__main__':
    unittest.main()