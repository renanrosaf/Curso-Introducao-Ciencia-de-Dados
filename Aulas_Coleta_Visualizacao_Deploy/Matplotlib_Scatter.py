import matplotlib.pyplot as plt

#definindo as váriaveis
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,5,6,8,4,8]

#criando um gráfico de dispersão
plt.scatter(x,y,label='Pontos',color='b',marker='*',s=100)

plt.legend()

plt.show()

# Importa o módulo pyplot da biblioteca Matplotlib
# Ele será utilizado para criar e exibir o gráfico
import matplotlib.pyplot as plt


# Define os valores do eixo X
# Cada elemento representa a coordenada horizontal de um ponto
x = [1, 2, 3, 4, 5, 6, 7, 8]

# Define os valores do eixo Y
# Cada elemento representa a coordenada vertical correspondente ao mesmo índice da lista x
y = [5, 2, 4, 5, 6, 8, 4, 8]


# Cria um gráfico de dispersão (Scatter Plot)
# x        -> Valores do eixo X
# y        -> Valores do eixo Y
# label    -> Nome que aparecerá na legenda
# color    -> Cor dos pontos ('b' = blue/azul)
# marker   -> Formato dos pontos ('*' = estrela)
# s        -> Tamanho dos marcadores (100 pixels²)
plt.scatter(
    x,
    y,
    label='Pontos',
    color='b',
    marker='*',
    s=100
)


# Exibe a legenda utilizando o texto definido em label='Pontos'
plt.legend()


# Exibe o gráfico na tela
plt.show()