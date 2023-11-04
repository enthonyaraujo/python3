'''Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é:
F = (9 x C /5) +32
'''
c = float(input("Digite a temperatura em graus celcius: "))
f = (9*c/5)+32
print("%d °C = %d °F"%(c,f))