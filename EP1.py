<<<<<<< HEAD
from random import randint
print('INÍCIO DO JOGO')
jogo = True
fichas= 100
print('Você possui {0} fichas'.format(fichas))
Come_out = True
print('Você está na fase Come Out')
while jogo:
    valor_apostado = int(input('Quantas fichas você quer apostar? '))
    while Come_out:
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
                    if fichas < 0:
                        jogo = False
                        print('FIM DO JOGO!')
            elif soma_dados1 == 3 or soma_dados1 == 4 or soma_dados1 == 9 or soma_dados1 == 10 or soma_dados1 == 11:
                fichas = fichas + valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            elif soma_dados1 == 2:
                fichas = fichas + 2*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            else:
                fichas = fichas + 3*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
        elif possibilidade_de_aposta == 'Any Craps':
            print('Você escolheu Any Craps')
            if soma_dados1 == 2 or soma_dados1 == 3 or soma_dados1 == 12:
                fichas = fichas + 7*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            else:
                fichas = fichas - valor_apostado
                print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas < 0:
                        jogo = False
                        print('FIM DO JOGO!')                
        elif possibilidade_de_aposta == 'Twelve':
            print('Você escolheu Twelve')
            if soma_dados1 == 12:
                fichas = fichas + 30*valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            else:
                fichas = fichas - valor_apostado
                print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                    if fichas < 0:
                        jogo = False
                        print('FIM DO JOGO!')
        elif possibilidade_de_aposta == 'Pass Line Bet':
            print('Você escolheu Pass Line Bet')
            if soma_dados == 7 or soma_dados == 11:
                fichas = fichas + valor_apostado
                print(('Você ganhou e agora possui {0} fichas'.format(fichas))
            elif soma_dados == 2 or soma_dados == 3 or soma_dados ==12:
                fichas = fichas - valor_apostado
                print(('Você perdeu e agora possui {0} fichas'.format(fichas))
                if fichas < 0:
                    jogo = False
                    print('FIM DO JOGO!')
            else:
                Come_out = False
                print('Você está na fase Point')
    escolha = input('Qual você escolhe? (Point ou Come Out):  ')
    if escolha == 'Come Out':
        Come_out = True and Point = False
    else:
        Come_out = False and Point = True

    while Point:
        possibilidade_de_aposta = input('Qual tipo de aposta você quer? (Pass Line Bet, Field, Any Craps, Twelve):  ')
        
    