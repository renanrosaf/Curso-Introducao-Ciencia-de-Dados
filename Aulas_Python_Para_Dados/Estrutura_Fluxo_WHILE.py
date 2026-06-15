#coleção de planetas
#Laço repetição For para obter cada elemento da lista
planetas=['Mercúrio','Vênus','Terra','Marte','Jupiter','Saturno','Urano','Netuno']

for planeta in planetas: #variavel planeta recebe o valor de cada planeta na coleção de planetas
    print('Planeta:', planeta)

#Função RANGE:
#  Número 5 se transforme em uma lsita que varie de 0 até 5, porém o 5 é exclusivo, ele não é impresso 
for i in range(5):
    print ("i=",i)

for i in range(10): #Numero inserido no range é quantidade de elementos 
    print ("i=",i)


#Laço While, condição que repete laço de código quando condição for verdadeira
i=0
#preciso de um contador para evitar Loop Infinito

while i<10:
    print(i,end='') #End: imprime todos os valores em uma linha só
    i+=1 #variavel aqui vai modificar o valor de i
    #+= incremento i=i+1



