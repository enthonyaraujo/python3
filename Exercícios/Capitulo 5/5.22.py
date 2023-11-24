'''Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.'''

while True:
    option=int(input("\n1- ADIÇÃO\n2- SUBTRAÇÃO\n3- DIVISÃO\n4-MULTIPLICAÇÃO\n0- SAIR\n"))
    if option==0:
        break
    elif option>=1 and option<5:
        n=int(input('Tabuada de: '))
        x=1
        while x<=10:
            if option==1:
                print('%d + %d = %d' %(n,x,n+x))
            elif option ==2:
                print('%d - %d = %d' %(n,x,n-x))
            elif option ==3:
                print('%d / %d = %d' %(n,x,n/x))
            elif option ==4:
                print('%d * %d = %d' %(n,x,n*x))
            x+=1
    else:
        print('Invalid')