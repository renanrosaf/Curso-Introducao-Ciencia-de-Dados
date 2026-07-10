import matplotlib.pyplot as plt
import seaborn as sns

voos=sns.load_dataset('flights')

voos=voos.pivot(index='month',columns='year', values='passengers')

plt.figure(figsize=(10,6))

sns.heatmap(voos,annot=True, fmt='.0f')

plt.show()


# Importa a biblioteca Matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Importa a biblioteca Seaborn para visualização de dados estatísticos
import seaborn as sns


# Carrega o conjunto de dados "flights" disponível no Seaborn
# O dataset contém as colunas: year (ano), month (mês) e passengers (nº de passageiros)
voos = sns.load_dataset('flights')


# Reorganiza o DataFrame no formato de matriz (pivot)
# index='month'   -> As linhas serão os meses
# columns='year'  -> As colunas serão os anos
# values='passengers' -> Os valores da tabela serão a quantidade de passageiros
voos = voos.pivot(
    index='month',
    columns='year',
    values='passengers'
)


# Cria uma figura com tamanho de 10 polegadas de largura por 6 de altura
plt.figure(figsize=(10, 6))


# Cria o mapa de calor (Heatmap)
# voos      -> DataFrame que será utilizado no gráfico
# annot=True -> Exibe os valores dentro de cada célula
# fmt='.0f' -> Mostra os números sem casas decimais
sns.heatmap(
    voos,
    annot=True,
    fmt='.0f'
)


# Exibe o gráfico na tela
plt.show()