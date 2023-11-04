'''Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.'''

cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fumou? "))
minutos_perdidos = 10
dias_perdidos = (cigarros_dia * minutos_perdidos * 365 * anos) / (24*60)

print("Você perderá: %d dias" % dias_perdidos) 