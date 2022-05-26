def main():
    
    entrada = input("Digite as dimensoes, separadas por espaco: ")
    lista = entrada.split(' ')
    linhas = int(lista[0])
    colunas = int(lista[1])
    
    matriz = inputMatriz(linhas, colunas)
    soma1 = 0
    soma2 = 0
    achou = False

    soma2 = somaDiagonal(matriz)
                    

def inputMatriz(linhas, colunas):

    matriz = []

    # Cria matriz de zeros
    
    for a in range(linhas):
        linha = [0]*colunas
        matriz.append(linha)

    # Coloca todos os elementos

    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = int(input("Proximo: "))

    return matriz

def somaDiagonal(matriz):
    
    somas = []
    soma = 0
    linhas = len(matriz)
    colunas = len(matriz[0])

    #Para todos os primeiros elementos verticais
    for a in range(linhas):
        while i < linhas and j < colunas:
            soma += matriz[i][j]
            i += 1
            j += 1

        if soma not in somas:
            achou = True

        somas.append(soma)

    #Para todos os primeiros elementos horizontais, menos o primeiro
    for a in range(1, colunas):
        while i < linhas and j < colunas:
            soma += matriz[i][j]
            i += 1
            j += 1

        if soma not in somas:
            achou = True

        somas.append(soma)
