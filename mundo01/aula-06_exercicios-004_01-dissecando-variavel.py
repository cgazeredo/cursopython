algo = input('Digite algo: ')
print('O tipo primitivo deste valor é ', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumerico? ', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas? ', algo.islower())
# print('Está capitalizada?', algo == algo.capitalize())
print('Está capitalizada?', algo.istitle())

