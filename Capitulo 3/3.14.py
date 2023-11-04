'''Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado.'''

dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
km = float(input("Digite a quantidade de km percorridos com o carro: "))

dias = dias*60
km = km*0.15
total = dias + km

print("Valor a pagar: %.2f" % total)
