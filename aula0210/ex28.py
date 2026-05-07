texto = input("Digite um texto: ").lower().strip()
palavra = input("Digite uma palavra: ").lower()

palavras = texto.split()
quant = palavras.count(palavra)
posicao = []

for i in range(len(palavras)):
    if palavras[i] == palavra:
        posicao.append(i + 1)

print(f"A palavra {palavra} aparece {quant} vezes no texto nas posições {posicao}")

