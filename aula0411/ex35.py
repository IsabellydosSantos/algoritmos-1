def mdc(a, b):
    # Troca automática se necessário (sempre a >= b)
    if a < b:
        a, b = b, a  # Troca os valores

    while b != 0:
        resto = a % b
        a, b = b, resto

    return a

def main():
    try:
        n1 = int(input("Insira o primeiro número inteiro positivo: "))
        n2 = int(input("Insira o segundoo número inteiro positivo: "))

        if n1 < 0 or n2 < 0:
            print("Digite apenas números positivos")
            return

        resultado = mdc(n1, n2)

        print(f"MDC({n1},{n2})")
        print(resultado)

    except ValueError:
        print("Digite apenas números inteiros")


main()

