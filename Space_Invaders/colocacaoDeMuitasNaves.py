import math

matriz = []
COLUNA_MAXIMA = 10
LINHA_MAXIMA = 5
quantidadeNaves = int(input("Digite o numero de naves (inteiro maior que 1 e menor que %d): " %(COLUNA_MAXIMA-3)))

for i in range(LINHA_MAXIMA+1):
    matriz.append([' ']*(COLUNA_MAXIMA+1))

for j in range(LINHA_MAXIMA+1):
    matriz[j][0] = "|"
    matriz[j][COLUNA_MAXIMA] = "|"

coluna = 1
a = 2
limitadorDeLinha = 0

#Seleciona as posicoes 1, 3, 5, ..., COLUNA_MAXIMA - 1
while 0 < coluna < COLUNA_MAXIMA:
    for linha in range(a-2, a):
        
        #Coloca nave
        if quantidadeNaves > 0:
            matriz[linha][coluna] = 'V'
            quantidadeNaves -= 1
            #Para trocar de linha no limite
            limitadorDeLinha += 1
            
        if limitadorDeLinha == COLUNA_MAXIMA:
            #Pula duas linhas
            a += 2
            limitadorDeLinha = 0
            #Volta pra primeira coluna de naves
            coluna = -1
            
    coluna += 2

#Posiciona o jogador
matriz[LINHA_MAXIMA][int(COLUNA_MAXIMA/2)] = "A"

for linha in matriz:
    for posicao in linha:
        print(posicao, end="")
    print("")
