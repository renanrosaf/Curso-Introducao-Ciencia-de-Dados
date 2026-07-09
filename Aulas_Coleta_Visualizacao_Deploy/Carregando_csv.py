import pandas as pd

#importando dados csv
df=pd.read_csv('data.csv')

# a partir dfe um diretório
#df=pd.read_csv('/caminho/para/o/diretorio/dados/csv')

#print informalões no arquivo csv
print(df)

#Exibindo as primeiras linhas do arquivo csv
print(df.head())

#arquvio csv deve estar no mesmo diretorio do arquivo python