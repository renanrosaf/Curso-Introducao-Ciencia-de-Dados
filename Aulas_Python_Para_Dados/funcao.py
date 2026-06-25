#Função recebe uma lista e incrementa ela
#Lista coleção de elementos

def pure_increments(elements, index):#Parâmetors:Elementos e Index(posição de incrementação)
    #elementos: elemento da lista
    #index: indice
    new_elements=elements.copy() #garanto que a lista original não foi alterada,não modifico a lsita original
    #Passando a lista como cópia para new_elements
    new_elements[index]+=1
    return new_elements

#variavel lisa
#Estou criando uma lista de 1 até 9
lista=[1,2,3,4,5,6,7,8,9]

#Efeito Colateral foi provocado
print(f"Lista original: {lista}")

#pure_elements
#chamo a função  e faço print
print(f"Lista incrementada + 1 na posição : {pure_increments(lista,1)}")

