def main():

    matriz, m, n = inputMatriz()

    for i in range(m):
        for j in range(n):

            minas = minasVizinhas(campoMinado, i, j)
            
            print("%d,%d tem %d minas vizinhas" %(i, j, minas))
    
    imprimeMatriz(campoMinado)


def inputMatriz():

    linhas = int(input("Linhas: "))
    colunas = int(input("Colunas: "))
    matriz = []

    # Cria matriz de zeros
    
    for a in range(linhas):
        linha = [0]*colunas
        matriz.append(linha)

    # Coloca todos os elementos

    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = int(input("Proximo: "))

    return matriz, linhas, colunas

def minasVizinhas(campoMinado, i, j):
    
    soma = 0
    nLinhas = len(campoMinado)
    nColunas = len(campoMinado[0])

    for linha in range(i-1, i+1 + 1):
        for coluna in range(j-1, j+1 + 1):

            if (not (linha == i and coluna == j)
                and (0 <= linha <= nLinhas - 1)
                and (0 <= coluna <= nColunas - 1)):
                
                soma += campoMinado[linha][coluna]
    
    return soma

def imprimeMatriz(matriz):
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for b in range(linhas):
        for c in range(colunas):
            print(matriz[b][c], end = "")
        print()

main()
