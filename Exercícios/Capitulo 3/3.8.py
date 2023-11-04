'''Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido
em milímetros.'''

metros = float(input("Digite a distancia: "))
milimetros = metros*(10**3)

print("%d em metros são %d em milimetros" % (metros,milimetros))