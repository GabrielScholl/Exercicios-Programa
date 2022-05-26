def imprimeMatrizSemBorda(matriz):

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):

            if coluna < len(matriz)-1:
                print(matriz[linha][coluna], end = "")
                
            if coluna == len(matriz)-1:
                print(matriz[linha][coluna])
            
        print("")

imprimeMatrizSemBorda()

"""Impressão dos elementos da matriz no sentido da leitura"""
