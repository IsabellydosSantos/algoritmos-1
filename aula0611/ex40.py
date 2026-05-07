def matriz_identidade(matriz):

    n = len(matriz)

    for i in range(n):
        for j in range(n):
            if i == j:
                if matriz[i][j] != 1:
                    return False
                else:
                    if matriz[i][j] != 0:
                        return False
    return True


def main():

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

    print(f"\nMatriz {n}x{n}:")
    for linha in matriz:
        print(linha)

    if matriz_identidade(matriz):
        print("É uma matriz identidade")
    else:
        print("Não é uma matriz identidade")

main()

