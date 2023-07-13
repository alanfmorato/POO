#Estudo sobre Orientação a Objetos em Python

## Contexto

Somos um baco e precisamos criar funcionalidades ao nosso sistema, para isso precisaremos trabalhar com orientação a objetos, vamos começar pelo conceito de dicionários

### Início do código

```python
def cria_conta(numero, titular, saldo, limite):
   conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
   return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("Saldo: {}".format(conta['saldo']))
```

### Classes e Atributos

Uma classe em Python é uma estrutura que representa um objeto do mundo real e contém seus atributos e métodos. É uma estrutura fundamental na programação orientada a objetos (POO) em Python, pois permite que o programador crie novos objetos com base em uma classe existente. Os objetos criados a partir de uma classe são referidos como instâncias da classe.

```python
class Conta: #Definindo a classe
    def __init__(self, numero, titular, saldo, limite): #Definindo o método construtor da classe
        print("Construindo ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
				#Essas linhas atribuem os valores passados como argumentos para o 
				#construtor aos atributos da classe. O self é usado para referenciar
				#o objeto atual, e self.numero, por exemplo, cria um atributo chamado 
				#"numero" no objeto atual e o atribui o valor passado como argumento para 
				#o construtor.
```

Para acessar um atributo utilizaremos o . , ou seja, conta.saldo para acessar o saldo de uma conta em específico.

### Métodos

Para criar um método precisamos definir o que será feito dentro dele

```python
class Conta: #Definindo a classe
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo do {} é R${}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
				self.saldo -= valor

conta = Conta(123, 'Alan', 55.0, 1000.0)
conta2 = Conta(321, 'Marco', 100.0, 1000.0)

conta.deposita(100)
conta2.deposita(100)
conta.extrato()
```

Quando você cria uma instância da classe **`Conta`** usando a linha **`conta = Conta(123, 'Alan', 55.0, 1000.0)`**, um objeto chamado **`conta`** é criado com todos os atributos e métodos definidos na classe. Esse objeto é uma instância específica da classe **`Conta`**.

Para acessar os métodos da instância da classe, você precisa usar a notação de ponto (**`.`**) para especificar em qual objeto a chamada do método deve ser feita. No caso do método **`deposita`**, você precisa chamar **`conta.deposita(100)`** para depositar o valor de 100 na conta associada ao objeto **`conta`**.

### Encapsulamento

O encapsulamento no Python (e em outras linguagens de programação orientadas a objetos) é um conceito que permite controlar o acesso aos atributos e métodos de uma classe. O objetivo principal do encapsulamento é proteger os dados e garantir que sejam acessados e modificados apenas de maneiras predefinidas, promovendo a segurança, a consistência e a organização do código.

Existem três níveis de encapsulamento no Python:

1. **Público**: Atributos e métodos públicos são acessíveis a partir de qualquer lugar do programa, tanto dentro da própria classe quanto externamente a ela. Eles podem ser acessados diretamente usando a notação de ponto (**`.`**) após a instância do objeto ou a referência à classe.
2. **Protegido**: Atributos e métodos protegidos são indicados por um único sublinhado (**`_`**) no início do nome. Embora ainda sejam acessíveis de fora da classe, é uma convenção indicar que eles são destinados a serem usados apenas dentro da classe ou por suas subclasses. O uso correto desses membros é baseado na confiança do programador.
3. **Privado**: Atributos e métodos privados são indicados por dois sublinhados (**`__`**) no início do nome. Esses membros são considerados privados e não devem ser acessados diretamente de fora da classe. No entanto, eles podem ser acessados por meio de métodos públicos da classe que têm permissão para acessá-los. O objetivo principal do encapsulamento privado é evitar que outros objetos manipulem ou acessem diretamente os dados internos da classe, mantendo assim a integridade do objeto.

```python
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
    
    def saca(self, valor):
        self.__saldo -= valor
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

conta = Conta(123, 'Alan', 55.0, 1000.0)
conta2 = Conta(321, 'Marco', 100.0, 1000.0)

conta2.transfere(10.0, conta)
conta2.extrato()
conta.extrato()
```

### Getters e Setters

Um get sempre precisa retornar algo, um set sempre precisa alterar algo.

No código fornecido, a parte com **`@property`** e **`@limite_set`** implementa um conceito chamado "property" ou "propriedade" em Python. Essa funcionalidade permite definir métodos especiais que são acessados como atributos, tornando o código mais intuitivo e elegante.

A linha **`@property`** é um decorador que indica que o método seguinte, **`limite`**, será tratado como uma propriedade. Nesse caso, a propriedade é chamada de **`limite`**. Quando você acessa **`conta.limite`**, o método **`limite()`** é chamado automaticamente.

A linha **`@limite.setter`** é outro decorador que indica que o método seguinte, **`limite`**, será usado para atribuir um novo valor à propriedade **`limite`**. Nesse caso, é um "setter" para a propriedade **`limite`**. Quando você atribui um valor a **`conta.limite`**, o método **`limite()`** é chamado automaticamente para realizar a atribuição. No exemplo acima, ele simplesmente atribui o novo valor ao atributo **`__limite`**.
```python
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
    
    def saca(self, valor):
        self.__saldo -= valor
    
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

conta = Conta(123, 'Alan', 55.0, 1000.0)
conta2 = Conta(321, 'Marco', 100.0, 1000.0)

conta.limite = 2000.0
conta.limite
```
