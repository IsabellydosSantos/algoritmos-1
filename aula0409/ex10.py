#imprime a quantidade de divisores de n

n = int(input("Insira um número inteiro positivo (n>1): "))

if n <= 1:
    print("Número Inválido")
else:
    divisores = []

for i in range(1, n + 1):
    if n % i == 0:
        divisores.append(i)
        quant = len(divisores)
        print(f"{n} tem {quant} divisores")
