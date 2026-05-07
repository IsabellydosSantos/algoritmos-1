texto = str(input("Digite uma palavra ou texto: ")).lower().strip()

if texto == texto[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
    
