#Teste Fatorial

n = int(input("Escolha um numero inteiro para saber seu fatorial: "))
cont = n
f = 1
print(f"Calculando {n}! = ", end="")
while cont > 0:
    print (f"{cont}", end="")
    print (" x " if cont > 1 else " = ", end="")
    f *= cont
    cont -= 1
print(f"{f}")