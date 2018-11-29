nome = input(' Digite um nome completo: ')

print('Todas Maisculas: ')
print(nome.upper())
print('Todas Minusculas:')
print(nome.lower())
print('Quantos caracteres sem contar espacos: ')
sem_espaco = nome.strip()
divido = sem_espaco.split()
print(len(''.join(divido)))
print('Numero de letras no primeiro nome: ')
print(len(divido[0]))



