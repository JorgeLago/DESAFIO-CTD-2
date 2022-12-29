# Faça um programa que leia um número qualquer e mostre o seu factorial.
#Ex.: 5!=5x4x3x2x1=120
numero = int(input(' Digite um número:  '))
fatorial = numero
for i in range(0,numero):
    fatorial *= i
print(fatorial)