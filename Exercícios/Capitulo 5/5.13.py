'''Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
de meses para que a dívida seja paga, o total pago e o total de juros pago.'''

divida = float(input('Digite o valor da divida: '))
juros = float(input('Digite o valor dos juros: '))
pagamento = float(input('Valor mensal a ser pago: '))
mes = 1

if (divida * (juros/100)) > pagamento:
    print('Valor é inferior ao pagamento mensal')
else: 
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros1 = saldo * juros / 100
        saldo = saldo + juros1 - pagamento
        juros_pago = juros_pago + juros1
        print(f"Saldo da dívida no mês {mes} é de R${saldo:6.2f}.")
        mes = mes + 1
print(f"Para pagar essa dívida você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
