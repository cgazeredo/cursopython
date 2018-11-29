frase = 'Curso em Video Python'

print(frase[9])  # imprime décimo caracter
print(frase[9:21])  # imprime do caracter 9 ate o 21 sem imprimir o 21
print(frase[9:21:2])  # imprime do caracter 9 ate o 21 sem imprimir o 21 pulando de 2 em 2
print(frase[:5])  # imprime do caracter 0 ate o 5 sem imprimir o 5
print(frase[15:])  # imprime do caracter 15 ate o ultimo caracter
print(frase[9::3])

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13)) # conta quantas vezes encontra caracter 'o' entre os caracteres 0 e 13
print(frase.find('deo'))  # aponta onde a sequencia buscada iniciou
print(frase.find('Android'))
print('curso' in frase)   # retorna true ou false pra existencia da string buscada
print(frase.replace('Python', 'Android'))  #troca python por android na string, mas nao edita a string, cri um nova para esse uso
print(frase.upper())
print(frase.lower())
print(frase.capitalize())  #primeira letra da string maiuscula
print(frase.title())  #todas as primeiras letras de cada palavrax

