'''Exercício 4.1 Analise o programa da listagem 4.2. Responda o que acontece se o
primeiro e o segundo valores forem iguais? Explique'''

# se a e b forem iguais o codigo não ira gerar nada, pois ele so funciona se forem dadas as condições certas
# no caso de dois numeros diferentes ele não da resultado nenhum por que não foi configurado para isso.
# para arrumar esse erro é possivel colocando um else no final do código como mostrado.

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b: 
    print("O primeiro número é o maior!") 
    if b > a: 
        print("O segundo número é o maior!") 
else:
    print("Invalido")   
