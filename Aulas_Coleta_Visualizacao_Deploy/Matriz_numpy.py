import numpy as np

#Criando a matriz
arr2=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#Acessando elemento de uma matriz:
print(arr2[1,2]) #saida esperado é o numero 6

#informações da matriz:
print(f"Shape da matriz: {arr2.shape}")
print(f"Numero de elementos: {arr2.size}")
print(f"Tipo  de elementos: {arr2.dtype}")