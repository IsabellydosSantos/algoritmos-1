n = input("Insira a sequência de números inteiros separados por espaço: ")
lista = [int(x) for x in n.split()]
media = sum(lista)/len(lista)
print(f"A média da sequência é {media:.2f}")
