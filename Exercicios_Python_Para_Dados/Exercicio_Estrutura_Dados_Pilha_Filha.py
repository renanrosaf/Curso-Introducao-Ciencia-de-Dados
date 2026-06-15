from collections import deque #Método de filha

#1 Criando lista 
compra_frutas_pilha=[]

#2 Métodos de pilha e fila
#Primeiro pelo método de pilha:LIFO
compra_frutas_pilha.insert(0,"Pêra")
compra_frutas_pilha.insert(1,"Maçã")
compra_frutas_pilha.insert(2,"Uva")
compra_frutas_pilha.insert(3,"Banana")
compra_frutas_pilha.insert(4,"Laranja")

#print(compra_frutas_pilha) #imprimindo os compoentes

#agora inserindo dados via fila, necessito imputar a variavel o método deque: FIFO
compra_frutas_fila=deque()
compra_frutas_fila.append("Melão")
compra_frutas_fila.append("Melância")
compra_frutas_fila.append("Goiaba")
compra_frutas_fila.append('Laranja')
compra_frutas_fila.append("Maçã")

#print(compra_frutas_fila) #imprimindo os compoentes

#3: Laço de repetição para imprimir todos os elementos dessa lista
for fruta in compra_frutas_pilha :
    print(fruta)

for fruta in compra_frutas_fila:
    print(fruta)

#4: Imprimir somente maça e laranja com estrutura de controle
for fruta in compra_frutas_pilha:
    if fruta=="Laranja" or fruta=="Maçã":
        print(fruta)

for fruta in compra_frutas_fila:
    #if fruta =="Laranja" and "Maça": Estrutura nesse formato, não pode, pois sera sempre verdadeira
    # if fruta=="Laranja" or fruta=="Maçã": Essa é correta
    if fruta in("Laranja","Maçã"): #Criei uma tupla aqui os elementos que quero na verificação, in é um operador de pertencimento e se for verdade, é true
        print(fruta)