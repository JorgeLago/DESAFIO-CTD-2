# Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for impar
# desconsidere-o.
soma = 0
for i in range(0, 6):
    i = int(input(' Digite um número: '))
    if i % 2 == 0:
        soma += i
print(soma)
