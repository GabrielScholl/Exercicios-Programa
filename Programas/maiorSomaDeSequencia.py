lista = []
sublista = []
quantia = int(input("Digite a quantidade de numeros: "))

for i in range(quantia):
    valor = int(input("Digite o proximo numero: "))
    lista.append(valor)

#Sublista de i ate j, escolhe um i e varia todos os j
for i in range(quantia):
    for j in range(i, quantia):

        for l in range(i, j+1):
            sublista.append(lista[l])

        for k in range(i, j+1):
            somaParcial = sublista[k]
            while k < j-1:
                somaParcial += sublista[k+1]

        if i == j == 0:
            somaFinal = somaParcial

        if somaParcial > somaFinal:
            somaFinal = somaParcial

print("A maior subsoma eh: ", somaFinal)

