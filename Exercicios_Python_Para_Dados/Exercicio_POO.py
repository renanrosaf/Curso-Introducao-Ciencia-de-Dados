#Criando classe chamada CARROS:
class Carro:
    #funcao construtora
    def __init__(self,modelo,placa,ano):
        self.modelo=modelo
        self.placa=placa
        self.ano=ano    

    #criando o método chamar placa
    def mostrar_multa(self):
        print("Modelo do veículo multado: ", self.modelo, "Ano:",self.ano)

    def mostrar_placa(self):
        print("Placa do veículo multado: ", self.placa)
   

#instanciei os objetos:
carro1=Carro("Ferrari 850","A7EF9",2020)
carro2=Carro("Chevrolet Camaro","B1LQ2",2015)

#excução dos métodos de cada objeto
carro1.mostrar_multa()
carro1.mostrar_placa()

print("-" * 40)  # Linha visual para organizar o terminal

carro2.mostrar_multa()
carro2.mostrar_placa()
