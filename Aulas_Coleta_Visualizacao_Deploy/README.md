## 📝 Aula 1: Mineração, Preparação e Estatística para Ciência de Dados

A **Ciência de Dados** envolve a coleta, análise e interpretação de dados com o intuito de obter *insights* valiosos e embasar a tomada de decisões. Dentro desse contexto, a mineração de dados, a preparação e a estatística aplicada desempenham papéis fundamentais para garantir que as informações extraídas sejam confiáveis e úteis.

---

### ⛏️ Mineração de Dados (Data Mining)
A mineração de dados é o processo de explorar grandes conjuntos de dados para encontrar anomalias, padrões e correlações que permitam prever resultados. 

### 🛤️ Etapas de Mineração de Dados

Para que a análise seja eficiente e gere valor real, o processo de mineração de dados segue um fluxo de trabalho estruturado. As principais etapas são:

1. **Definição do Problema:** Entender claramente qual é o objetivo do projeto, a pergunta de negócio que precisa ser respondida ou o problema que a inteligência de dados deve resolver.
2. **Coleta de Dados:** Obtenção das informações necessárias a partir de diversas fontes (bancos de dados relacionais, APIs, web scraping, arquivos CSV, etc.).
3. **Pré-processamento e Preparação dos Dados:** Etapa mais crítica e demorada. Envolve a limpeza dos dados (tratar valores nulos, remover duplicatas) e a transformação das informações para que os algoritmos consigam processá-las corretamente.
4. **Análise Exploratória:** Investigação inicial dos dados utilizando estatística descritiva e visualizações. O objetivo é encontrar padrões preliminares, identificar anomalias e entender a distribuição das variáveis.
5. **Modelagem:** Aplicação de técnicas matemáticas e algoritmos de Machine Learning (como classificação, regressão ou clustering) para construir modelos capazes de prever resultados ou extrair insights profundos.
6. **Avaliação dos Resultados:** Teste e validação do modelo criado para garantir que ele possui uma boa precisão e que realmente resolve o problema definido na primeira etapa.

### As principais tarefas dentro da mineração incluem:
* **Clustering (Agrupamento):** Agrupar dados semelhantes sem um rótulo prévio.
* **Classificação:** Categorizar novos dados com base em padrões de dados históricos.
* **Associação:** Identificar regras que mostram como os itens estão associados (ex: quem compra pão, costuma comprar manteiga).

### 🛠️ Principais Ferramentas do Ecossistema Python
Abaixo, as bibliotecas essenciais utilizadas no processo de mineração e análise:

| Biblioteca | Principal Função na Ciência de Dados |
| :--- | :--- |
| **Pandas** | Manipulação, tratamento e análise estruturada de dados. |
| **NumPy** | Computação numérica e tratamento de arrays multidimensionais. |
| **Scikit-Learn** | Implementação de algoritmos de Machine Learning e mineração. |
| **Matplotlib / Seaborn** | Visualização de dados por meio de gráficos estáticos ou interativos. |

---

### 🛤️ Etapas do Processo de Dados

Para que a análise seja eficiente, os dados precisam passar por um fluxo de trabalho estruturado:

1. **Reunir (Coleta) de Dados:** Extração de dados de fontes diversas (bancos de dados, APIs, arquivos). O foco inicial é garantir a obtenção das informações.
2. **Preparação e Limpeza:** Etapa crítica onde os dados são ajustados para ficarem prontos para análise. Envolve tratar valores nulos, remover duplicatas e garantir a integridade das informações.
3. **Transformação de Dados:** Conversão de formatos, normalização e padronização para que os algoritmos consigam processar as informações corretamente.
4. **Análise Exploratória de Dados (EDA):** Uso de estatística descritiva para interpretar os dados pela primeira vez. Aqui analisamos a média, mediana, desvio padrão e a distribuição de probabilidades das variáveis.

---

### 🐼 A Biblioteca Pandas: Estruturas e Exemplos

O **Pandas** é a biblioteca central para a análise de dados em Python. Ele facilita a importação, limpeza e manipulação de informações. Para utilizá-lo, é necessário realizar a instalação via terminal (`pip install pandas`) e importá-lo no código.

O Pandas trabalha fundamentalmente com duas estruturas de dados:

#### 1. Series
Uma Series é um array unidimensional capaz de armazenar dados de qualquer tipo (inteiros, strings, floats). Pode ser comparada a uma única coluna de uma planilha de Excel.

```python
import pandas as pd

# Criando uma Series a partir de uma lista comum do Python
notas = pd.Series([8.5, 9.0, 7.5, 10.0], index=['Prova 1', 'Prova 2', 'Prova 3', 'Prova 4'])

print(notas)

```

#### 2. DataFrame
O DataFrame é uma estrutura bidimensional (linhas e colunas), muito semelhante a uma tabela de banco de dados relacional ou uma planilha. É a estrutura mais importante e utilizada do Pandas.
O comando pd.DataFrame() aceita vários argumentos, sendo os principais: data (os dados em si), index (nome das linhas) e columns (nome das colunas).

``` Python
import pandas as pd

# Criando um dicionário no Python
dados_alunos = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro'],
    'Idade': [22, 25, 23, 21],
    'Curso': ['Engenharia', 'Dados', 'Engenharia', 'Automação']
}

# Convertendo o dicionário em um DataFrame
df = pd.DataFrame(data=dados_alunos)

print(df)
```

### 📂 Leitura de Arquivos CSV
O Pandas aceita arquivos em diversos formatos (Excel, JSON, SQL). Uma das operações mais comuns é a leitura de arquivos delimitados por vírgula (CSV) utilizando operações semelhantes à álgebra relacional.

Diretório Local: Se o arquivo CSV estiver na mesma pasta que o seu script Python, a leitura é mais rápida e basta inserir o nome do arquivo.

Caminho Absoluto: Caso o arquivo esteja em outra pasta, é necessário passar o caminho completo (ex: C:/pasta/arquivo.csv).

Exemplo prático de leitura e visualização inicial:

Python
import pandas as pd

# Lê o arquivo CSV e converte automaticamente em um DataFrame
df_vendas = pd.read_csv('vendas.csv')

# O método .head() exibe as 5 primeiras linhas do DataFrame
# É excelente para dar uma olhada rápida na estrutura dos dados recém-carregados
print(df_vendas.head())

## 📝 Aula 2: Numpy: Objetos, Vetorização e Fundamentos da Estatística

### 🔢 Biblioteca NumPy: Arrays e Computação Numérica

O **NumPy** (Numerical Python) é uma das bibliotecas fundamentais mais utilizadas em Ciência de Dados. Enquanto o Pandas brilha na manipulação de dados tabulares (DataFrames), o NumPy é focado em cálculos matemáticos de alta performance, manipulação de arrays e matrizes multidimensionais, além de oferecer ferramentas avançadas de álgebra linear.

Para utilizá-lo, a convenção padrão de importação é:
```python
import numpy as np

```

### 🧱 O Objeto Principal: ndarray
A estrutura central do NumPy é o ndarray (n-dimensional array). Diferente de uma lista comum do Python, um array do NumPy exige que todos os elementos sejam do mesmo tipo de dado (geralmente números). Isso permite que o computador processe as informações muito mais rápido.

Array Unidimensional (1D): Semelhante a uma lista simples ou um vetor matemático.

Array Bidimensional (2D): Semelhante a uma lista de listas, uma matriz matemática ou uma tabela no Excel (composta por linhas e colunas).

Criando e Acessando Arrays:
A indexação em Python sempre inicia no índice 0. Para acessar elementos em matrizes (2D), utilizamos o formato [linha, coluna].

``` Python
import numpy as np

# 1. Criando e acessando um Array 1D (Vetor)
vetor = np.array([10, 20, 30, 40])
print(f"Primeiro elemento do array: {vetor[0]}") # Saída: 10

# 2. Criando e acessando um Array 2D (Matriz)
# Possui 2 linhas e 3 colunas
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Acessando o elemento da segunda linha (índice 1) e terceira coluna (índice 2)
print(f"Elemento [1, 2]: {matriz[1, 2]}") # Saída: 6
```

### 🏷️ Atributos do Objeto ndarray
Você pode verificar as características de um array utilizando seus atributos nativos:

shape: Retorna o formato do array (número de linhas e colunas).

size: Retorna o número total de elementos presentes no array.

dtype: Retorna o tipo de dado armazenado no array (ex: int64, float64).

```Python
import numpy as np

matriz = np.array([[1.5, 2.0], [3.5, 4.0]])

print(f"Formato (shape): {matriz.shape}") # Saída: (2, 2)
print(f"Total de elementos (size): {matriz.size}") # Saída: 4
print(f"Tipo de dado (dtype): {matriz.dtype}") # Saída: float64
```

### ✖️ Operações Matemáticas: Arrays vs Matrizes
O NumPy lida de forma diferente com multiplicações dependendo do método utilizado:

Multiplicação de Arrays (Elemento por Elemento): Multiplica os valores que estão na mesma posição.

Multiplicação de Matrizes (Álgebra Linear): Segue as regras da álgebra linear (o número de colunas da 1ª matriz deve ser igual ao número de linhas da 2ª). No NumPy, utilizamos o símbolo @ ou a função np.dot().

``` Python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicação elemento por elemento (1*5, 2*6, 3*7, 4*8)
mult_array = A * B 

# Multiplicação matricial (Álgebra Linear)
mult_matriz = A @ B 
```

### 📊 Operações Estatísticas Básicas
O NumPy possui métodos otimizados para extrair informações estatísticas diretamente dos arrays ou matrizes.

Média (np.mean): A soma de todos os valores dividida pela quantidade de elementos. Representa o valor central dos dados.

Mediana (np.median): O valor que separa a metade maior e a metade menor de um conjunto de dados. Menos sensível a valores extremos que a média.

Variância (np.var): Mede o quão dispersos os dados estão em relação à média.

Desvio Padrão (np.std): É a raiz quadrada da variância. Indica o quanto os valores, em média, se desviam do valor médio (quanto menor, mais consistentes são os dados).

```Python
import numpy as np

dados = np.array([10, 12, 23, 23, 16, 23, 21, 16])

print(f"Média: {np.mean(dados)}")
print(f"Mediana: {np.median(dados)}")
print(f"Variância: {np.var(dados)}")
print(f"Desvio Padrão: {np.std(dados):.2f}")
```

### 🔍 Encontrando Valores Mínimos e Máximos
Para localizar os extremos em um conjunto de dados, o NumPy oferece funções diretas para encontrar o valor em si ou a posição (índice) onde ele se encontra.

``` Python
import numpy as np

vendas = np.array([150, 300, 50, 400, 200])

# Retornam o valor real
print(f"Maior valor de venda: {np.max(vendas)}") # Saída: 400
print(f"Menor valor de venda: {np.min(vendas)}") # Saída: 50

# Retornam a posição (índice) onde o valor está
print(f"Índice da maior venda: {np.argmax(vendas)}") # Saída: 3
print(f"Índice da menor venda: {np.argmin(vendas)}") # Saída: 2
```
## 📝 Aula 3: Visualização Eficaz de Dados (Data Viz)

A **Visualização de Dados (Data Viz)** é a representação gráfica de informações. O objetivo principal é transformar grandes e complexos conjuntos de dados em gráficos, tabelas e diagramas que possam ser processados visualmente e compreendidos com facilidade pelo cérebro humano.

O grande lema da visualização de dados é **transformar dados brutos em decisões acionáveis.**

### 🎯 A Importância da Visualização de Dados
* **Compreensão de Dados:** Permite entender rapidamente a estrutura e a distribuição da base de dados.
* **Identificação de Padrões e Correlações:** Facilita a descoberta de tendências (ex: como uma variável afeta a outra ao longo do tempo).
* **Detecção de Anomalias (Outliers):** Valores que fogem drasticamente do padrão tornam-se imediatamente visíveis em um gráfico.
* **Comunicação Eficaz:** Traduz análises estatísticas complexas para um formato visual que gestores e equipes não-técnicas possam interpretar.
* **Suporte à Tomada de Decisão:** Fornece a base visual necessária para escolhas estratégicas seguras.

---

### 📚 Principais Bibliotecas em Python
O ecossistema Python possui excelentes ferramentas para Data Viz. As três principais são:
1. **Matplotlib:** A biblioteca pioneira e mais fundamental (foco desta aula).
2. **Seaborn:** Construída sobre o Matplotlib, focada em gráficos estatísticos mais bonitos e fáceis de gerar.
3. **Plotly:** Focada em gráficos interativos (dashboards web).

---

### 📊 Matplotlib: A Base da Visualização
O **Matplotlib** é uma biblioteca de plotagem 2D poderosa, originalmente projetada com uma sintaxe muito semelhante ao software MATLAB. Ela possui uma API orientada a objetos que permite um controle minucioso sobre cada elemento do gráfico.

*A documentação oficial oferece guias excelentes como "Plot Types" e "Examples", cobrindo visualizações como `plot` (linhas), `scatter` (dispersão), `bar` (barras), `stem`, `step` e `fill_between`.*

**Instalação e Importação Padrão:**
```bash
pip install matplotlib
Python
import matplotlib.pyplot as plt
```

### 1. Gráfico de Linhas (Line Plot)
Ideal para mostrar a evolução de uma variável contínua ao longo do tempo (tendências).

``` Python
import matplotlib.pyplot as plt

# Simulando dados de um equipamento
tempo = [1, 2, 3, 4, 5]
tensao_volts = [220, 222, 218, 225, 221]

plt.plot(tempo, tensao_volts, color='red', marker='o', label='Tensão da Rede')
plt.title("Monitoramento de Tensão ao Longo do Tempo")
plt.xlabel("Tempo (Horas)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.show() # Comando obrigatório para exibir o gráfico na tela
```

### 2. Gráfico de Dispersão (Scatter Plot)
Utiliza pontos para representar valores de duas variáveis numéricas diferentes. É a melhor escolha para descobrir se existe correlação entre duas métricas.

``` Python
import matplotlib.pyplot as plt

# Avaliando se a temperatura afeta a corrente de um motor
temperatura = [30, 35, 40, 45, 50, 55, 60]
corrente = [10.5, 10.8, 11.2, 12.0, 13.5, 15.0, 17.2]

plt.scatter(temperatura, corrente, color='blue', label='Leituras do Motor')
plt.title("Relação: Temperatura vs Corrente")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Corrente (A)")
plt.legend()
plt.show()
```

### 🌊 Seaborn: Visualização Estatística de Alto Nível
O Seaborn trabalha em conjunto com o Pandas e o Matplotlib. Ele requer menos linhas de código para gerar gráficos complexos e já vem com paletas de cores e estilos pré-configurados muito elegantes.

Instalação e Importação:

```Bash
pip install seaborn
Python
import seaborn as sns
import matplotlib.pyplot as plt
```

### 1. Gráfico de Barras (Bar Plot)
Usado para comparar quantidades entre diferentes categorias.

```Python
import seaborn as sns
import matplotlib.pyplot as plt


# Comparando acionamentos de diferentes sensores PNP na linha de montagem
dados_sensores = {'Sensor': ['Sensor A', 'Sensor B', 'Sensor C'], 'Acionamentos': [450, 320, 500]}

sns.barplot(x='Sensor', y='Acionamentos', data=dados_sensores, palette='viridis')
plt.title("Total de Acionamentos por Sensor")
plt.show()
``` 
### 2. Histograma (Hist Plot)
Representa a distribuição de frequência de uma variável contínua. Ele agrupa os dados em "caixas" (bins) para mostrar onde os valores estão mais concentrados.

```  Python
import seaborn as sns
import matplotlib.pyplot as plt

# Distribuição de peso de chapas de aço bifásicas (em kg)
pesos_chapas = [15.2, 15.5, 15.1, 14.8, 15.3, 15.2, 16.0, 15.4, 15.2, 14.9]

sns.histplot(pesos_chapas, bins=5, kde=True, color='purple')
plt.title("Distribuição de Peso das Chapas Automotivas")
plt.xlabel("Peso (kg)")
plt.show()
``` 

### 3. Mapa de Calor (Heatmap)
Representa dados em um formato de matriz, utilizando um gradiente de cores para indicar a intensidade ou magnitude dos valores. É amplamente utilizado para visualizar matrizes de correlação (para ver quais variáveis de uma base de dados influenciam mais umas às outras).

```  Python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Simulando uma matriz de correlação entre variáveis industriais
dados = {
    'Temperatura': [1.0, 0.8, -0.2],
    'Pressão': [0.8, 1.0, -0.5],
    'Umidade': [-0.2, -0.5, 1.0]
}
df_correlacao = pd.DataFrame(dados, columns=['Temperatura', 'Pressão', 'Umidade'], index=['Temperatura', 'Pressão', 'Umidade'])

# Gerando o heatmap
sns.heatmap(df_correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Mapa de Calor: Correlação de Variáveis")
plt.show()
``` 