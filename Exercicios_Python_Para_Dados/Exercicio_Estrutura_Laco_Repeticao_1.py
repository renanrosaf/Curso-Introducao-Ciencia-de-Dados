#Quantidade de números pares em um intevalo digitado pelo usuário
n1=int(input("Insira o número incial do intervalo:"))
n2=int(input("Insira o número final do intervalo:"))

#Laço de repetição
for num in range(n1,n2+1):
    if num%2==0:
        print(num)

lista_par=[]

for num in range (n1,n2+1):
    if num%2==0:
        par=num
        lista_par.append(par)
    
print(f"Os números pares no intervalo entre {n1} e {n2} são {lista_par}")