'''Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a mul-
tiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

x = 1
y = 0

while x <= n2:
    y = y + n1
    x = x + 1
print("%d x %d = %d" %(n1,n2,y))