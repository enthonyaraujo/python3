'''Exercício 5.15 Escreva um programa para controlar uma pequena máquina registra-
dora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
Código:      Preço: 
1      -      0,50
2      -      1,00
3      -      4,00
5      -      7,00
9      -      8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.'''

pagar = 0
while True:
    codigo = int(input('Digite o codigo do produto ou 0 para somar: '))
    preço = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preço = 0.50
        quant = int(input('Digite a quantidade:'))
        pagar = pagar + (preço * quant) 
    elif codigo == 2:
        preço = 1
        quant = int(input('Digite a quantidade:'))
        pagar = pagar + (preço * quant) 
    elif codigo == 3:
        preço = 4
        quant = int(input('Digite a quantidade:'))
        pagar = pagar + (preço * quant) 
    elif codigo == 5:
        preço = 7
        quant = int(input('Digite a quantidade:'))
        pagar = pagar + (preço * quant) 
    elif codigo == 9:
        preço = 8
        quant = int(input('Digite a quantidade:'))
        pagar = pagar + (preço * quant) 
    else:
        print('Opção Invalida!!!')
print(f'Valor a pagar: R${pagar:.1f}')