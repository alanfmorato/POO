class Conta: #Definindo a classe
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo do {} é R${}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor acima do limite")
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    def get_saldo(self):
        print(self.__saldo)
        return self.__saldo
        
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        print(self.__limite)
        return self.__limite

    @limite.setter
    def limite(self, limite):
       self.__limite = limite

    @staticmethod
    def codigo_banco():
        print("001")
        return "001"

conta = Conta(123, 'Alan', 55.0, 1000.0)
conta2 = Conta(321, 'Marco', 100.0, 1000.0)

conta.codigo_banco()
