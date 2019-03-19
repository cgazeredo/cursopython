num = int(input('Digite o numero para obter seu fatorial: '))
fat = 1
print('{}! = '.format(num), end='')
while num != 1:
    print('{} x '.format(num), end='')
    fat = num*fat
    num -= 1
print('1 = {}'.format(fat))
