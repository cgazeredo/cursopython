#  Informar a soma de todos os numeros impares  multiplos de 3 entre 1 e 500
soma = 0
for c in range(1, 500, 2):

    if c%3 == 0:
        print(c)
        soma += c
print(soma)