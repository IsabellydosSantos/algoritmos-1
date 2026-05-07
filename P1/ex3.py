n = int(input("Insira a quantidade de números da lista (n>1): "))
lista = []
if n <= 1:
    print("Esse número é inválido")
else:
    for i in range(n):
        num = int(input(f"{i+1}° número: "))
        lista.append(num)
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            lista.pop(i)
        else:
            i += 1
    print("Lista sem números pares: ", lista)

