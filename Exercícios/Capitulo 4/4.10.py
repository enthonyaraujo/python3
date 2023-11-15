'''Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta-
lação: R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir.'''

kWh = float(input("Digite seu consumo em kWh (Quilowatt-hora): "))
operação = input("Qual seu tipo de instalação?\n R/r- Residencial\n I/i- Industria\n C/c- Comércio\n")

if operação == "R" or operação == "r":
    if kWh <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif operação == "I" or operação == "i":
    if kWh <=1000:
        preço = 0.55
    else:
        preço = 0.60
elif operação == "C" or operação == "c":
    if kWh <= 5000:
        preço = 0.55
    else:
        preço = 0.60
else:
    print("Operação Invalida!!!")
    
consumo = kWh * preço

print("Valor a pagar: R$ %.1f " % consumo)
