'''Exercício 5.7 Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10.'''

n = int(input("Tabuada de:"))
x = int(input("Digite o número que deseja começar: "))
fim = int(input("Digite o ultimo número para imprimir: "))
while x <= fim:
    print(n*x)
    x=x+1