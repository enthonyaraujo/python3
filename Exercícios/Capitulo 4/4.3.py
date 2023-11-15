'''Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
e o menor.'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

maior = n1
if n2 > maior :
    maior = n2
if n3 > maior:
    maior = n3

menor = n1 
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    
print("Maior: ",maior)
print("Menor: ",menor)