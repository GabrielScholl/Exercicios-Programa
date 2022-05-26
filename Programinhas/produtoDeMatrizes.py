def main():

    print("Matriz A")
    matrizA, linhasA, colunasA = inputMatriz()
    print("Matriz B")
    matrizB, linhasB, colunasB = inputMatriz()
    matrizC = criaMatrizZeros(linhasA, colunasB)

    for i in range(linhasA):
        for j in range(colunasB):
            soma = 0
            for k in range(colunasA):
                soma += matrizA[i][k] * matrizB[k][j]
            matrizC[i][j] = soma

    print(matrizC)

def inputMatriz():

    linhas = int(input("Linhas: "))
    colunas = int(input("Colunas: "))
    matriz = []
    
    for a in range(linhas):
        linha = [0]*colunas
        matriz.append(linha)    

    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = int(input("Proximo: "))

    return matriz, linhas, colunas

def criaMatrizZeros(linhas, colunas):

    matriz = []
    
    for a in range(linhas):
        linha = [0]*colunas
        matriz.append(linha)

    return matriz

def imprimeMatriz(matriz):
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for b in range(linhas):
        for c in range(colunas):
            print(matriz[b][c], end = "")
        print()

main()
