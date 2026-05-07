def contar_zeros_matriz():

    print("Digite a matriz linha por linha.")

    matriz = []
    print("Digite cada linha separada por espaços:")

    primeira_linha = input("Linha 1: ").split()
    n = len(primeira_linha)
    matriz.append([int(x) for x in primeira_linha])

    for i in range(1, n):
        linha = input(f"Linha {i + 1}: ").split()
        if len(linha) != n:
            print("Erro: Todas as linhas devem ter o mesmo tamanho")
            return
        matriz.append([int(x) for x in linha])

    zeros = 0
    for linha in matriz:
        for num in linha:
            if num == 0:
                zeros += 1

    print(f"\nMatriz {n}x{n}:")
    for linha in matriz:
        print(linha)

    print(f"\nZeros: {zeros} de {n * n} elementos")


contar_zeros_matriz()

