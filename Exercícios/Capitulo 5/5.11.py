'''Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.'''

deposito = float(input('Digite o valor do deposito: '))
taxa = float(input('Digite o valor da taxa (5 = 5%): '))
mes = 1
saldo = deposito

while mes <=24:
    saldo = saldo + (saldo*(taxa/100))
    print(f'Mês {mes} - Saldo = {saldo:.1f}')
    mes += 1
  
print(f'Valor lucrado: {saldo-deposito:.1f}.')  