from random import randint
#Requisitos para o jogo
primeira_rodada = True 
Pass_Line_Point = True
Pass_Line_Point2 = True
demais_rodadas = True
jogo = True
print('INÍCIO DO JOGO')
fichas = 100
print('Você possui {0} fichas'.format(fichas))

while jogo:
#Primeira rodada do jogo
    while primeira_rodada:
        print('Primeira rodada. Você está na fase Come Out')
        valor_apostado = int(input('Quantas fichas você quer apostar? '))
        dado_1 = randint(1,6)
        dado_2 = randint(1,6)
        soma_dados1 = dado_1 + dado_2
        possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Pass Line Bet, Field, Any Craps, Twelve):  ')
        print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_1, dado_2, soma_dados1))
        if possibilidade_de_aposta == 'Field':
            print('Você escolheu Field')
            if soma_dados1 == 3 or soma_dados1 == 4 or soma_dados1 == 9 or soma_dados1 == 10 or soma_dados1 == 11:
                fichas = fichas + valor_apostado
                print('Você ganhou e agora possui {0} fichas'.format(fichas))
                primeira_rodada = False
            elif soma_dados1 == 2:
                fichas = fichas + 2*valor_apostado
                print('Você ganhou e agora possui {0} fichas'.format(fichas))
                primeira_rodada = False
            elif soma_dados1 == 5 or soma_dados1 == 6 or soma_dados1 == 7 or soma_dados1 == 8:
                fichas = fichas - valor_apostado
                print('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    primeira_rodada= False
                    print('FIM DO JOGO')
                else:
                    primeira_rodada = False
            else:
                fichas = fichas + 3*valor_apostado
                print('Você ganhou e agora possui {0} fichas'.format(fichas))
                primeira_rodada = False
        elif possibilidade_de_aposta == 'Any Craps':
            print('Você escolheu Any Craps')
            if soma_dados1 == 2 or soma_dados1 == 3 or soma_dados1 == 12:
                fichas = fichas + 7*valor_apostado
                print('Você ganhou e agora possui {0} fichas'.format(fichas))
                primeira_rodada = False  
            else:
                fichas = fichas - valor_apostado
                print('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    primeira_rodada = False
                    print('FIM DO JOGO!')
                else:
                    primeira_rodada = False
        elif possibilidade_de_aposta == 'Twelve':
            print('Você escolheu Twelve')
            if soma_dados1 == 12:
                fichas = fichas + 30 * valor_apostado
                print('Você ganhou e agora possui {0} fichas'.format(fichas))
                primeira_rodada = False
            else:
                fichas = fichas - valor_apostado
                print('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    primeira_rodada = False
                    print('FIM DO JOGO!')
                else:
                    primeira_rodada = False
        elif possibilidade_de_aposta == 'Pass Line Bet':
            print('Você escolheu Pass Line Bet')
            if soma_dados1 == 7 or soma_dados1 == 11:
                fichas = fichas + valor_apostado
                print('Você ganhou e agora possui {0} fichas'.format(fichas))
                primeira_rodada = False
            elif soma_dados1 == 2 or soma_dados1 == 3 or soma_dados1 ==12:
                fichas = fichas - valor_apostado
                print('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas <= 0:
                    primeira_rodada = False
                    print('FIM DO JOGO!')
                else:
                    primeira_rodada = False        
            else:
                while Pass_Line_Point:
                    print('Você está na fase Point. O novo sorteio é...') 
                    dado_3 = randint(1,6)
                    dado_4 = randint(1,6)
                    soma_dados2 = dado_3 + dado_4
                    print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_3, dado_4, soma_dados2))
                    if soma_dados2 == soma_dados1:
                        fichas = fichas + valor_apostado
                        Pass_Line_Point = False
                        primeira_rodada = False
                    elif soma_dados2 == 7:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        Pass_Line_Point = False
                        if fichas <= 0:
                            primeira_rodada = False
                            print('FIM DO JOGO!')
                        else:
                            primeira_rodada = False
                    else:
                        fichas = fichas
                        print('Você continua com {0} fichas'.format(fichas))
                        print('Os dados serão sorteados novamente!')
                        Pass_Line_Point = True
    if primeira_rodada == False:
        print('Acabou a primeira rodada!')
#Demais Rodadas
    while demais_rodadas:
        jogando = input('Você quer continuar jogando?  ')
        if jogando == 'Sim':
            fase = input('Você quer jogar em Point ou em Come Out?  ')
            if fase == 'Point':
                print('Você está jogando na fase Point')
                valor_apostado = int(input('Quantas fichas você quer apostar? '))
                dado_5 = randint(1,6)
                dado_6 = randint(1,6)
                soma_dados3 = dado_5 + dado_6
                possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Field, Any Craps, Twelve):  ')
                print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_5, dado_6, soma_dados3))
                if possibilidade_de_aposta == 'Field':
                    print('Você escolheu Field')
                    if soma_dados3 == 5 or soma_dados3 == 6 or soma_dados3 == 7 or soma_dados3 == 8:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            print('FIM DO JOGO')
                        else:
                            print('Acabou a rodada!')
                    elif soma_dados3 == 3 or soma_dados3 == 4 or soma_dados3 == 9 or soma_dados3 == 10 or soma_dados3 == 11:
                        fichas = fichas + valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    elif soma_dados3 == 2:
                        fichas = fichas + 2 * valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')    
                    else:
                        fichas = fichas + 3 * valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                elif possibilidade_de_aposta == 'Any Craps':
                    print('Você escolheu Any Craps')
                    if soma_dados3 == 2 or soma_dados3 == 3 or soma_dados3 == 12:
                        fichas = fichas + 7 * valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    else:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            print('FIM DO JOGO!')
                        else:
                            print('Acabou a rodada!')
                elif possibilidade_de_aposta == 'Twelve':
                    print('Você escolheu Twelve')
                    if soma_dados3 == 12:
                        fichas = fichas + 30 * valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    else:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            print('FIM DO JOGO!')
                        else:
                            print('Acabou a rodada!')
            if fase == 'Come Out':
                valor_apostado = int(input('Quantas fichas você quer apostar? '))
                dado_7 = randint(1,6)
                dado_8 = randint(1,6)
                soma_dados4 = dado_7 + dado_8
                possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Pass Line Bet,Field, Any Craps, Twelve):  ')
                print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_7, dado_8, soma_dados4))
                if possibilidade_de_aposta == 'Field':
                    print('Você escolheu Field')
                    if soma_dados4 == 5 or soma_dados4 == 6 or soma_dados4 == 7 or soma_dados4 == 8:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            print('FIM DO JOGO')
                        else:
                            print('Acabou a rodada!')
                    elif soma_dados4 == 3 or soma_dados4 == 4 or soma_dados4 == 9 or soma_dados4 == 10 or soma_dados4 == 11:
                        fichas = fichas + valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    elif soma_dados4 == 2:
                        fichas = fichas + 2*valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')    
                    else:
                        fichas = fichas + 3*valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                elif possibilidade_de_aposta == 'Any Craps':
                    print('Você escolheu Any Craps')
                    if soma_dados4 == 2 or soma_dados4 == 3 or soma_dados4 == 12:
                        fichas = fichas + 7*valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    else:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            print('FIM DO JOGO!')
                        else:
                            print('Acabou a rodada!')
                elif possibilidade_de_aposta == 'Twelve':
                    print('Você escolheu Twelve')
                    if soma_dados4 == 12:
                        fichas = fichas + 30*valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    else:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            print('FIM DO JOGO!')
                        else:
                            print('Acabou a rodada!')
                elif possibilidade_de_aposta == 'Pass Line Bet':
                    print('Você escolheu Pass Line Bet')
                    if soma_dados4 == 7 or soma_dados4 == 11:
                        fichas = fichas + valor_apostado
                        print('Você ganhou e agora possui {0} fichas'.format(fichas))
                        print('Acabou a rodada!')
                    elif soma_dados4 == 2 or soma_dados4 == 3 or soma_dados4 ==12:
                        fichas = fichas - valor_apostado
                        print('Você perdeu e agora possui {0} fichas'.format(fichas))
                        if fichas <= 0:
                            demais_rodadas = False
                            jogo = False
                            print('FIM DO JOGO!')
                        else:
                            print('Acabou a rodada!')                      
                    else:
                        while Pass_Line_Point2:
                            print('Você está na fase Point. O novo sorteio é...')
                            dado_9 = randint(1,6)
                            dado_10 = randint(1,6)
                            soma_dados5 = dado_9 + dado_10
                            print('Você sorteou os valores {0} e {1}, e a soma deles é {2}'.format(dado_9, dado_10, soma_dados5))
                            if soma_dados5 == soma_dados4:
                                fichas = fichas + valor_apostado
                                Pass_Line_Point2 = False
                                primeira_rodada = False
                            elif soma_dados5 == 7:
                                fichas = fichas - valor_apostado
                                print('Você perdeu e agora possui {0} fichas'.format(fichas))
                                Pass_Line_Point2 = False
                                if fichas <= 0:
                                    demais_rodadas = False
                                    jogo = False
                                    print('FIM DO JOGO!')                                  
                                else:
                                    print('Acabou a rodada!')
                            else:
                                fichas = fichas
                                print('Você continua com {0} fichas'.format(fichas))
                                print('Os dados serão sorteados novamente!')
                                Pass_Line_Point2 = True 
                        if Pass_Line_Point2 == False:
                            demais_rodadas = True 
        else:
            print('Você saiu do jogo')
            jogo = False
            primeira_rodada = False
            demais_rodadas = False
if jogo == False:
    print('FIM DO JOGO')