#imprime os divisores de n

n = int(input("Insira um número inteiro positivo (n>1): "))

divisores = []

for i in range(1, n + 1):
    if n <= 1:
        print("Número Inválido")
    elif n % i == 0:
        divisores.append(i)
        print(f"Os divisores de {n} são {divisores}")
