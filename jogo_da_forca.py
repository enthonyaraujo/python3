import random

palavras = ["BRASIL","ARGENTINA", "BOLIVIA","CHILE","COLOMBIA","EQUADOR","GUIANA","PERU","PARAGUAI","SURINAME","URUGUAI","VENEZUELA"]

palavras = random.choice(palavras) # GERADOR DE ALGUM PAIS DA LISTA)
palavras = list(palavras) # TRANSFORMANDO EM UMA LISTA
qnt_letras = len(palavras) ## QUANTIDADE DE LETRAS
letras_descobertas = [] # LISTA DE LETRAS DESCOBERTAS
print("#### JOGO DA FORCA ####")

for i in range(0, len(palavras)):
    letras_descobertas.append("-")
print("DICAS: O tema é Países Sul Americanos \nA palavras tem %d letras" % qnt_letras)

acertou = False

while acertou == False:
    letra = str(input("\nDigite uma letra: "))
    
    for i in range(0, len(palavras)):
        if letra == palavras[i]:
            letras_descobertas[i] = letra
        print(letras_descobertas[i], end='')
        
    acertou = True

    for x in range(0,len(letras_descobertas)):
        if letras_descobertas[x] == "-":
            acertou = False
print("\nACERTOU A PALAVRA!!!!")