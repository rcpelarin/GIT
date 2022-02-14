class DadosEleicao:
    """
    Classe onde todos os cálculos para contagem de votos da eleição são definidos.
    """
    def __init__(self, eleitores, votos_validos, votos_brancos, votos_nulos):
        self.eleitores = eleitores
        self.votos_validos = votos_validos
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos
    
    def total(self):
        print(f'O Total de eleitores é {self.eleitores}.')

    def validos(self):
        v = int(self.votos_validos/self.eleitores*100)
        print(f'O percentual de votos válidos é {v}%')

    def brancos(self):
        b = int(self.votos_brancos/self.eleitores*100)
        print(f'O percentual de votos em branco é {b}%')

    def nulos(self):
        n = int(self.votos_nulos/self.eleitores*100)
        print(f'O percentual de votos nulos é {n}%')

eleicao = DadosEleicao(1000, 800, 150, 50)
eleicao.total()
eleicao.validos()
eleicao.brancos()
eleicao.nulos()