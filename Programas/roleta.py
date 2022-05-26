numero = int(input("Digite o numero: "))
lista = [0] * 37

# A roleta (de cassino) tem os numeros de 0 a 36
while 0 <= numero <= 36:
    lista[numero] += 1
    numero = int(input("Digite o proximo numero: "))

for i in range(36):
    print("Numero", i, "saiu", lista[i], "vezes")
