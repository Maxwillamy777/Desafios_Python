lis = {'player': str(input('Name of player: '))}
n = int(input(f'How many games did {lis["player"]} play: '))
departure = list()
for cont in range(0, n):
    cont += 1
    departure.append(int(input(f'In the {cont}°match, when he scored goals: ')))
lis['goals'] = departure[:]
lis['total'] = sum(departure)
print('-=' * 30)
print(lis)
print('-=' * 30)
for k, v in lis.items():
    print(f'The site {k} have the value {v}')
print('=-' * 30)
print(f'The player {lis["player"]} it played {len(lis["goals"])} departures')
for i, v in enumerate(lis['goals']):
    print(f'     => In departure {i}, make {v} goals.')
print(f'It was total of {lis["total"]} goals.')
