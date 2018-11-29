frase = 'Curso em Video Python'

print(frase[3:9:2])

print('''Com o Spotlight
você pode encontrar apps,
documentos e outros arquivos
no Mac. Com as Sugestões do
Spotlight, você também pode
saber sobre notícias, esportes
filmes, previsão do tempo e muito mais.''')


print(frase.lower().find('curso'))

print(frase.split())
dividida = frase.split()
print(dividida[0][3])  # pega a primeira palavra da lista depois do split, e imprime a terceira letra
