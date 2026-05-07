n = int(input("Quantidade de lançamentos: "))
r = input(f"Digite os {n} resultados (1-6) separados por vírgulas:").strip()
resultados = list(map(int, r.split(',')))

# Verificações básicas
if len(resultados) != n:
    print("Quantidade incorreta de resultados")
    exit()

if any(x < 1 or x > 6 for x in resultados):
    print("Faces devem ser entre 1 e 6")
    exit()

# PASSO 1: Criar um dicionário vazio para armazenar as contagens
contagem = {}  # Exemplo: {1: 5, 2: 3, 3: 2} significa: face1=5x, face2=3x, face3=2x

# PASSO 2: Percorrer cada resultado com um loop
for face in resultados:    
    # Verifica se esta face já está no dicionário
    if face in contagem:
        # Se já estiver: incrementa a contagem
        contagem[face] += 1
    else:
        # Se não estiver: cria entrada com valor 1
        contagem[face] = 1

# PASSO 3: Mostrar resultados organizados
print("\n=== Resultado Final ===")
for face in sorted(contagem.keys()):  # sorted() ordena as faces
    print(f"Face {face}: {contagem[face]} ocorrências")

# Análise de vício
freq_esperada = n / 6
mais = max(contagem.values()) # Face que mais apareceu 
menos = min(contagem.values()) # Face que menos apareceu
diferenca = mais - menos # Calcula o desequilíbrio 

print(f"Diferença máxima: {diferenca}")

if diferenca > freq_esperada * 0.7:
  # Se a diferença for maior que 70% da frequência esperada
  print("⚠️  Possível dado viciado")
else:
    print("✓  Dado parece honesto")

