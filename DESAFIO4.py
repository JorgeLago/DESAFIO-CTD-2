# Faça um programa que calcule a soma entre todos os números ímpares que
# são multiplos de três e que se
# encontram no intervalo de 1 até 500.
multi = 0
for multi_tres in range(0, 1000, 3):
    if multi_tres % 2 == 1:
        multi += multi_tres

print(multi)