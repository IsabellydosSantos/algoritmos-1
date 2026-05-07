texto = str(input("Digite um texto: "))
caracteres = ". , ; : ! ?"

for i in caracteres:
    texto = texto.replace(i, " ")

palavra = texto.split()

print(f"O texto tem {len(palavra)} palavras.")
