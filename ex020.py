from random import shuffle
n = input('O primeiro aluno: ')
n2 = input('O segundo aluno: ')
n3 = input('O terceiro aluno: ')
n4 = input('O quarto aluno: ')
l = [n, n2, n3, n4]
shuffle(l)
print('A ordem dos alunos escolhidos foi:')
print(l)
