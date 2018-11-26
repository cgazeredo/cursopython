import math

angulo = int(input('Entre com um angulo qualquer: '))
sen = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
print('Para o ângulo {} temos seno {:.2f}, cosseno {:.2f} e tangente {:.2f}. '.format(angulo, sen, cos, tg))
