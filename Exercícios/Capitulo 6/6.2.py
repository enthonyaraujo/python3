''' Exercicio 6.2 Faça um programam que leia duas listas e que gere
uma terceira com os elementos das duas primeiras'''

L1 = [] #primeira lista   
L2 = [] #segunda lista

# L3 = L1 + L2 #soma das duas listas

while True:
    #preenchimento da primeira lista
    entry = int(input("Digite um numero para ser adicionado a PRIMEIRA lista: (0 para terminara a lista)"))
    if entry == 0:
        break
    L1.append(entry)

while True:
    #preenchimento da segunda lista
    entry = int(input("Digite um numero para ser adicionado a SEGUNDA lista: (0 para terminara a lista)"))
    if entry == 0:
        break
    L2.append(entry)
''' 
uma maneira de adicionar a terceira lista   
L3 = L1 + L2
print(L3)'''

# adicionando a terceira lista
L3 = L1[:]
L3.extend(L2)
x = 0
while x < len(L3):
    print(f"{x}: {L3[x]}")
    x += 1 
    