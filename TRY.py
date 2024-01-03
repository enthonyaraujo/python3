notas = []
n1 = int(input('Digite a primeria nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
notas.extend([n1,n2,n3])
soma = 0
x = 0
while x<3:
    soma += notas[x]
    x += 1 
print('Média: %.1f ' % (soma/x))
    