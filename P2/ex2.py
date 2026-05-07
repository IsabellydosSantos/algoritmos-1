def mdc(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        resto = a % b
        a, b = b, resto
    return a


def mmc(a, b):
    mdc_valor = mdc(a, b)
    return (a * b) // mdc_valor


def main():
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))

    resultadomdc = mdc(n1, n2)
    resultadommc = mmc(n1, n2)

    print(f"O MDC dos números {n1} e {n2} é {resultadomdc} e o MMC é {resultadommc}")


main()

