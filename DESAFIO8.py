# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]Somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# Seu prgrama deverá realizar o operação solicitada em cada caso.
num1 = input(' Digite o numero 1: ')
num2 = input(' Digite o numero 2: ')
escolha = 0
while escolha == 0:
    if escolha == 1:
        print(' A soma resulta em {}.'.format(num1+num2))
    elif escolha == 2:
        print(' A multiplicação resulta em {}.'.format(num1 * num2))
    elif escolha == 3:
        print(' O maior número é {}.'.format(max(num1, num2)))
    elif escolha == 4:
        num1 = input(' digite um novo numero:' )
        num2 = input(' Digite um novo numero2: ')
    elif escolha == 5:
        break
    escolha = input(' Oq deseja fazer: 1 somar, 2 multiplicar, 3 qual o maior, 4 novos numeros, 5 Fim!')

print('Fim do Programa!!')