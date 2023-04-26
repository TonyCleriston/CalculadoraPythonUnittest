import time
from Calculadora import Calculadora
x = 1
while x != 0:
    print("-----/     Calculadora     /------")
    print("")
    print("Digite   +   para   SOMAR")
    print("Digite   -   para   SUBTRAIR")
    print("Digite   *   para   MULTIPLICAÇÂO")
    print("Digite   /   para   SOMAR")
    print("Aperte ENTER   para   FINALIZAR")
    operacao = input("Escolha a operação: ")
    if operacao == "":
        break
    if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except:
            print("ERROR - Digite um numero inteiro")
            break
        if operacao == "+":
            resultado = Calculadora.soma(num1,num2)
        elif operacao == "-":
            resultado = Calculadora.sub(num1,num2)
        elif operacao == "*":
            resultado = Calculadora.mult(num1,num2)
        elif operacao == "/":
            resultado = Calculadora.div(num1,num2)

        print("")
        print("Resultado: ", resultado)
        time.sleep(2)

    else:
        print("ERROR - Digite uma operação válida do menu")
        break
