"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Gabriel Boaventura Scholl
  NUSP : 10771218
  Turma: 12
  Prof.: Alan Mitchell Durham
  
  """



def main():
        
    tipo_de_jogo = int(input("Escolha o tipo de jogo (1: Facil; 2: Dificil): "))
    # Facil
    if tipo_de_jogo == 1:
        numero_de_jogadas = int(input("Entre com o numero de jogadas: "))
        rodada = 1
        semente = 3
        pontos_jogador = 0
        pontos_maquina = 0
        estrelas = 0
        stars = 0
        
        while rodada <= numero_de_jogadas:
            print("Sua ", rodada, "a jogada: ", end = "")
            jogada_do_jogador = int(input())

            semente = (22695477 * semente + 1) % 2**(32)
            if semente <= 2**(31):
                jogada_do_computador = 0
            else:
                jogada_do_computador = 1
            
            if jogada_do_computador != jogada_do_jogador:
                vencedor = "Jogador ganha!"
                pontos_jogador += 1
            elif jogada_do_computador == jogada_do_jogador:
                vencedor = "Maquina ganha!"
                pontos_maquina += 1

            print("jogador = ", jogada_do_jogador, " maquina = ", jogada_do_computador, vencedor)

            print("JOGADOR: ", end = "")
            for i in range(pontos_jogador):
                print("*", end = "")
            print("")

            print("MAQUINA: ", end = "")
            for j in range(pontos_maquina):
                print("*", end = "")
            print("")

            rodada += 1
    # Fim de jogo
        game_over(pontos_jogador, pontos_maquina)
    # Dificil
    elif tipo_de_jogo == 2:
        numero_de_jogadas = int(input("Entre com o numero de jogadas: "))
        rodada = 1
        semente = 3
        pontos_jogador = 0
        pontos_maquina = 0
        estrelas = 0
        stars = 0
        
        anterior0 = False
        anterior1 = False

        lance00 = 0
        lance01 = 0
        lance10 = 0
        lance11 = 0

        while rodada <= numero_de_jogadas:
            print("Sua ", rodada, "a jogada: ", end = "")
            jogada_do_jogador = int(input())

                              
    # Jogada aleatoria
            if rodada == 1 or rodada == 2:
                if semente <= 2**(31):
                    jogada_do_computador = 0
                else:
                    jogada_do_computador = 1

    # Escolha da melhor jogada:
            else:
                if anterior0:
                    if lance10 > lance00:
                        jogada_do_computador = 1
                    elif lance10 < lance00:
                        jogada_do_computador = 0
                    else:
                        if semente <= 2**(31):
                            jogada_do_computador = 1
                        else:
                            jogada_do_computador = 0
                        
                elif anterior1:
                    if lance11 > lance01:
                        jogada_do_computador = 1
                    elif lance11 < lance01:
                        jogada_do_computador = 0
                    else:
                        if semente <= 2**(31):
                            jogada_do_computador = 0
                        else:
                            jogada_do_computador = 1

            semente = (22695477 * semente + 1) % 2**(32)

    # Comparacao do historico do jogador
            if rodada >= 2:
                if jogada_do_jogador == 0 and anterior0:
                    lance00 += 1
                elif jogada_do_jogador == 1 and anterior0:
                    lance10 += 1
                elif jogada_do_jogador == 0 and anterior1:
                    lance01 += 1
                elif jogada_do_jogador == 1 and anterior1:
                    lance11 += 1

    # Contabiliza a ultima jogada

            if jogada_do_jogador == 0:
                anterior0 = True
                anterior1 = False
            elif jogada_do_jogador == 1:
                anterior0 = False
                anterior1 = True
                            
    # Montagem do placar
            if jogada_do_computador != jogada_do_jogador:
                vencedor = "Jogador ganha!"
                pontos_jogador += 1
            elif jogada_do_computador == jogada_do_jogador:
                vencedor = "Maquina ganha!"
                pontos_maquina += 1

            print("jogador = ", jogada_do_jogador, " maquina = ", jogada_do_computador, vencedor)

            print("JOGADOR: ", end = "")
            for i in range(pontos_jogador):
                print("*", end = "")
            print("")

            print("MAQUINA: ", end = "")
            for j in range(pontos_maquina):
                print("*", end = "")
            print("")

            rodada += 1
    # Fim de jogo
        game_over(pontos_jogador, pontos_maquina)

    return

def game_over(pontos_jogador, pontos_maquina):
    
    if pontos_jogador > pontos_maquina:
        print("Voce venceu!")
    elif pontos_jogador < pontos_maquina:
        print("A maquina venceu!")
    else:
        print("Empate!")
        
    return

main()
