# 💻 Códigos das Aulas

**Introdução e Python para Dados:** Repositório destinado ao armazenamento dos códigos, anotações e exemplos práticos desenvolvidos durante as aulas.

---

## 📝 Aulas 1 e 2: Primeiros Passos com Python

Nestas aulas introdutórias, focou-se na preparação do ambiente de desenvolvimento e nos comandos fundamentais da linguagem Python. Os tópicos abordados nos códigos destas aulas incluem:

* **Configuração do Ambiente:**
    * Instalação do Python.
    * Instalação e configuração do editor VS Code (Visual Studio Code).
* **Sintaxe e Estrutura Básica:**
    * Como realizar e utilizar comentários no código para documentação.
* **Entrada e Saída de Dados:**
    * `print()`: Comando inicial para exibição de mensagens no console (saída de dados).
    * `input()`: Comando para receber informações digitadas pelo usuário (entrada de dados).
* **Variáveis:**
    * Atribuição de valores.
    * Regras e boas práticas de como nomear variáveis corretamente.
* **Manipulação Inicial de Strings (Textos):**
    * Operações básicas com strings.
    * Concatenação (união de duas ou mais strings).
    * Como verificar o tamanho de uma string (quantidade de caracteres, via comando len()).

---

## 📝 Aula 3: Ambiente Virtual (VirtualENV) e Ecossistema Python

Nesta aula, exploramosexploru-se  o conceito de ambientes virtuais e as principais ferramentas que compõem o ecossistema de dados em Python.

### 📦 O que é um Ambiente Virtual?
Um ambiente virtual (VirtualENV) é um diretório isolado que contém uma instalação autônoma do Python, além de pacotes e bibliotecas específicas para um projeto. 
* **Por que usar?** Ele permite o uso de diferentes versões de bibliotecas em projetos distintos na mesma máquina, evitando conflitos de dependências. Facilita o gerenciamento do projeto e mantém a instalação global do Python limpa.
* **Nota:** Você pode criar quantos ambientes virtuais forem necessários (geralmente, cria-se um para cada novo projeto).

### ⚙️ Roteiro: Criação de um Ambiente Virtual
Abaixo está o passo a passo dos comandos utilizados no terminal (Bash/CMD) para criar e gerenciar seu ambiente:

```bash
# 1. Instalar a ferramenta virtualenv (caso ainda não tenha instalado)
pip install virtualenv

# 2. Criar o diretório para o seu novo projeto
mkdir primeiro_projeto_python

# 3. Navegar para dentro do diretório criado
cd primeiro_projeto_python

# 4. Criar o ambiente virtual (daremos o nome de 'venv')
virtualenv venv

# 5. Ativar o ambiente virtual (Comando para Windows)
venv\Scripts\activate 

# 6. Desativar o ambiente virtual (quando terminar de trabalhar no projeto)
deactivate
```


### 📚 Principais Bibliotecas e Ferramentas (Ecossistema de Dados)
Uma visão geral das bibliotecas e tecnologias essenciais apresentadas para a área de dados e desenvolvimento:

**Análise e Visualização de Dados**
* **NumPy:** Focada em computação numérica e manipulação eficiente de arrays/matrizes multidimensionais.
* **Pandas:** Essencial para a manipulação e análise de dados tabulares (utilizando a estrutura de DataFrames).
* **Matplotlib:** Biblioteca fundamental para a criação de gráficos e plotagens 2D.
* **Seaborn:** Interface de alto nível baseada no Matplotlib, focada na criação de gráficos estatísticos atraentes e informativos.

**Inteligência Artificial e Machine Learning**
* **Scikit-Learn:** Biblioteca principal para algoritmos clássicos de Machine Learning (como classificação, regressão e clusterização).
* **PyTorch e TensorFlow:** Frameworks avançados focados em Deep Learning e construção de redes neurais complexas.

**Extração, Interação e Banco de Dados**
* **Jupyter Notebook:** Aplicação web interativa que permite mesclar código Python em execução, textos formatados, equações e visualizações em um único documento.
* **Scrapy e BeautifulSoup:** Ferramentas poderosas para extração e raspagem de dados de páginas da web (Web Scraping).
* **SQLAlchemy:** Uma API/ORM (Object-Relational Mapping) em Python que facilita a integração e manipulação de bancos de dados SQL utilizando código Python.

**Versionamento de Código**
* **Git:** Sistema de controle de versão que registra o histórico de alterações do código e permite a ramificação (branches) do projeto.
* **GitHub:** Plataforma em nuvem baseada no Git para hospedagem de código, facilitando o portfólio e a colaboração em equipe.


## 📝 Aula 4: Estruturas de Dados, Módulos e Pacotes

Nesta aula, abordamos as principais estruturas de dados nativas do Python e como estruturar e organizar projetos utilizando módulos e pacotes.

### 🧱 Estruturas de Dados

* **Listas:** Coleções de itens utilizadas para armazenar múltiplos valores em uma única variável.
    * **Características:** São estruturas **mutáveis** (podem ser alteradas após a criação) e **ordenadas**, definidas utilizando colchetes `[]`.
    * **Conceitos:** Definição, criação e acesso de elementos via índice.
    * **Inserção:** Adição de elementos em posições específicas (`insert()`) ou ao final da lista (`append()`).
    * **Remoção:** Exclusão de elementos pelo valor (`remove()`) ou pelo índice/último elemento (`pop()`).

* **Tuplas:** Coleções de itens utilizadas para armazenar múltiplos valores, com funcionamento semelhante ao das listas.
    * **Características:** São estruturas **ordenadas**, porém **imutáveis** (seus elementos não podem ser alterados após a criação), definidas utilizando parênteses `()`.
    * **Conceitos:** Definição, criação, acesso de elementos via índice e criação de listas contendo tuplas.

* **Dicionários:** Estruturas que mapeiam pares de **Chave-Valor**, definidas utilizando chaves `{}`.
    * **Características:** Semelhantes a listas, mas os elementos não são acessados por índices numéricos, e sim por chaves únicas (que devem ser de um tipo imutável). Eles facilitam a busca, adição e remoção de itens de forma muito eficiente.
    * **Conceitos:** Definição de chave/valor, conversão de lista de tuplas para dicionário (usando a função `dict()`), acesso aos valores, além da adição e remoção referenciando a chave.

---

### 📦 Organização e Reutilização de Código

Mecanismos que permitem estruturar e reaproveitar o código de maneira eficiente:

* **Módulo:** Um arquivo Python (extensão `.py`) que contém definições de funções, classes e variáveis que possuem relação entre si.
* **Pacote:** Uma coleção de módulos organizados dentro de um diretório. Para que o Python reconheça esse diretório como um pacote, ele deve conter um arquivo chamado `__init__.py`.

**Sintaxe Básica de Importação (`import`):**

```python
# Importando um módulo inteiro
import meu_modulo

# Importando um módulo e atribuindo um "apelido" (alias)
import pandas as pd

# Importando apenas uma função específica de dentro de um módulo
from meu_modulo import minha_funcao

# Importando apenas um módulo específico de dentro de um pacote
import meu_pacote.meu_modulo

# Importando uma função específica de um módulo que está dentro de um pacote
from meu_pacote.meu_modulo import minha_funcao
```

## 📝 Aulas 6: Tipos, Estruturas de Dados e Fluxos de Controle 

Nestas aulas, exploramos os tipos de dados fundamentais do Python, além de como organizar e manipular informações de forma eficiente através de estruturas lineares (Pilhas e Filas) e do controle de fluxo do código.

### 🔡 Tipos de Dados em Python
Uma visão geral dos principais tipos de dados e estruturas nativas suportadas pela linguagem:

* **Números:**
    * **Inteiros (`int`):** Números inteiros, sem casas decimais (ex: 1, 100, -5).
    * **Números de Ponto Flutuante (`float`):** Números reais, com casas decimais (ex: 3.14, -0.5).
    * **Números Complexos (`complex`):** Números com parte real e imaginária.
* **Strings (`str`):** Sequências de caracteres utilizadas para representar textos.
* **Booleanos (`bool`):** Representam valores lógicos: `True` (Verdadeiro) ou `False` (Falso).
* **Listas (`list`):** Sequências mutáveis de elementos.
* **Tuplas (`tuple`):** Sequências imutáveis de elementos.
* **Conjuntos (`set`):** Coleções não ordenadas de elementos únicos (não permitem valores duplicados).
* **Dicionários (`dict`):** Coleções de dados organizadas em pares de Chave-Valor.

---

### 🧱 Tipos de Estruturas de Dados: Pilhas e Filas
Ambas são baseadas em listas para organizar informações, mas se diferenciam fortemente pela regra de entrada e saída dos elementos:

* **Pilha (Stack):**
    * **Comportamento:** Opera no modelo **LIFO** (*Last In, First Out* - O último elemento a entrar é o primeiro a sair).
    * **No Python:** A estrutura de **Lista** nativa no formato padrão do Python se comporta exatamente como uma Pilha. Ao utilizarmos os métodos `append()` para adicionar e `pop()` para remover, estamos sempre operando no final da lista.

* **Fila (Queue):**
    * **Comportamento:** Opera no modelo **FIFO** (*First In, First Out* - O primeiro elemento a entrar é o primeiro a sair). É o mesmo funcionamento de uma fila de banco ou supermercado.
    * **No Python:** Embora seja possível usar uma lista comum, geralmente utilizamos outras bibliotecas nativas (como `collections.deque`) para manipular filas de forma mais otimizada e eficiente computacionalmente.

## 📝 Aula 7: Fluxos de Controle (Condicionais e Repetições) 

Nesta etapa, focamos nas estruturas que ditam o fluxo de execução de um programa em Python: como o código toma decisões e como ele repete ações (loops).

### 🔀 Estruturas Condicionais (Tomada de Decisão)
Permitem que o programa execute diferentes blocos de código dependendo de uma condição lógica (Verdadeiro ou Falso).

* **`if` (Se):** Avalia a primeira condição. Se for verdadeira, executa o bloco.
* **`elif` (Se não, se):** Permite encadear múltiplas condições adicionais caso as anteriores sejam falsas.
* **`else` (Se não):** O bloco executado por padrão caso todas as condições anteriores (`if` e `elif`) sejam falsas.

**Exemplo prático: Estruturas condicionais**
```python
nota = 8.5

if nota >= 7:
    print("Aprovado! Acima da média.")
elif nota >= 5:
    print("Em recuperação.")
else:
    print("Reprovado! Não atingiu a média.")
```

### 🔁 Estruturas de Repetição (Loops)

Servem para automatizar tarefas repetitivas, executando um mesmo bloco de código diversas vezes.

#### 1. Loop for (Para):

Conceito: Utilizado para iterar (percorrer) sobre uma sequência de dados, como listas, tuplas, strings ou dicionários.

Uso: Executa uma ação específica para cada item dentro dessa sequência. É ideal quando sabemos a quantidade de vezes que o loop deve rodar ou o tamanho da coleção.
frutas = ["maçã", "banana", "uva"]

**Exemplo prático com lista: Iteração sobre a lista, passando por cada item**
```python
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
```

#### 2. Loop while (Enquanto):

Conceito: Repete a execução de um bloco de código continuamente enquanto uma condição específica for verdadeira (True).

Uso: Muito útil para automatizar processos onde não sabemos exatamente quantas iterações serão necessárias, dependendo de um evento de parada.

**Exemplo prático com loop while**
``` python
contador = 0

# Repete o bloco enquanto o contador for menor que 3
while contador < 3:
    print(f"O contador atual é: {contador}")
    contador += 1 # Incrementa o contador para evitar um "loop infinito"
```

## 📝 Aula 8 e 9: Ampliando Conhecimentos de Estruturas de Dados e Fluxos de Controle

Nesta aula, aprofundamos o entendimento sobre como o Python toma decisões complexas, com foco no encadeamento de múltiplas condições e na importância estrutural do código.

### 📐 Indentação e Aninhamento (A Estrutura do Código)
Ao contrário de muitas linguagens que usam chaves `{}` para delimitar blocos, o Python depende da **indentação** (o recuo ou espaçamento no início da linha).
* **Aninhamento:** É o ato de colocar um comando dentro de outro comando "superior". 
* **Importância:** A indentação é essencial e obrigatória para que o `if` seja funcional. É através desse recuo que o Python entende se um bloco de código faz parte de uma condição ou se está fora dela.

### 🛤️ Encadeamento de Condições
Podemos construir fluxos de controle detalhados que avaliam várias situações em sequência. O programa testará as opções de cima para baixo até encontrar uma que obedeça à condição:

* **O papel do `else`:** Ele é o "último recurso". O bloco de código dentro do `else` será executado **apenas** depois de todas as condições anteriores terem sido testadas e falhado. Ou seja, se o `if` e todos os `elif` não forem atendidos, a ação do `else` entra em cena.

**Exemplo Prático Corrigido:**
```python
acao = 5

if acao == 1:
    print("Ação 1 ativada.")
    
elif acao == 2:
    print("Ação 2 ativada.")
    
elif acao > 2 and acao < 10:
    # Múltiplas validações na mesma linha utilizando o operador lógico 'and'
    print("Ação 3 ativada (valor está entre 3 e 9).")
    
else:
    # Se nenhuma das condições acima for verdadeira, o else é executado
    print("Ação 4 ativada: Nenhuma condição anterior foi atendida.")

```

### 🔁 Aprofundando em Laços de Repetição (Loops)

**1. O Laço `for`**
Utilizado para iterar (percorrer) cada elemento individual de uma coleção (como listas, tuplas ou strings). O laço extrai um item por vez da coleção e executa uma ação para ele.

 **Sintaxe básica:**
  ```python
  for variavel_de_busca in colecao:
      # Ação a ser executada para cada item
 ```
**2. Uso da função range()**

A função range() retorna uma sequência de números. Ela é ideal para quando precisamos executar um loop um número específico de vezes ou percorrer os índices de uma lista.

Comportamento: range(tamanho) gera números começando do 0 até o tamanho - 1. O último número nunca é incluso.

  **Exemplo de estrutura:**

```Python
# Vai imprimir os números 0, 1, 2, 3 e 4
for i in range(5):
    print(i) 
```

**3. O Laço while:**

Repete a execução de um bloco de código continuamente enquanto uma condição específica for avaliada como verdadeira (True).

Cuidado com o Loop Infinito: Como o while só para quando a condição deixa de ser atendida, é essencial criar um critério de parada. Para isso, geralmente utilizamos uma variável de controle e a incrementamos a cada iteração (ex: i += 1).

 **Exemplo de estrutura:**

```Python
i = 0
while i < 5:
    print(f"Iteração número: {i}")
    i += 1 # Incrementa o valor de 'i' para evitar um loop infinito
```

**4.A Estrutura "Switch Case" em Python**

Em linguagens como C ou Java, o switch-case é muito comum. No Python, durante muito tempo, essa estrutura não existia de forma nativa e precisava ser simulada utilizando encadeamentos de if-elif-else ou Dicionários.

Simulação utilizando if-elif-else:

```Python
opcao = 2

if opcao == 1:
    print("Ação da Opção 1")
elif opcao == 2:
    print("Ação da Opção 2")
elif opcao == 3:
    print("Ação da Opção 3")
else:
    print("Opção inválida: Padrão (Default)")
```

Nota de Atualização: A partir da versão 3.10 do Python, foi introduzida a estrutura estrutural de correspondência de padrões chamada match-case, que funciona de maneira nativa e muito semelhante ao switch-case tradicional.

## 📝 Aula 10 e 11: Funções, Programação Funcional e Tratamento de Erros

Nesta aula, aprendemos como criar blocos de código reutilizáveis (Funções), exploramos diferentes formas de pensar e estruturar um código (Paradigms) e introduzimos conceitos de Programação Funcional e tratamento de exceções.

### 🛠️ Funções em Python
Uma função é um pedaço de código encapsulado que executa uma tarefa específica. Ela permite que você chame a mesma lógica várias vezes, evitando repetição e dividindo o programa em partes menores e organizadas. Dentro de uma função, podemos colocar vários blocos de comando (como `if/else`, loops `for` e `while`).

* **`def`:** Palavra-chave utilizada para definir (criar) a função.
* **Parâmetros:** Variáveis que a função recebe para processar (`a` e `b` no exemplo).
* **`return`:** Define a ação final da função e o valor que ela irá devolver (retornar) para o programa.

**Exemplo Prático:**
```python
# Definindo uma função que soma dois números quaisquer
def somar(a, b):
    return a + b  # Ação da função: retorna a soma dos parâmetros

# Chamando a função e guardando o resultado em uma variável
resultado = somar(2, 3) 

# Isso vai imprimir 5
print(resultado)
```
### 🧠 Paradigmas de Programação

Um paradigma de programação é uma abordagem específica ou estilo de programar. É um conjunto de princípios, regras e padrões para escrever código, onde cada paradigma oferece uma perspectiva diferente para resolver problemas.

Imperativo: Foca em como o programa deve fazer algo. Baseia-se em instruções passo a passo que alteram o estado do programa.

Procedural: Um subtipo do paradigma imperativo, onde o código é agrupado em procedimentos (ou rotinas/funções).

Orientado a Objetos (POO): Foco na criação de "objetos" que representam entidades e conceitos do mundo real. Baseia-se na definição de Atributos (características/dados) e Métodos (ações/comportamentos).

Declarativo: Foca no que deve ser alcançado, e não no passo a passo de como fazer. Pode ter um custo computacional mais alto dependendo da implementação. A Programação Funcional faz parte deste paradigma.

### ⚙️ Programação Funcional (FP)
A Programação Funcional é um paradigma que trata a computação como a avaliação de funções matemáticas.

Evitando "Efeitos Colaterais" (Side Effects): Um efeito colateral ocorre quando uma função altera dados ou o estado do programa fora do seu próprio escopo. A FP busca evitar isso.

Funções Puras: São funções que, para uma mesma entrada, sempre retornam o mesmo resultado, sem modificar o valor dos parâmetros originais ou depender de dados externos mutáveis.

Funções de Alta Ordem (Higher-Order Functions): São funções que podem receber outras funções como parâmetros ou retornar funções como resultado.

O Python possui funções nativas (built-ins) para facilitar operações, como print(), e clássicas funções puras de alta ordem herdadas do conceito funcional, como map(), filter() e funções de ordenação como sorted().


### 🚨 Lidando com Erros e Exceções (Try / Except / Finally)

É fundamental saber lidar com erros na programação. Tratar essas falhas adequadamente impede interrupções abruptas (quando o programa "quebra"), exibe mensagens mais amigáveis ao usuário e torna o código muito mais robusto, limpo e confiável.

Existem dois tipos principais de erros que encontramos ao programar:

* **Erros de Sintaxe (Syntax Errors):** São erros na escrita do código (como esquecer dois pontos `:` ou errar a indentação). O próprio interpretador do Python identifica e aponta o erro antes mesmo de o código rodar.
* **Exceções (Exceptions):** Ocorrem durante a execução do programa. A sintaxe do código está totalmente correta, mas acontece um imprevisto (ex: o usuário digita uma letra onde era esperado um número, ocorre uma divisão por zero, ou o sistema tenta acessar uma página que está fora do ar). 

Se uma exceção ocorre e não é tratada, o Python interrompe a execução imediatamente. Para evitar isso, utilizamos os blocos de tratamento.

#### 🧱 A Estrutura de Tratamento
* **`try` (Tentar):** Bloco onde colocamos o código principal que será testado. O programa tenta executá-lo normalmente.
* **`except` (Exceto):** Se ocorrer uma exceção dentro do `try`, o Python pula para este bloco para "capturar" e tratar o erro. Podemos ter vários blocos `except` para tratar falhas diferentes de maneiras específicas.
* **`finally` (Finalmente):** Bloco opcional que é executado **sempre**, independentemente de ter ocorrido uma exceção ou não. É muito utilizado para liberar recursos (como fechar um arquivo aberto ou encerrar a conexão com um banco de dados).

**Exemplo Prático Completo:**
```python
try:
    # Tenta executar este bloco de código
    numero = int(input("Digite um número para dividir 10: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")

except ZeroDivisionError:
    # Captura o erro específico de tentar dividir por zero
    print("Erro: Não é possível dividir um número por zero!")

except ValueError:
    # Captura o erro do usuário ter digitado um texto ao invés de um número
    print("Erro: Você deve digitar um número inteiro válido!")

finally:
    # Executa sempre, dando certo ou errado
    print("Fim da operação de divisão.")

```
#### 🛠️ Exceções Personalizadas

Além das exceções nativas do Python (como ValueError ou ZeroDivisionError), você pode criar as suas próprias exceções para lidar com regras de negócio específicas do seu projeto.

Para isso, é necessário utilizar o paradigma de Programação Orientada a Objetos (POO), criando uma classe personalizada que herda as características da classe base Exception do Python.