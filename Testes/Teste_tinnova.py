eleitores = 1000
validos = 800
votos_brancos = 150
votos_nulos = 50

print(f'O Total de Eleitores é {eleitores}')

#Calculando e apresentando os votos válidos
v = validos/eleitores*100
print(f'O percentual de votos válidos é {v}%, sendo {validos} votos')

#Calculando e apresentando os votos em branco
b = votos_brancos/eleitores*100
print(f'O percentual de votos em branco é de {b}%, sendo {votos_brancos} votos')

#Calculando e apresentando os votos nulos
n = votos_nulos/eleitores*100
print(f'O percentual de votos nulos é de {n}%, sendo {votos_nulos} votos')
