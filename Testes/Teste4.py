#Teste Soma Multiplos de 3 ou de 5.

soma = 0
teto = int(input('Digite o número que servirá de limite para a busca de múltiplos de 3 e 5:'))
for c in range(1, teto):
    if (c % 3 == 0) or (c % 5 == 0):
        print(c, end=' ')
        soma += c
print (f'\nA soma dos múltiplos de 3 ou 5, entre 1 e {teto} é igual a {soma}')