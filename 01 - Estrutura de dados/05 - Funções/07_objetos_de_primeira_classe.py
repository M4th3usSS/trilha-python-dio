def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, multiplicar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, dividir)  # O resultado da operação 10 + 10 = 20

op = somar

print(op(1, 23))
