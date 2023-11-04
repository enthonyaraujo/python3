'''Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual
de desconto. Exiba o valor do desconto e o preço a pagar'''

# Preço com desconto = Preço original - (Preço original * Percentagem de desconto / 100)

produto = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite a porcentagem de desconto: "))
produto = produto - (produto * desconto / 100)

print("Valor total com desconto: %d " % produto)
