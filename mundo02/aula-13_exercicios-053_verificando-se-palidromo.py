frase = str(input('Entre com a frase: ')).strip()

separado = frase.split()
sem_espaco = ''.join(separado).lower()
tam = len(sem_espaco)
reverso = ''
for c in range(tam, 0, -1):
    reverso += sem_espaco[c-1]
if reverso == sem_espaco:
    print('A frase [{}] '.format(frase), end='')
    print('é palindromo. ')
else:
    print('A frase [{}], não é palindromo.'.format(frase))
