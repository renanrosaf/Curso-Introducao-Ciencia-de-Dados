#Estrutura IF:
hora=11
#de acordo com condição, imprimo resultado

#humor='sono' 
#humor='sedento'
humor='calor'

if humor =='sono' and hora<10: #And:E
    print('café') #Só ocorre se a condição do IF for verdadeira
    #Esta recuada, aninhada, SE A CONDIÇÃO FOR VERDADE, IRA IMPRIMIR CAFÉ
#Se não se
elif humor=='sedento' or hora<2: #Or=Ou
    print('Limonada')

else: #Executada depois de todas as condições, se nenhuma for atendida, alinhada a outras condições
    print('Água')
