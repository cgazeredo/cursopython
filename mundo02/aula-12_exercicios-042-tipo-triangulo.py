a = float(input("Entre com o lado A do triangulo: "))
b = float(input("Entre com o lado B do triangulo: "))
c = float(input("Entre com o lado C do triangulo: "))

if abs(b-c) < a < abs(b+c):
    if abs(a-c) < b < abs(a+c):
        if abs(a-b) < c < abs(a+b):
            #  se as retas formam um triangulo, dizer que dipo de triangulo é
            if a == b == c:
                print('As retas formam um triangulo equilátero. ')
            elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
                print('As retas formam um triangulo isoceles')
            else:
                print('As retas formam um triangulo escaleno.')

else:
    print("As retas a = {}, b = {} e c = {} não podem formar um triangulo".format(a, b, c))
