novaLista = []

lista = input("Numero: ")
lista = lista.split(' ')

for elemento in lista:
    if elemento not in novaLista:
        novaLista.append(elemento)

print(novaLista)
