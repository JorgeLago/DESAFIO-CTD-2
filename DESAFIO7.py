# Melhore o jogo do DESAFIO028 onde o computador  vai 'pensar'
# em um numero entre 0 a 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import random

palpite = 0
numero_secreto = random.randrange(0, 10)
chutes = 0

while palpite != numero_secreto:
    palpite = int(input(' Chute um numero de 0 a 10: '))
    if palpite == numero_secreto:
        print('Voce acertou o número com {} tentativas. '.format(chutes))
    else:
        print('Voce errou, tente novamente. ')
        print(numero_secreto)
        chutes += 1
print('Fim de Jogo')