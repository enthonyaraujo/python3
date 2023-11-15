'''Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar.'''

casa = float(input("Informe o valor da casa a comprar: "))
salario = float(input("Informe o valor do seu salario: "))
qnt_anos = float(input("Informe a quantidade anos a pagar: "))
meses = qnt_anos*12
prestação_mensal = casa/meses

if prestação_mensal <= (0.3*salario):
    print("Emprestimo feito com sucesso!")
    print("Suas prestações ficaram de %.1f em %.1f meses (%d anos)" % (prestação_mensal,meses,qnt_anos))
else:
    print("Desculpe, não vai ser possivel obter o emprestimo.")
    
