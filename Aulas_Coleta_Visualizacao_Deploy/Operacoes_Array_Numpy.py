import numpy as np

arr1=np.array([10,20,30,40,50])

#soma de 10 aos elementos
print(arr1+10)

#Operações de estatísticas 
print("Media:")
print(np.mean(arr1))

print("Mediana:")
print(np.median(arr1))

print("Desvio Padrão")
print(np.std(arr1))

print("Variância")
print(np.var(arr1))

print("Valor minimo e Máximo:")
min=np.min(arr1)
max=np.max(arr1)
print(f"Valor máximo: {min}")
print(f"Valor máximo: {max}")