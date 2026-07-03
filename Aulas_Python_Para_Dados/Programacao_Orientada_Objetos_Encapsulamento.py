
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
        self.__nome=nome #encapsulando, protegendo o atributo
        self.__idade=idade #encapsulando idade
        self.altura=altura

#definindo uma ação para classe:método, mesma sintaxe função
#self: classe em si
    def apresentar(self): 
        print('Olá, meu nome é:',self.__nome,'tenho', self.__idade, 'anos de idade e tenho', self.altura, 'de altura') #imprimindo cada atributo da classe, dentro de uma frase


    def get_nome(self):
        return self.__nome
    
    #alterando idade, só pode ser alterado menor 40
    def set_idade(self,nova_idade):
        if nova_idade<40:
            self.__idade=nova_idade



#Só instanciei objeto aqui: Instanciar um Objeto:Torno a classe real aqui
p1=Pessoa("João",33,"1,80 m")
p2=Pessoa("Karina",28,"1,70 m")

#Chamando apresentar:
p1.apresentar()
p2.apresentar()

#consigo alterar idade, pois ela não estam encapsulada
#p1.idade=34
p1.set_idade(35)
p1.apresentar()

#Pratica: mesma classe chamada Pessoa, embora tenha os mesmo atributos. Ao tornar ela concreta, alguem em um momento criar uma variavel pessoa
#acima são o que ela é.

#Encapsulando: #falta de segurança acessar nome assim, atributo acessado diretamente
#print(p1.nome) #da erro acessando assim

#para acessar, crio método para recuperar atributo encapsulado em uma classe:metodo get
print(p1.get_nome())


# =======================================================
# EXEMPLO PRÁTICO: CLASSES, OBJETOS E ENCAPSULAMENTO
# =======================================================

# Nós nos enxergamos como uma classe: temos características em comum (cabelo, nome, etc).
# A classe 'Pessoa' define essas propriedades (atributos) e o que ela faz (métodos).

# 1. CRIANDO A CLASSE
class Pessoa:
    
    # FUNÇÃO CONSTRUTORA (__init__)
    # É a função de iniciação da classe. Constrói o objeto e o torna realidade.
    # Atribui os parâmetros informados na hora da criação aos atributos da classe.
    def __init__(self, nome, idade, altura):  
        # ENCAPSULAMENTO: Protegendo os atributos com duplo sublinhado (__)
        self.__nome = nome   
        self.__idade = idade 
        
        # Atributo PÚBLICO (pode ser acessado e alterado diretamente de fora)
        self.altura = altura

    # DEFININDO UMA AÇÃO (MÉTODO)
    # self: Refere-se à própria classe/objeto em si.
    def apresentar(self): 
        # Imprimindo cada atributo da classe dentro de uma frase usando f-strings
        print(f'Olá, meu nome é: {self.__nome}, tenho {self.__idade} anos de idade e tenho {self.altura} de altura.')

    # MÉTODO GET: Recupera o valor de um atributo encapsulado para leitura externa
    def get_nome(self):
        return self.__nome
    
    # MÉTODO SET: Altera o valor de um atributo encapsulado seguindo uma regra específica
    def set_idade(self, nova_idade):
        # Regra de negócio: A idade só pode ser alterada se for menor que 40
        if nova_idade < 40:
            self.__idade = nova_idade
        else:
            print("Erro: A idade não pode ser maior ou igual a 40.")


# =======================================================
# 2. INSTANCIANDO OBJETOS (Tornando a classe real)
# =======================================================
# Na prática, usamos a "receita" (Classe Pessoa) para criar instâncias concretas (Objetos p1 e p2).

p1 = Pessoa("João", 33, "1,80 m")
p2 = Pessoa("Karina", 28, "1,70 m")

# Chamando o método 'apresentar' para cada objeto criado:
p1.apresentar()
p2.apresentar()

print("-" * 30)

# =======================================================
# 3. MANIPULANDO OS DADOS ENCAPSULADOS
# =======================================================

# ALTERANDO A IDADE:
# Como a idade está encapsulada (__idade), não podemos fazer p1.idade = 34 diretamente.
# Precisamos usar o método SET, que passa pela regra de validação que criamos:
p1.set_idade(35)
p1.apresentar() # Vai imprimir com a idade atualizada para 35

print("-" * 30)

# ACESSANDO O NOME:
# É uma falha de segurança acessar o atributo diretamente (ex: print(p1.__nome)). 
# O Python vai gerar um erro dizendo que o atributo não existe, pois ele está protegido.

# A forma correta para acessar (ler) o atributo encapsulado é através do método GET:
nome_recuperado = p1.get_nome()
print(f'Nome recuperado com o método GET: {nome_recuperado}')