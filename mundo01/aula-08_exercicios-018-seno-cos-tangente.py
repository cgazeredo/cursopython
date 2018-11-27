import math

angulo_graus = float(input('Digite um angulo qualquer de novo: '))

angulo_rad = math.radians(angulo_graus)

s = math.sin(angulo_rad)
c = math.cos(angulo_rad)
t = math.tan(angulo_rad)
print('Para o angulo de {} graus temos: sen {}, cos {} e tg {}'.format(angulo_graus, s, c, t))
