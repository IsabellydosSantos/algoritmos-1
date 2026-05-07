#imprime se o número n é primo

n = int(input("Insira um número inteiro positivo (n>1): "))

if n <= 1:
    print("Número Inválido")
else:
    divisores = []

for i in range(1, n + 1):
    if n % i == 0:
        divisores.append(i)

if len(divisores) == 2:
    print(f"{n} é primo")
else:

    print(f"{n} não é primo")

