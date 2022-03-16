
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O Saldo de {self.__titular} é {self.__saldo}")
    
    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saque(self, valor):
        if (valor <= __pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O saque de {valor} ultrapassa o limite máximo")

    def transfer(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
    
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    
    
    
