n = int(input("Digite um número inteiro para verificar se ele é primo ou não: "))

total = 0
for count in range(1, n+1):
    if n % count == 0:
        total += 1
print("O numero %d pode ser dividido por %d números." %(n,total))
if (total == 2):
    print("Portanto, %d é um número primo." %n) 
else:
    print("Portanto, %d não é um número primo. " %n)