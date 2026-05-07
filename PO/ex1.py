import math

a = float(input("Insira o número a: "))
b = float(input("Insira o número b: "))
c = float(input("Insira o número c: "))

delta = b ** 2 - 4 * a * c
raizd = math.sqrt(delta)
bhaskarap = (-b + raizd)/(2*a)
bhaskaran = (-b - raizd)/(2*a)

if a == 0:
    if b == 0:
        print("Não tem raiz")
    else:
        raiz = (-c/b)
        print("A raiz é: ", raiz)
else:
    if delta < 0:
        print("Não existem raizes reais")
    elif delta != 0:
        print(f"As raízes da equação de segundo grau são {bhaskarap} e {bhaskaran}")
    else:
        raiz = -b / (2 * a)
        print("A raiz é: ", raiz)

