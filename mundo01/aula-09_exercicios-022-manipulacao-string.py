nome = str(input(' Digite um nome completo: ')).strip()

print('Todas Maisculas: ')
print(nome.upper())
print('Todas Minusculas:')
print(nome.lower())
print('Quantos caracteres sem contar espacos: ')

divido = nome.split()
print(len(''.join(divido)))
print('Numero de letras no primeiro nome: ')
print(nome.find(' '))
print(len(divido[0]))



