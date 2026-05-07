def primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def encontra_primo(n):
    if n < 2:
        menor_maior_igual = 2  # O menor primo é 2
        maior_menor_igual = None  # Não existe primo ≤ n para n < 2
        return menor_maior_igual, maior_menor_igual
    
    # Encontra o maior primo menor ou igual a n
    maior_menor_igual = n
    while maior_menor_igual >= 2:
        if primo(maior_menor_igual):
            break
        maior_menor_igual -= 1
    
    # Encontra o menor primo maior ou igual a n
    menor_maior_igual = n
    while True:
        if primo(menor_maior_igual):
            break
        menor_maior_igual += 1
    
    return menor_maior_igual, maior_menor_igual

def main():
    try:
        n = int(input("Digite um número natural n: "))
        
        if n < 0:
            print("Digite um número natural (não negativo).")
            return
        
        menor_maior_igual, maior_menor_igual = encontra_primo(n)
        
        print(f"\nPara n = {n}:")
        
        if maior_menor_igual is not None:
            print(f"Maior número primo menor ou igual a n: {maior_menor_igual}")
        else:
            print("Não existe número primo menor ou igual a n (n < 2)")
        
        print(f"Menor número primo maior ou igual a n: {menor_maior_igual}")
        
        if primo(n):
            print(f"Obs: {n} é primo")
        else:
            print(f"Obs: {n} não é primo.")
            
    except ValueError:
        print("Digite um número inteiro válido.")

  
main()

