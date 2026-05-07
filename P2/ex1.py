texto = input("Insira um texto sem acentos: ").lower().strip()

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
espacos = 0

for caractere in texto:
    if caractere == ' ':
        espacos += 1
    elif caractere in vogais:
        vogais[caractere] += 1

print(f"Espaços: {espacos}, a: {vogais['a']}, e: {vogais['e']}, i: {vogais['i']}, o: {vogais['o']}, u: {vogais['u']}")

