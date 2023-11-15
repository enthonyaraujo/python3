'''Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.'''

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operação = int(input("Digite a operação que deseja:\n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão\n"))

if operação == 1:
    soma = n1+n2
    print("%d + %d = %d" % (n1,n2,soma))
elif operação == 2:
    subtração = n1-n2
    print("%d - %d = %d" % (n1,n2,subtração))
elif operação == 3:
    multiplicação = n1*n2
    print("%d x %d = %d" % (n1,n2,multiplicação))
elif operação == 4:
    divisão = n1/n2
    print("%d / %d = %d" % (n1,n2,divisão))
else:
    print("Operação invalida, digite um valor entre 1 e 4.")