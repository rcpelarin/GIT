class DadosEleicao:
    """
    Classe onde todos os cálculos para contagem de votos da eleição é definido.
    """
    def __init__(self, eleitores, votos_validos, votos_brancos, votos_nulos):
        self.eleitores = eleitores
        self.votos_validos = votos_validos
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos

    def validos(self):
        v = votos_validos/eleitores*100
        return (v)

    def brancos(self):
        b = votos_brancos/eleitores*100
        return (b)

    def nulos(self):
        n = votos_nulos/eleitores*100
        return (n)

eleitores = 1000
votos_validos = 800
votos_brancos = 150
votos_nulos = 50

print(f'O Total de Eleitores é {eleitores}')
print(f'O percentual de votos válidos é {v}%, sendo {votos_validos} votos')
print(f'O percentual de votos em branco é de {b}%, sendo {votos_brancos} votos')
print(f'O percentual de votos nulos é de {n}%, sendo {votos_nulos} votos')
