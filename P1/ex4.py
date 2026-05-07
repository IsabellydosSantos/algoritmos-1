x = int(input("Insira um número  inteiro positivo: "))
y = int(input("Insira um número  inteiro positivo: "))
z = int(input("Insira um número  inteiro positivo: "))

if (x + y > z) and (x + z > y) and (z + y > x):
    if x==y==z:
        print("O triângulo é válido e equilátero")
    elif x!=y!=z:
        print("O triângulo é válido e escaleno")
    else:
        print("O triângulo é válido e isósceles")
else:

    print("Os valores não podem formar um triângulo, logo ele não é válido")

