a = float(input("Entre com o lado A do triangulo: "))
b = float(input("Entre com o lado B do triangulo: "))
c = float(input("Entre com o lado C do triangulo: "))

if abs(b-c) < a < abs(b+c):
    if abs(a-c) < b < abs(a+c):
        if abs(a-b) < c < abs(a+b):
            #se as retas formam um triangulo, dizer que dipo de triangulo é

else:
    print("As retas a = {}, b = {} e c = {} não podem formar um triangulo".format(a, b, c))

