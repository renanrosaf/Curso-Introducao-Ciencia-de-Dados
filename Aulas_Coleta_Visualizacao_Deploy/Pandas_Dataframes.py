import pandas as pd

#criando dicionario
data={
    'Nome':['Alice','Bob','Charlie','David'],
    'Idade':[25,30,35,40],
    'Cidade':['São Paulo','Rio de Janeiro','Salvador','Brasilia']
}

df=pd.DataFrame(data)
print(df)

#Posso acessar recursos como:
print(df['Nome'])

#Acessar Dados Dataframe em uma linha
print(df.iloc[0])

#Acessar valor especificos: 1° item do dicionario
print(df.loc[0,'Nome'])