import math

angulo = math.radians(int(input('Entre com um angulo qualquer: ')))
sen = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
print('Para o ângulo {:.0f} temos seno {:.2f}, cosseno {:.2f} e tangente {:.2f}. '.format(math.degrees(angulo), sen, cos, tg))
