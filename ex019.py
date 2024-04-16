import random
n1 = input('O nome do 1°aluno(a): ')
n2 = input('O nome do 2°aluno(a): ')
n3 = input('O nome do 3°aluno(a): ')
n4 = input('O nome do 4°aluno(a): ')
a = [n1, n2, n3, n4]
escolhido = random.choice(a)
print('O aluno(a) escolhido foi {}'.format(escolhido))
