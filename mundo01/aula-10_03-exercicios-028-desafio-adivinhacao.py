from random import randint

r_num = randint(0, 5)
chute = int(input('Tente acertar o numero que o computador pensou de 0 a 5: '))
if chute == r_num:
    print('Parabens voce acertou, o numero é {}'.format(r_num))
else:
    print('Você errou. O número era {}'.format(r_num))

