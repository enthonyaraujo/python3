'''Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.'''

dias = int(input("Digite a quantidade de dias: "))
horas = float(input("Digite a quantidade de horas: "))
minutos = float(input("Digite a quantidade de minutos: "))
segundos = float(input("Digite a quantidade de segundos: "))

dias_s= dias*86400
horas_s = horas*3600
minutos_s = minutos*60

total = dias_s + horas_s + minutos_s + segundos

print("O total me segundos é: %d" % total)