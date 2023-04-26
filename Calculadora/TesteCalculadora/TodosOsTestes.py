import unittest
from CalculadoraSomaTest01 import CalculadoraSomaTest
from CalculadoraSubTest01 import CalculadoraSubTest
from CalculadoraMultTest01 import CalculadoraMultTest
from CalculadoraDivTest01 import CalculadoraDivTest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(CalculadoraSomaTest))
    test_suite.addTest(unittest.makeSuite(CalculadoraSubTest))
    test_suite.addTest(unittest.makeSuite(CalculadoraMultTest))
    test_suite.addTest(unittest.makeSuite(CalculadoraDivTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())