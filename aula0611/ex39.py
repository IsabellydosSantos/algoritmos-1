def soma(matriz):
    soma = 0
    for i in range(len(matriz)):
        # A diagonal principal tem índices i,i
        soma += matriz[i][i]
    return soma

def le_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    
    # Verifica se a matriz é quadrada
    if linhas != colunas:
        print("Para uma diagonal principal bem definida, a matriz deve ser quadrada")
    
    matriz = []
    print(f"\nDigite os elementos da matriz {linhas}x{colunas}:")
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = float(input(f"Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

def mostrar_matriz(matriz):
    print("\nMatriz informada:")
    for linha in matriz:
        print("[", end="")
        for elemento in linha:
            print(f"{elemento:8.2f}", end="")
        print(" ]")


def main():
    matriz = le_matriz()
    
    mostrar_matriz(matriz)
    
    try:
        soma = soma(matriz)
        print(f"\nSomatório da diagonal principal: {soma:.2f}")
        
        print("Elementos da diagonal principal:", end=" ")
        elementos_diagonal = [matriz[i][i] for i in range(min(len(matriz), len(matriz[0])))]
        print(" + ".join(f"{elem:.2f}" for elem in elementos_diagonal))
        
    except IndexError:
        print("Erro: A matriz não é quadrada ou está mal formada")


    main()

