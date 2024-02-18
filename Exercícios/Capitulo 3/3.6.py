materia1 = float(input("Digite a nota da sua primeira materia: "))
materia2 = float(input("Digite a nota da sua segunda materia: "))
materia3 = float(input("Digite a nota da sua terceira materia: "))

if (materia1 and materia2 and materia3) >= 7:
    print('Aprovado!')
else:
    print('Reprovado')
