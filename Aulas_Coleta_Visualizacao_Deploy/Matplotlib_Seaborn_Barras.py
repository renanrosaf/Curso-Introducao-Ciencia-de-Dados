import seaborn as sns
import matplotlib.pyplot as plt

#grafico de barras usando biblioteca
titanic=sns.load_dataset('titanic')

#agrupando por sexo e fazendo a soma dos que sobreviveram
df_por_sexo=titanic.groupby('sex')['survived'].sum().reset_index()

plt.figure(figsize=(8,6))

sns.barplot(data=df_por_sexo,x='sex',y='survived')

plt.show()

# Importa a biblioteca Matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Importa a biblioteca Seaborn para visualização de dados estatísticos
import seaborn as sns


# Carrega o conjunto de dados "titanic" disponível no Seaborn
# Esse dataset contém informações sobre os passageiros do Titanic
titanic = sns.load_dataset('titanic')


# Cria uma figura com tamanho de 8 polegadas de largura por 6 de altura
plt.figure(figsize=(8, 6))


# Cria um histograma para visualizar a distribuição das idades dos passageiros
# data=titanic -> Define o DataFrame que será utilizado
# x='age'      -> A variável (coluna) representada no eixo X será a idade
sns.histplot(
    data=titanic,
    x='age'
)


# Exibe o gráfico na tela
plt.show()

# Importa a biblioteca Seaborn para análise e visualização de dados
import seaborn as sns

# Importa o módulo pyplot da biblioteca Matplotlib para criação dos gráficos
import matplotlib.pyplot as plt


# Carrega o conjunto de dados "titanic" disponível no Seaborn
# O dataset contém informações sobre os passageiros do Titanic
titanic = sns.load_dataset('titanic')


# Agrupa os dados pela coluna "sex" (sexo)
# Para cada grupo (masculino e feminino), soma os valores da coluna "survived"
# Como survived possui valores 0 (não sobreviveu) e 1 (sobreviveu),
# a soma representa a quantidade total de sobreviventes de cada sexo.
df_por_sexo = titanic.groupby('sex')['survived'].sum().reset_index()


# Cria uma figura com tamanho de 8 polegadas de largura por 6 de altura
plt.figure(figsize=(8, 6))


# Cria um gráfico de barras
# data=df_por_sexo -> DataFrame que contém os dados agrupados
# x='sex'          -> Define o sexo no eixo X
# y='survived'     -> Define a quantidade de sobreviventes no eixo Y
sns.barplot(
    data=df_por_sexo,
    x='sex',
    y='survived'
)


# Exibe o gráfico na tela
plt.show()