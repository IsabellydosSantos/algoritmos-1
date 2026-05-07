def num_tri(n):
    if n < 0:
        return False, None
    elif n == 0:
        return True, (0,1,2)

    i = 0
    while i*(i+1)*(i+2) <= n:
        if i*(i+1)*(i+2) == n:
            return True, (i, i+1, i+2)
        i += 1
    return False, None


def main():
    n = int(input("Insira um número inteiro positivo: "))

    resultado, elementos = num_tri(n)

    print(resultado, elementos)


main()

