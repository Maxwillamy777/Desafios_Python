from random import randint
n = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10),randint(1,10)]
print(n,end=',')
print('Analysis:')
l = sorted(n)
print(f'The highest value was {l[4]}')
print(f'and smallest value was {l[0]}')
print('FINISHED!')


