class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b == 0:
            return print("ERROR - não é possivel dividir por zero")
        return a / b