def main():
    quantidade = int(input("Quantos numeros quer verificar se sao soma de dois primos? "))

    for contador in range (quantidade):
        numero = int(input("Digite um numero: "))
        
        primo1, primo2 = verificadora(numero)

        if primo1 != 0 and primo2 !=0:
            print(numero, "eh soma de", primo1, "e", primo2)
        else:
            print(numero, "nao eh soma de dois primos")
    main()
    return

def verificadora(numero):
    fator = 2
    contador = 0
    marcador = False
    primo1 = primo2 = 0
    primo = True
    outro_primo = True

    while fator < numero:
        
        for p in range(2, numero - fator - 1, 1):
            if (numero - fator) % p == 0:
                primo = False
            elif (numero - fator) % p != 0:
                primo1 = numero - fator
        fator += 1

    while parametro < fator:            
        if primo:
            for p in range(2, fator - 1, 1):
                if fator % p == 0:
                    outro_primo = False
                elif fator % p != 0:
                    primo2 = fator
                    
        if primo and outro_primo:
            return primo1, primo2

        else:
            return 0, 0

        parametro += 1
        
main()
