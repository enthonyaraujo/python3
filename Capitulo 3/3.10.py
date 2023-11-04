'''Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.'''

salario = float(input("Digite seu salario: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))
aumento = porcentagem/100

novo_salario = salario + (aumento * salario)

print("Seu salario aumentará para %d" % novo_salario)

# Novo salário = R$ 3.000 + (0,10 * R$ 3.000) = R$ 3.30300