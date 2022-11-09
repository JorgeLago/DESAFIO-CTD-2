#Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.
pessoa = 'incorreto'
while pessoa == 'incorreto':
    pessoa = str(input(('Digite qual seu sexo ( com M ou F ): '))).upper()
    if pessoa == 'M':
        print(' Você escolheu Sexo masculino (M)!')
    elif pessoa == 'F':
        print(('Você escolheu Sexo Feminino (F) !'))
    else:
        print('Alternativa incorreta, responda com M ou F.')
        pessoa = 'incorreto'
print( ' Fim do Programa!!')