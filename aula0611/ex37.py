def verificar_matriz_quadrada():

    try:
        linhas = int(input("Digite o número de linhas da matriz: "))
        colunas = int(input("Digite o número de colunas da matriz: "))

        print("\nDigite os elementos da matriz linha por linha:")
        matriz = []

        for i in range(linhas):
            linha = []
            print(f"Linha {i + 1}:")
            for j in range(colunas):
                elemento = float(input(f"  Elemento [{i + 1},{j + 1}]: "))
                linha.append(elemento)
            matriz.append(linha)

        print("\nMatriz informada:")
        for linha in matriz:
            print(linha)

        if linhas == colunas:
            print(f"\n A matriz é QUADRADA ({linhas}x{colunas})")
        else:
            print(f"\n A matriz NÃO é quadrada ({linhas}x{colunas})")

    except ValueError:
        print("Digite apenas números válidos.")


verificar_matriz_quadrada()

