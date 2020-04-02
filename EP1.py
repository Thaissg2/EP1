print('Iniciando o jogo Craps')
from random import randint
print('INÍCIO DO JOGO')
primeira_rodada = True
fichas = 100
print('Você possui {0} fichas'.format(fichas))
Pass_Line_Point = True
demais_rodadas = True
Come_Out = True
Point = True

#Primeira rodada do jogo
while primeira_rodada:
    print('Primeira rodada. Você está na fase Come Out')
    valor_apostado = int(input('Quantas fichas você quer apostar? '))
    possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Pass Line Bet, Field, Any Craps, Twelve):  ')
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    soma_dados1 = dado_1 + dado_2
    print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_1, dado_2, soma_dados1))
    if possibilidade_de_aposta == 'Field':
        print('Você escolheu Field')
        if soma_dados1 == 5 or soma_dados1 == 6 or soma_dados1 == 7 or soma_dados1 == 8:
            fichas = fichas - valor_apostado
            print(('Você perdeu e agora possui {0} fichas'.format(fichas))
            if fichas <= 0:
                primeira_rodada = False
                print('FIM DO JOGO!')
            else:
                print('Acabou a primeira rodada!')
                primeira_rodada = False

        elif soma_dados1 == 3 or soma_dados1 == 4 or soma_dados1 == 9 or soma_dados1 == 10 or soma_dados1 == 11:
            fichas = fichas + valor_apostado
            print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            print('Acabou a primeira rodada!')
            primeira_rodada = False
            
        elif soma_dados1 == 2:
            fichas = fichas + 2*valor_apostado
            print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            print('Acabou a primeira rodada!')
            primeira_rodada = False

        else:
            fichas = fichas + 3*valor_apostado
            print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            print('Acabou a primeira rodada!')
            primeira_rodada = False
            
    elif possibilidade_de_aposta == 'Any Craps':
        print('Você escolheu Any Craps')
        if soma_dados1 == 2 or soma_dados1 == 3 or soma_dados1 == 12:
            fichas = fichas + 7*valor_apostado
            print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            print('Acabou a primeira rodada!')
            primeira_rodada = False
            
        else:
            fichas = fichas - valor_apostado
            print(('Você perdeu e agora possui {0} fichas'.format(fichas))
            if fichas <= 0:
                primeira_rodada = False
                print('FIM DO JOGO!')
            else:
                print('Acabou a primeira rodada!')
                primeira_rodada = False
                             
    elif possibilidade_de_aposta == 'Twelve':
        print('Você escolheu Twelve')
        if soma_dados1 == 12:
            fichas = fichas + 30*valor_apostado
            print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            print('Acabou a primeira rodada!')
            primeira_rodada = False
            
        else:
            fichas = fichas - valor_apostado
            print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    primeira_rodada = False
                    print('FIM DO JOGO!')
                else:
                    print('Acabou a primeira rodada!')
                    primeira_rodada = False

    elif possibilidade_de_aposta == 'Pass Line Bet':
        print('Você escolheu Pass Line Bet')
        if soma_dados1 == 7 or soma_dados1 == 11:
            fichas = fichas + valor_apostado
            print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            print('Acabou a primeira rodada!')
            primeira_rodada = False
        elif soma_dados1 == 2 or soma_dados1 == 3 or soma_dados1 ==12:
            fichas = fichas - valor_apostado
            print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    primeira_rodada = False
                    print('FIM DO JOGO!')
                else:
                    print('Acabou a primeira rodada!')
                    primeira_rodada = False
        else:
            while Pass_Line_Point:
                print('Você está na fase Point')
                dado_3 = randint(1,6)
                dado_4 = randint(1,6)
                soma_dados2 = dado_3 + dado_4
                print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_3, dado_4, soma_dados2))
                if soma_dados2 == soma_dados1:
                    fichas = fichas + valor_apostado
                    print('Acabou a primeira rodada!')
                    primeira_rodada = False

                elif soma_dados2 == 7:
                    fichas = fichas - valor_apostado
                    print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas <= 0:
                        primeira_rodada = False
                        print('FIM DO JOGO!')
                    else:
                        print('Acabou a primeira rodada!')
                        primeira_rodada = False
                else:
                    fichas = fichas
                    print('Você continua com {0} fichas'.format(fichas))
                    print('Os dados serão sorteados novamente!')
                    Pass_Line_Point = True

continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
if continuar_jogando == 'Sim':
    demais_rodadas = True
else:
    print('Você saiu do jogo')
    print ('FIM DO JOGO')
    demais_rodadas = False

#Demais rodadas
while demais_rodadas:
    while Come_Out:
        print('Você está na fase Come Out')
        valor_apostado = int(input('Quantas fichas você quer apostar? '))
        possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Pass Line Bet, Field, Any Craps, Twelve):  ')
        dado_5 = randint(1,6)
        dado_6 = randint(1,6)
        soma_dados3 = dado_5 + dado_6
        print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_5, dado_6, soma_dados3))
            if possibilidade_de_aposta == 'Field':
                print('Você escolheu Field')
                if soma_dados3 == 5 or soma_dados3 == 6 or soma_dados3 == 7 or soma_dados3 == 8:
                    fichas = fichas - valor_apostado
                    print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas <= 0:
                        demais_rodadas = False
                        print('FIM DO JOGO!')
                    else:
                        print('Acabou a rodada!')
                        continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                        if continuar_jogando == 'Sim':
                            demais_rodadas = True
                        else:
                            print('Você saiu do jogo')
                            print ('FIM DO JOGO')
                            demais_rodadas = False
                elif soma_dados3 == 3 or soma_dados3 == 4 or soma_dados3 == 9 or soma_dados3 == 10 or soma_dados3 == 11:
                    fichas = fichas + valor_apostado
                    print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False
                elif soma_dados3 == 2:
                    fichas = fichas + 2*valor_apostado
                    print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False
                else:
                    fichas = fichas + 3*valor_apostado
                    print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False

            elif possibilidade_de_aposta == 'Any Craps':
                print('Você escolheu Any Craps')
                if soma_dados3 == 2 or soma_dados3 == 3 or soma_dados3 == 12:
                    fichas = fichas + 7*valor_apostado
                    print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False
                else:
                    fichas = fichas - valor_apostado
                    print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas <= 0:
                        demais_rodadas = False
                        print('FIM DO JOGO!')
                    else:
                        print('Acabou a rodada!')
                        continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                        if continuar_jogando == 'Sim':
                            demais_rodadas = True
                        else:
                            print('Você saiu do jogo')
                            print ('FIM DO JOGO')
                            demais_rodadas = False

            elif possibilidade_de_aposta == 'Twelve':
                print('Você escolheu Twelve')
                if soma_dados3 == 12:
                    fichas = fichas + 30*valor_apostado
                    print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False
                else:
                    fichas = fichas - valor_apostado
                    print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas <= 0:
                        demais_rodadas = False
                        print('FIM DO JOGO!')
                    else:
                        print('Acabou a rodada!')
                        continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                        if continuar_jogando == 'Sim':
                            demais_rodadas = True
                        else:
                            print('Você saiu do jogo')
                            print ('FIM DO JOGO')
                            demais_rodadas = False

            elif possibilidade_de_aposta == 'Pass Line Bet':
                print('Você escolheu Pass Line Bet')
                if soma_dados3 == 7 or soma_dados3 == 11:
                    fichas = fichas + valor_apostado
                    print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False
                elif soma_dados3 == 2 or soma_dados3 == 3 or soma_dados3 ==12:
                    fichas = fichas - valor_apostado
                    print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas <= 0:
                        demais_rodadas = False
                        print('FIM DO JOGO!')
                    else:
                        print('Acabou a rodada!')
                        continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                        if continuar_jogando == 'Sim':
                            demais_rodadas = True
                        else:
                            print('Você saiu do jogo')
                            print ('FIM DO JOGO')
                            demais_rodadas = False
                else:
                    while Pass_Line_Point:
                        print('Você está na fase Point')
                        dado_7 = randint(1,6)
                        dado_8 = randint(1,6)
                        soma_dados4 = dado_7 + dado_8
                        print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_7, dado_8, soma_dados4))
                        if soma_dados4 == soma_dados3:
                            fichas = fichas + valor_apostado
                            print('Acabou a rodada!')
                            continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                            if continuar_jogando == 'Sim':
                                demais_rodadas = True
                            else:
                                print('Você saiu do jogo')
                                print ('FIM DO JOGO')
                                demais_rodadas = False
                        elif soma_dados4 == 7:
                            fichas = fichas - valor_apostado
                            print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                            if fichas <= 0:
                                demais_rodadas = False
                                print('FIM DO JOGO!')
                            else:
                            print('Acabou a rodada!')
                            continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                            if continuar_jogando == 'Sim':
                                demais_rodadas = True
                            else:
                                print('Você saiu do jogo')
                                print ('FIM DO JOGO')
                                demais_rodadas = False
                        else:
                            fichas = fichas
                            print('Você continua com {0} fichas'.format(fichas))
                            print('Os dados serão sorteados novamente!')
                            Pass_Line_Point = True

    while Point:
        print('Você está na fase Come Out')
        valor_apostado = int(input('Quantas fichas você quer apostar? '))
        possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Pass Line Bet, Field, Any Craps, Twelve):  ')
        dado_5 = randint(1,6)
        dado_6 = randint(1,6)
        soma_dados3 = dado_5 + dado_6
        print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_5, dado_6, soma_dados3))
        if possibilidade_de_aposta == 'Field':
            print('Você escolheu Field')
            if soma_dados3 == 5 or soma_dados3 == 6 or soma_dados3 == 7 or soma_dados3 == 8:
                fichas = fichas - valor_apostado
                print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    demais_rodadas = False
                    print('FIM DO JOGO!')
                else:
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False
            elif soma_dados3 == 3 or soma_dados3 == 4 or soma_dados3 == 9 or soma_dados3 == 10 or soma_dados3 == 11:
                fichas = fichas + valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                print('Acabou a rodada!')
                continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                if continuar_jogando == 'Sim':
                    demais_rodadas = True
                else:
                    print('Você saiu do jogo')
                    print ('FIM DO JOGO')
                    demais_rodadas = False
            elif soma_dados3 == 2:
                fichas = fichas + 2*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                print('Acabou a rodada!')
                continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                if continuar_jogando == 'Sim':
                    demais_rodadas = True
                else:
                    print('Você saiu do jogo')
                    print ('FIM DO JOGO')
                    demais_rodadas = False
            else:
                fichas = fichas + 3*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                print('Acabou a rodada!')
                continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                if continuar_jogando == 'Sim':
                    demais_rodadas = True
                else:
                    print('Você saiu do jogo')
                    print ('FIM DO JOGO')
                    demais_rodadas = False

        elif possibilidade_de_aposta == 'Any Craps':
            print('Você escolheu Any Craps')
            if soma_dados3 == 2 or soma_dados3 == 3 or soma_dados3 == 12:
                fichas = fichas + 7*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                print('Acabou a rodada!')
                continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                if continuar_jogando == 'Sim':
                    demais_rodadas = True
                else:
                    print('Você saiu do jogo')
                    print ('FIM DO JOGO')
                    demais_rodadas = False
            else:
                fichas = fichas - valor_apostado
                print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    demais_rodadas = False
                    print('FIM DO JOGO!')
                else:
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False

        elif possibilidade_de_aposta == 'Twelve':
            print('Você escolheu Twelve')
            if soma_dados3 == 12:
                fichas = fichas + 30*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
                print('Acabou a rodada!')
                continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                if continuar_jogando == 'Sim':
                    demais_rodadas = True
                else:
                    print('Você saiu do jogo')
                    print ('FIM DO JOGO')
                    demais_rodadas = False
            else:
                fichas = fichas - valor_apostado
                print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    demais_rodadas = False
                    print('FIM DO JOGO!')
                else:
                    print('Acabou a rodada!')
                    continuar_jogando = input('Você quer continuar jogando? (Sim ou Não) ')
                    if continuar_jogando == 'Sim':
                        demais_rodadas = True
                    else:
                        print('Você saiu do jogo')
                        print ('FIM DO JOGO')
                        demais_rodadas = False