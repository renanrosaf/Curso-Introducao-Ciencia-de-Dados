#1: CRIANDO A LISTA DE ALUNOS
alunos=['Hamilton','Bruce','Janet','Bruna','Amy','Ozzy']
print(f"Lista de alunos matriculados: {alunos}")
print(20*"-")

#2: ADICIONAR NOVOS ALUNOS QUE ESTÃO FAZENDO A AULA
alunos.append('Hetfield') #Esse método o novo elemento vai para ultima posição
print(f"Lista com aluno novo na ultima posição: {alunos}")
print(20*"-")
alunos.insert(1,'Maya')
print(f'Lista com aluna nova na segunda posição: {alunos}')
print(20*"-")

#3: ALUNO DESISTIU: PRECISO REMOVER ELE
alunos.remove('Ozzy') #Remove indico o valor que quero remover
print(f"Removendo aluno da lista usando remove: {alunos} ")
print(20*"-")
alunos.pop(4) #No POP indico o indice que quero remover
print(f"Removendo aluno da lista usando o pop {alunos}")
print(20*"-")

#4: Conceito de dicionário, para pesquisar aluno especifico
#Criando dicionário a partir da lista de alunos, uso o enumerate para criar uma chave numérica

alunos_dict=dict(enumerate(alunos))
print(alunos_dict)
print(20*"-")
aluno_pesquisado=alunos_dict[1]
print(f"Aluno pesquisado: {aluno_pesquisado}")

#Criando dicionario a partir de uma tupla: Usando aqui chave como matricual e aluno como valor
print(20*"-")
alunos_matricula=[(1234,'Hamilton'),(4567,'Bruce',),(4053, 'Janet'),(1555,'Bruna',),(8888,'Amy'),(4566,'Ozzy')]
print(f"Tupla: Matricula-Aluno: {alunos_matricula}")
print(20*"-")
alunos_matricula_dict=dict(alunos_matricula)
print(f"Transformando tupla em dicionario: Chave: MATRICULA e VALOR: Nome do Aluno: {alunos_matricula_dict}")
print(20*"-")
alunos_matricula_pesquisa=alunos_matricula_dict[1555]
print(f"Pesquisa do aluno a partir da matricula: {alunos_matricula_pesquisa}")