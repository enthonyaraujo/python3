'''Exercício 4.6
Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.'''

distancia = float(input("Digite a distacia (km) que devemos percorrer: "))
if distancia <= 200:
    taxa = 0.5
    preço = distancia*taxa
    print("Sua corrida vai ficar de: R$ %.1f" %preço)
else:
    taxa = 0.45
    preço = distancia*taxa
    print("Sua corrida vai ficar de: R$ %.1f" %preço)