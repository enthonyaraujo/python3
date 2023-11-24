'''Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O pro-
grama deve ler os números até que o usuário digite 0 (zero). No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.'''

quantidade = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro ou 0 para dar break: '))
    if num == 0:
        break
    soma = soma + num
    quantidade = quantidade + 1
print(f'Quantidade de numeros digitados pelo usuario: {quantidade} ')
print(f'Soma dos numeros: {soma}')
print(f'Media dos numeros: {soma/quantidade}')