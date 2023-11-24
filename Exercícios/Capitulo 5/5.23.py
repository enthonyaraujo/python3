'''Exercício 5.23 Escreva um programa que leia um número e verifique se é ou não
um número primo. Para fazer essa verificação, calcule o resto da divisão do número
por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
primos e que 2 é o único número primo que é par.'''

n = int(input("Digite um número inteiro para verificar se ele é primo ou não: "))

if n<0:
    print('Invalido')
if n == 0 or n == 1:
    print('Não são primos.')
else: 
    if n % 2 == 0 and n > 2:
        print('%d não é primo' %n)
    else:
        print('%d é primo' %n)