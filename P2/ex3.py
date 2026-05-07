def soma(matriz):
    soma = 0
    for i in range(min(len(matriz), len(matriz[0]))):
        soma += matriz[i][i]
    return soma


def main():
    linhas = int(input("Insira o número de linhas: "))
    colunas = int(input("Insira o número de colunas: "))

    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elem = int(input(f"Linha [{i + 1}][{j + 1}]: "))
            linha.append(elem)
        matriz.append(linha)

    for linha in matriz:
        print(linha)

    elem_diagonal = [matriz[i][i] for i in range(min(len(matriz), len(matriz[0])))]
    print("+".join(str(elem) for elem in elem_diagonal))
    print(f"Soma da diagonal: {soma(matriz)}")


main()
