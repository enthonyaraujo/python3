'''Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h.'''

velocidade = int(input("Olá, a que velocidade (km/h) você estava no carro? "))
multa = velocidade*5

if velocidade > 80:
    print("Você foi multado em %d." %multa)
if velocidade <= 80:
    print("Tudo bem, pode seguir viagem.")
