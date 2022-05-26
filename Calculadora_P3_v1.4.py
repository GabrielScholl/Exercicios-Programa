'''Este software eh Open Source, sendo assim pode modificar e
melhorar e mandar de volta no grupo'''


def main():
    print("")
    print("Calculo - 1")
    print("Algelin - 2")
    print("Fisica - 3")
    print("Computacao - 4")
    print("")
    materia = int(input("Entre o numero da materia: "))

    CALCULO = 1
    ALGELIN = 2
    FISICA = 3
    COMPUTACAO = 4

    if materia == CALCULO:
        p1 = float(input("Digite a nota da sua P1 (com ponto): "))
        p2 = float(input("Digite a nota da sua P2 (com ponto): "))
        p3 = (5 * 8 - 2 * p1 - 3 * p2) / 3

        print("Sua P3 deve ser igual ou maior a %.1f" % p3)

    elif materia == ALGELIN:
        p1 = float(input("Digite a nota da sua P1 (com ponto): "))
        p2 = float(input("Digite a nota da sua P2 (com ponto): "))
        p3 = 5 * 3 - p1 - p2

        print("Sua P3 deve ser igual ou maior a %.1f" % p3)

    elif materia == FISICA:
        p1 = float(input("Digite a nota da sua P1 (com ponto): "))
        p2 = float(input("Digite a nota da sua P2 (com ponto): "))
        p3 = (5 * 10 - 3 * p1 - 3 * p2) / 4

        print("Sua P3 deve ser igual ou maior a %.1f" % p3)

    elif materia == COMPUTACAO:
        a = float(input("Digite seu coeficiente de conduta ética (a<=1): "))
        EP1 = float(input("Digite a nota do seu EP1: "))
        EP2 = float(input("Digite a nota do seu EP2: "))
        EP3 = ((30 / a) - EP1 - 2 * EP2) / 3
        P1 = float(input("Digite a nota da sua P1: "))
        P2 = float(input("Digite a nota da sua P2: "))
        p3 = ((25 / a) - P1 - 2 * P2) / 2

        print("Sua P3 deve ser igual ou maior a %.1f" % p3)
        print("Seu EP3 deve ser igual ou maior a %.1f" % EP3)

    if p3 <= 0:
        print("")
        print("CongratuFUCKINGlations")
        print("")

    elif p3 <= 3:
        print("")
        print("PARABENS, ESTA QUASE LA")
        print("")

    elif 3 < p3 <= 5:
        print("")
        print("NAO PERCA A ESPERANCA, AINDA HA CHANCE")
        print("")

    elif 5 < p3 <= 8:
        print("")
        print("'TODO MUNDO VAI RPA CALCULO 2', by Lymber")
        print("")

    elif 8 < p3 <= 10:
        print("")
        print("BOA SORTE")
        print("")

    else:
        print("")
        print("oh.")
        print("")
        

    quero = input("'s' ou 'n': Quer continuar? ")

    if quero == 's':
        main()

main()

