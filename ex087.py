space = (10 * '==')
spc = (12 * ' ')
print(f'{space}MATRIX-ANALYSIS{space}')
data = [[],[],[]]
n = 0
i = 0
y = 0
z = 0
h = 0
n1 = 0
for cont in range(1, 10):
    n = int(input(f'Enter a number for [{z, y}]: '))
    if cont > 3 and cont <= 6:
        if n1 < n:
            n1 = n
    if n % 2 == 0:
        h += n
    y += 1
    if y > 2:
        y -= 3
        z += 1
    data[i].append(n)
    if cont == 3 or cont == 6:
        i += 1
print('YOUR MATRIX:')
print(f'{spc}[{data[0][0]:^5}] [{data[0][1]:^5}] [{data[0][2]:^5}]')
print(f'{spc}[{data[1][0]:^5}] [{data[1][1]:^5}] [{data[1][2]:^5}]')
print(f'{spc}[{data[2][0]:^5}] [{data[2][1]:^5}] [{data[2][2]:^5}]')
print('ANALISE:')
print(f'The sun of all even numbers: [{h}].')
print(f'The sum of the value in the bird column: [{data[0][2] + data[1][2] + data[2][2]}].')
print(f'The largest value in the second line: [{n1}].')
