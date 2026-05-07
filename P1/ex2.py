# Recebe o valor de n
n = int(input("Digite um número inteiro positivo maior que 0: "))

# Verifica se n é válido
if n <= 0:
    print("O número deve ser maior que 0!")
else:
    soma = 0
    contador = 0
    numero = 2  # Começamos do primeiro número primo
    
    while contador < n:
        # Verifica se o número é primo
        eh_primo = True
        
        # Um número é primo se for divisível apenas por 1 e por ele mesmo
        # Verificamos divisores de 2 até a raiz quadrada do número
        divisor = 2
        while divisor * divisor <= numero:
            if numero % divisor == 0:
                eh_primo = False
                break
            divisor += 1
        
        # Se for primo, adiciona à soma e incrementa o contador
               if eh_primo:
            if contador == 0:
                print(numero, end="")
            else:
                print(f" + {numero}", end="")
            soma += numero
            contador += 1
        
        numero += 1
    
    print(f"A soma dos {n} primeiros números primos é: {soma}")
