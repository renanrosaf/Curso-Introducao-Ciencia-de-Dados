import pandas as pd

#Dataframe contendo informações dos funcionários
funcionarios={
    'nome':['João','Marta','Ana','Mario'],
    'Endereco':['Rua 708','Rua 500','Rua 900','Rua 1001'],
    'Data_Nascimento':['21/07/1995','04/04/1986','18/01/2000','31/12/2005'],
    'Data_Admissao':['12/03/2025','04/08/2024','18/09/2019','04/12/2017'],
    'Salario_R$':[5500,4000.34,9987.40,3500],
    'Cargo':['Gerente','Supervisor','Chefia','Analista']
}

#Mostrando o dataframe
df=pd.DataFrame(funcionarios)

print(df)

#Todas as linhas da coluna de admissão
print(df.loc[:,'Data_Admissao'])