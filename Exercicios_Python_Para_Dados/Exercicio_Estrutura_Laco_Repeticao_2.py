#Codificador de Números Pares:
int_1=int(input("Digite o número incial do intevalo: "))
int_2=int(input("Digite o número final do intervalo: "))

lista_par=[]
for par  in range(int_1,int_2+1):
    if par%2==0:
       lista_par.append(par)

print(f"Os números pares entre {int_1} e {int_2} são: {lista_par}")