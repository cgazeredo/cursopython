from emoji import emojize
from time import sleep

print('Contagem regressiva para os fogos!!')
print('VAMOS LA! ')
sleep(1)
for c in range(11,0,-1):
    print('{}!! '.format(c-1))
    sleep(1)
print(emojize(':fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks:'':fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks::fireworks::fireworks::fireworks::fireworks:'))
print(emojize(':fireworks:{:^34}:fireworks:'.format('FELIZ ANO NOVO!')))
print(emojize(':fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks:'':fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks:'
              ':fireworks::fireworks::fireworks::fireworks::fireworks:'))

