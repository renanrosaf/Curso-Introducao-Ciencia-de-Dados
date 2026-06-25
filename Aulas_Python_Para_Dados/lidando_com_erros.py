#Função para dividir dois números
#Erro de Sintaxe : Algo esquecido na escrita do código, está errada, mais facil de ser identificado
# def dividir(a,b):
#     return a/b #sem barra, ação não é executada
# print(dividir(4,2))

#Erro de Excessão
#print(dividir(4,0)) -- Impossivel dividir por zero

#Lidando com Erros:
#Usando o Try, Except, Finally

def dividir(a,b):
    r=0
    try: 
        r=a/b
        return print (r)
    except ZeroDivisionError:
        print("Erro: Divisão Por Zero")
    except:
        print("Erro inesperado.Desculpe.")
    finally:
        print("Função Executada.")


#Passando Letra
print(dividir(4,'a'))