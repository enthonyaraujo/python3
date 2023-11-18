real = float(input("Moeda em R$: "))
operação = int(input("[1] Dolar\n[2] Euro\n"))

if operação == 1:
    dolar = 4.91*real
    print("R$ %.2f = %.2f US$" %(real, dolar))
elif operação == 2:
    euro = 5.36*real
    print("R$ %.2f = %.2f €" %(real,euro))
else:
    print("Moeda invalida.")

