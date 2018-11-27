from math import trunc

n = float(input('Entre com um numero qualquer: '))
#t = trunc(n)
t = (n*n)//n
print('O numero digitado foi {} e sua parte inteira é {:.0f}'.format(n, t), )