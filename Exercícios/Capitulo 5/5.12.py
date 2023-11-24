'''Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês, e você
deve considerá-lo para o cálculo de juros do mês seguinte.'''

deposito = float(input('Digite o valor do deposito: '))
taxa = float(input('Digite o valor da taxa (5 = 5%): '))
deposito_mensal = float(input('Digite o valor do deposito mensal (se não quer digite 0): '))
mes = 1
saldo = deposito

while mes <=24:
    saldo = saldo + (saldo*(taxa/100)) + deposito_mensal
    print(f'Mês {mes} - Saldo = {saldo:.1f}')
    mes += 1
  
print(f'Valor lucrado: {saldo-deposito:.1f}.')  