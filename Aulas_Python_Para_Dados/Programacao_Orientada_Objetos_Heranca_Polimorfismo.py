
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


#herança: herdar

#classe: ALuno, é uma pessoa, tem idade, tem altura
#uma pessoa não precisa ter matricula, mas quando pessoa é aluno ela passa a ter
class Aluno(Pessoa): #herdando classe pessoa
    def __init__(self, nome, idade, altura,matricula):
        super().__init__(nome,idade,altura)#acesso tudo da classe mae(pessoa)
        self.matricula=matricula
    def estudante(self):
        print('A matricula do aluno é:', self.matricula)
    def apresentar(self):#na classe aluno:metodo apresentar, poliformismo
        print('Olá, meu nome é:' ,super().get_nome(), ' e minha matricula é:', self.matricula)
#forma apresenta é diferente da forma de apresentar uma pessoa
aluno1=Aluno('Pedro',30,'1,90','000678908')
aluno1.estudante()   
aluno1.apresentar()

# =======================================================
# EXEMPLO PRÁTICO: PILARES DA POO EM PYTHON
# =======================================================

# 1. CRIANDO A CLASSE MÃE (Superclasse)
# A classe 'Pessoa' define as propriedades e comportamentos básicos.
# Nós nos enxergamos como uma classe: temos características em comum (nome, idade, altura).
class Pessoa:
    
    # FUNÇÃO CONSTRUTORA (__init__)
    # É chamada automaticamente ao instanciar (criar) o objeto, tornando a classe realidade.
    # Atribui os parâmetros informados aos atributos da classe.
    def __init__(self, nome, idade, altura):  
        
        # ENCAPSULAMENTO: O uso de '__' (duplo sublinhado) torna os atributos PRIVADOS.
        # Eles ficam protegidos e só podem ser alterados/acessados por dentro desta mesma classe.
        self.__nome = nome   
        self.__idade = idade 
        
        # Atributo PÚBLICO (sem o duplo sublinhado, pode ser acessado livremente de fora)
        self.altura = altura

    # MÉTODO: Define uma ação da classe (mesma sintaxe de uma função).
    # O parâmetro 'self' indica que estamos nos referindo à classe em si (este objeto específico).
    def apresentar(self): 
        print(f'Olá, meu nome é: {self.__nome}, tenho {self.__idade} anos de idade e tenho {self.altura}m de altura.')

    # MÉTODO GET (Getter): Recupera e retorna o valor de um atributo encapsulado de forma segura.
    def get_nome(self):
        return self.__nome
    
    # MÉTODO SET (Setter): Altera o valor de um atributo encapsulado, impondo regras de negócio.
    def set_idade(self, nova_idade):
        # Regra: A idade só pode ser alterada se o novo valor fornecido for menor que 40.
        if nova_idade < 40:
            self.__idade = nova_idade
        else:
            print("Erro: A idade informada excede o limite permitido (40).")


# =======================================================
# 2. HERANÇA E POLIMORFISMO (Criando a Classe Filha)
# =======================================================

# A classe 'Aluno' É UMA 'Pessoa'. Ela herda tudo (idade, altura, nome).
# Uma pessoa comum não precisa ter matrícula, mas quando ela se torna um Aluno, passa a ter.
class Aluno(Pessoa): 
    
    def __init__(self, nome, idade, altura, matricula):
        # SUPER(): Acessa a classe mãe (Pessoa) e chama o construtor dela 
        # para inicializar os atributos que foram herdados.
        super().__init__(nome, idade, altura)
        
        # Inicializa o atributo que é exclusivo da classe Aluno
        self.matricula = matricula
        
    # Método específico da classe Aluno
    def estudante(self):
        print(f'A matrícula do aluno é: {self.matricula}')
        
    # POLIMORFISMO (Sobrescrita de Método)
    # A classe Aluno tem o seu próprio método 'apresentar', que sobrescreve o da classe Pessoa.
    # A forma como o Aluno se apresenta é diferente da forma de uma pessoa comum.
    def apresentar(self):
        # Como '__nome' é um atributo privado da classe mãe, usamos 'super().get_nome()' 
        # para conseguir acessá-lo aqui dentro da classe filha com segurança.
        print(f'Olá, meu nome é: {super().get_nome()} e minha matrícula é: {self.matricula}')


# =======================================================
# INSTANCIANDO E TESTANDO OS OBJETOS
# =======================================================

# Criando um objeto (instância) referenciando a classe Aluno
aluno1 = Aluno('Pedro', 30, '1.90', '000678908')

# Chamando o método exclusivo do Aluno
aluno1.estudante()   

# Chamando o método sobrescrito (Polimorfismo em ação!)
aluno1.apresentar()

