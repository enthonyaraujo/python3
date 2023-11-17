
n1 = float(input("Informe a nota da PRIMERIA UNIDADE: "))
n2 = float(input("Informe a nota da SEGUNDA UNIDADE: "))
n3 = float(input("Informe a nota da TERCEIRA UNIDADE: "))

media = (n1+n2+n3)/3
rec = (50-media*6)/4

if media>=7 and media<=10:
    print("Aluno aprovado com media %.1f" %media)
elif media>=5 and media<7:
        print("Vocẽ esta de recuperação, precisando de %.1f" %rec)
elif media<5:
    print("Aluno reprovado")
else: 
    print("Operação Invalida")