#faz a fatoração de n em números primos

n = int(input("Insira um número inteiro positivo (n>1): "))
num_orig = n
if n <= 1:
    print("Número Inválido")
else:
    fatores = []
    divisor = 2

while n > 1:
    if n % divisor == 0:
        fatores.append(divisor)
        n = n // divisor
    else:
        divisor += 1

print(f"Os fatores primos de {num_orig} são: {fatores}")

