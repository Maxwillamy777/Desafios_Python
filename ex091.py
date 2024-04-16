from random import randint
from time import sleep
from operator import itemgetter
game = {}
print(15 * '=-')
print('DRAWN-VALUES:')
game['kicker1'] = randint(1,6)
game['Kicker2'] = randint(1,6)
game['Kicker3'] = randint(1,6)
game['Kicker4'] = randint(1,6)
for K, d in game.items():
    print(f'{K}: {d}.')
    sleep(1)
print(15 * '=-')
print('Kicker-Raking:')
ranking = list()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    i += 1
    print(f'{i}° place: {v[0]} with {v[1]}.')
    sleep(1)
print('Finally!')
