def main():
    
    matriz, linhas, colunas = inputMatriz()
    achei = False

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] != matriz[j][i]:
                achei = True

    if achei:
        print("Nao eh simetrica")
    elif not achei:
        print("Eh simetrica")


def inputMatriz():

    linhas = int(input("Numero de linhas: "))
    colunas = int(input("Numero de colunas: "))
    matriz = []

    if linhas!= colunas:
        print("Nao pode ser simetrica, porque o numero de linhas eh diferente do numero de colunas, feche o programa")

    for a in range(linhas):
        linha = [0]*colunas
        matriz.append(linha)
    
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = int(input("Proximo: "))

    return matriz, linhas, colunas

main()
