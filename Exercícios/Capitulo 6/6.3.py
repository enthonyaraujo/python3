''' Exercício 6.3 Faça um programa que percorra duas listas e gere
uma terceira sem elementos repetidos'''

l1 = []
l2 = []
while True:
    entry = int(input("PRIMEIRA lista: (0 para terminar a lista): "))
    if entry == 0:
        break
    l1.append(entry)
while True:
    entry = int(input("SEGUNDA lista: (0 para terminar a lista): "))
    if entry == 0:
        break
    l2.append(entry)

l3=[]
l12=l1[:]
l12.extend(l3)

x=0
while x < len(l12):
    y = 0
    while y < len(l3):
        if l12[x] == l3[y]:
            break
        y+=1
    if y == len(l3):
        l3.append(l12[x])
    x+=1
x = 0 
while x < len(l3):
    print(f"{x}: {l3[x]}")
    x+=1
        