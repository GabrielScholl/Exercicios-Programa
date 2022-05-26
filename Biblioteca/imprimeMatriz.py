def imprimeMatriz(matriz):
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for b in range(linhas):
        for c in range(colunas):
            print(matriz[b][c], end = "")
        print()
