#1.Lista de Alunos que estão fazendo a aula
alunos=['Renan','João Pedro','Paula','Ana','Lars','Madonna']
print(alunos)

#2.Adicionando alunos 
alunos.append("Maria")
alunos.append("Mario")
alunos.insert(2,"Silvio")
print(alunos)

#3.Removendo alunos da lista:Alunos que desisitiram
alunos.pop(2) #Silvio desistiu
alunos.remove("Mario")
print(alunos)

#4.Conceito de dicionário:
#transformando a lsita de alunos em um dicionário com chave sendo o indice e o valor o nome do aluno
dict_alunos=dict(enumerate(alunos))
print(dict_alunos)

#Pesquisando por um aluno especifico nessa lista: Aluno 1
#nomedicionario[chavedodcionário]
print(dict_alunos[1])