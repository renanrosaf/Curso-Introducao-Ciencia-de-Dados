import matplotlib.pyplot as plt

# #criando um grafico de linha
# plt.plot([1,3,5],[2,6,7])

# #exibe o gráfico
# plt.show()

#criando gráfico de barras
x=['Maças','Laranja','Uva','Figos','Banana']
y=[5,3,7,4,6]

plt.bar(x,y,color='green')

#adicionando rotutlos
plt.xlabel('Frutas') #rotulo eixo x
plt.ylabel('Quantidade') #rotulo eixo y
plt.title('Quantidade de Frutas') #titulo do gráfico

#Mostrando o gráfico
plt.show()