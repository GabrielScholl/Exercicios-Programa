"""
Este programa:

pede uma sequencia de numeros
le os conjuntos de numeros adjacentes
    os conjuntos podem ter qualquer tamanho
soma os numeros do conjunto
caso forem maiores que a soma do anterior
    atribui aa variavel que carrega a maior soma

"""

def main():

    lista = []
    tamanhoDaLista = int(input("Quantos numeros: "))

    lista = montaLista(lista, tamanhoDaLista) #cospe lista

    maiorSoma = testaSequencias(lista, tamanhoDaLista) #cospe maiorSoma

    print("Maior soma: ", maiorSoma)

def montaLista(lista, tamanhoDaLista):
    
    for i in range(tamanhoDaLista):
        a = int(input("Um numero: "))
        lista.append(a)
    
    return lista

def testaSequencias(lista, tamanhoDaLista):

    #A estrategia eh criar uma lista vazia, colocar todos os valores e depois somar
    #Isso eh feito com sublistas de tamanho variado
    grupo = []

    #Variacao dos elementos
    for cadaElemento in range(tamanhoDaLista):
        
        #Variacao do tamanho do grupo que comeca num elemento
        for tamanhoGrupo in range(1, tamanhoDaLista + 1):
            
            #Comprimento p usar na lista[i:c](-1 pq n pode comecar no indice 1)
            posicaoFinal = cadaElemento + tamanhoGrupo - 1
            
            #Criacao do grupo com inicio e comprimento (+1 pq vai ate n-1)
            grupo = lista[cadaElemento:posicaoFinal + 1][:]

            soma = somaDosElementosDaLista(grupo)
            
            #Definicao da maiorSoma para o primeiro uso
            if cadaElemento == 0 and tamanhoGrupo == 1:
                maiorSoma = soma

            #Pegando a maior soma
            elif soma > maiorSoma:
                maiorSoma = soma
            
    return maiorSoma

def somaDosElementosDaLista(lista):

    length = len(lista)
    soma = 0
    
    for contador in range(length):
        parcial = lista[contador]
        soma += parcial
    
    return soma

main()
