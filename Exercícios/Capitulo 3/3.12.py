'''Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.'''

distancia = float(input("Digite a distancia que deseja percorrer (km): "))
velocidade = float(input("Digite a velocidade (km/h): "))
tempo = distancia/velocidade
print("Você levará %.2f horas para chegar ao seu destino!" %tempo)
