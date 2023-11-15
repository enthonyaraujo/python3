'''Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%.'''

salario = float(input("Digite seu salario: "))
porcentagem = 0.15

if salario > 1250:
    porcentagem = 0.10

aumento = salario * porcentagem

print("O aumento do seu salario será de: R$ %.1f " %aumento)
print("Portanto seu salario total vai ser de: R$ ", aumento + salario)
