#calcula expoente sem usar **

base = int(input("Base: "))
exp = int(input("Expoente: "))
result = base
i = 1
while i < exp:
  result = result * base
  i = i + 1

print(result)

