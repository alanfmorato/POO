class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando metodo")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando metodo")
        self.__nome = nome

cliente = Cliente("alan")
cliente.nome = "marco"
print(cliente.nome)