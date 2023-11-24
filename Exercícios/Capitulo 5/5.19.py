'''Exercício 5.18 Modifique o programa para também trabalhar com notas de R$ 100'''

valor=int(input("Digite o valor a pagar:"))
cédulas=0
atual=50
apagar=valor
#utilizarei apenas moedas de 0.5, 0.10, 0.25, 0.50 e 1 real
while True:
    if atual<=apagar:
        apagar-=atual
        cédulas+=1
    else:
        if atual > 1:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
        else: 
            print("%d moedas de R$ %d" %(cédulas, atual))
        if apagar <0.05:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05		
        cédulas = 0