def conv(vetor):
    return [1 if valor > 0 else 0 for valor in vetor]

def main():
    vetor = []

    print("Digite 30 números: ")

    for i in range(30):
        while True:
            numero = float(input(f"Número {i+1}/30: "))
            vetor.append(numero)
            break

    print(f"Vetor original: {vetor}")

    vetor_mod = conv(vetor)

    print(f"Vetor modificado: {vetor_mod}")

main()

