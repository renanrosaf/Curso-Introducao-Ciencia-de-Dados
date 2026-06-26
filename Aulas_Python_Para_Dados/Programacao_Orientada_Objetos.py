"""
CONCEITO DA AULA:
- Classe: É o molde abstrato (A ideia do que é uma 'Pessoa').
- Objeto: É a materialização desse molde (O 'João' e a 'Karina' reais).
- Atributos: São as características (Nome, Idade, Altura).
- Métodos: São as ações que essa classe sabe fazer (Apresentar).
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        # O método __init__ é o CONSTRUTOR. Ele dá vida ao objeto.
        # O 'self' é a própria instância olhando para si mesma.
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        # Método: uma função acoplada à classe (uma ação)
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e tenho {self.altura} de altura.")


# =========================================================
# ÁREA DE INSTANCIAÇÃO (Tornando a classe concreta na memória)
# =========================================================

p1 = Pessoa("João", 33, "1,80 m")
p2 = Pessoa("Karina", 28, "1,70 m")

# Chamando o método (ação) de cada objeto criado:
p1.apresentar()
p2.apresentar()



#VERSÃO 2:
#Nós nos enxergamos como uma classe, temos uma característica.
#Cabelo, Nome característica em comum da pessoa
#Classe pessoa define propriedade 

#Criando classe pessoa
class Pessoa:
    #funcao inciação da classe, com dois atributos:nome e idade
    #cosntrução do objeto da classe, torna realidade a classe
    #atribuir para cada atributo da classe, parametros informados na hora que foi construida
    #usando funcao construtoria para gerar a classe
    def __init__(self,nome,idade,altura):  
        self.nome=nome 
        self.idade=idade
        self.altura=altura

#definindo uma ação para classe:método, mesma sintaxe função
#self: classe em si
    def apresentar(self): 
        print('Olá, meu nome é:',self.nome,'tenho', self.idade, 'anos de idade e tenho', self.altura, 'de altura') #imprimindo cada atributo da classe, dentro de uma frase

#Só instanciei objeto aqui: Instanciar um Objeto:Torno a classe real aqui
p1=Pessoa("João",33,"1,80 m")
p2=Pessoa("Karina",28,"1,70 m")

#Chamando apresentar:
p1.apresentar()
p2.apresentar()

#Pratica: mesma classe chamada Pessoa, embora tenha os mesmo atributos. Ao tornar ela concreta, alguem em um momento criar uma variavel pessoa
#acima são o que ela é.

