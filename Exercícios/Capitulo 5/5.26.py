'''Exercício 5.26 Escreva um programa que calcule o resto da divisão inteira entre dois
números. Utilize apenas as operações de soma e subtração para calcular o resultado.'''

dividendo = int(input("Digite o número do dividendo: "))
divisor = int(input("Digite o número do divisor: "))
quociente = 0
dividendo1 = dividendo
while dividendo1 >= divisor:
    dividendo1 = dividendo1 - divisor
    quociente+=1
resto = dividendo1   
print("O resto de %d / %d é igual a %d" %(dividendo, divisor, resto))
      