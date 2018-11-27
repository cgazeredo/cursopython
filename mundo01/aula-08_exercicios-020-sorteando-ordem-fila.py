import random

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')


fila = [a1, a2, a3, a4]

# ordem_apresentacao = random.sample(fila, 4) jeito que eu fiz inicialmente

random.shuffle(fila) # O shuffle salva na variavel que ele embaralha

print('A ordem de apresentaçao dos trabalhos será: {}'.format(fila))