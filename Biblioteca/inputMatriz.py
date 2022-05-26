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

    return matriz
