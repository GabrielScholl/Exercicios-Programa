def somaDosElementosDaLista(lista):

    length = len(lista)
    soma = 0
    
    for contador in range(length):
        parcial = lista[contador]
        soma += parcial
    
    return soma
