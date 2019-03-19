from random import randint
from time import sleep

tentativas = 1
r_num = randint(0, 10)
print('COMPUTADOR: Pensei num número!')
chute = int(input('Tente acertar o numero que o computador pensou de 0 a 10: '))
print('PROCESSANDO...')
sleep(3)
while chute != r_num:
    r_num = randint(0, 10)
    print('Você errou. O número era {}'.format(r_num))
    chute = int(input('Tente novamente, em qual numero eu pensei agora? '))
    tentativas += 1
    print('PROCESSANDO...')
    sleep(1)

print('Parabens voce acertou, o numero é {}'.format(r_num))
print('Voce precisou de {} tentativa(s). '.format(tentativas))

