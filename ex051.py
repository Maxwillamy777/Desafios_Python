N = int(input('Primeiro termo: '))
R = int(input('Razão: '))
D = N + (10 - 1) * R
for i in range(N, D, R):
    print('{} '.format(i), end=',')
print('ACABOU')

