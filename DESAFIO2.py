# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1.250,00
# , calcule um aumento de 10%. Para inferiores ou iguais, o aumento é 15%.
salario = float(input('Qual o salário do funcionário? > '))
if salario > 1250:
    print('O salário teve aumento e reajustou para R${}.'.format(salario + (salario * 0.10)))
else:
    print('O salário teve aumento e reajustou para R${}.'.format(salario + (salario * 0.15)))
