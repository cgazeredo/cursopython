import random

al1 = input('Nome do aluno 1: ')
al2 = input('Nome do aluno 2: ')
al3 = input('Nome do aluno 3: ')
al4 = input('Nome do aluno 4: ')

sorteio = random.choice([al1, al2, al3, al4, al1])
print('Quem vai apagar o quadro é {}'.format(sorteio))

