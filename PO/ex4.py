def verificar_matriz():
    lista_bi = []

    linhas = int(input("Insira o número de linhas: "))

    for i in range(linhas):
        entrada = input(f"Linha {i+1}: ").strip()
        try:
            linha = [float(x) for x in entrada.split()]
            lista_bi.append(linha)
        except ValueError:
            print("Digite apenas números separados por espaço")
            return ()

    if not lista_bi:
        return ()

    colunas = len(lista_bi[0])

    for linha in lista_bi:
        if len(linha) != colunas:
            print("Não é uma matriz: número de colunas inconsistente")
            return ()

    print(f"É uma matriz {len(lista_bi)}x{colunas}")
    return len(lista_bi), colunas

verificar_matriz()

