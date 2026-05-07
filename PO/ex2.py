numero_decimal = int(input("Digite um número inteiro decimal: "))

# Armazena o número original para exibição posterior
numero_original = numero_decimal

# Se o número for 0, seu binário é 0
if numero_decimal == 0:
    print(f"O número 0 em binário é: 0")
else:
    # Lista para armazenar os dígitos binários (restos das divisões)
    digitos_binarios = []
    
    # Converte o número decimal para binário usando divisões sucessivas por 2
    while numero_decimal > 0:
        # Calcula o resto da divisão por 2 (0 ou 1)
        resto = numero_decimal % 2
        # Adiciona o resto à lista de dígitos binários
        digitos_binarios.append(str(resto))
        # Divide o número por 2 (divisão inteira)
        numero_decimal = numero_decimal // 2
    
    # Inverte a lista porque os restos foram coletados do último para o primeiro
    numero_binario = ''.join(digitos_binarios[::-1])
    
    print(f"O número {numero_original} em binário é: {numero_binario}")

