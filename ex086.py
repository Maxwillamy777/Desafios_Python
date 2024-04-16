matrix = [[],[],[]]
i = 0
t = 0
k = 0
l = (10 * '-=')
print(f'{l}MATRIX{l}')
for m in range(1,10):
    num = int(input(f'Enter a number for [{t,k}]: '))
    k += 1
    if k > 2:
        k -= 3
        t += 1
    matrix[i].append(num)
    if m == 3 or m == 6:
        i += 1
print('YOUR MATRIX:')
print(f'[{matrix[0][0]:^5}] [{matrix[0][1]:^5}] [{matrix[0][2]:^5}]')
print(f'[{matrix[1][0]:^5}] [{matrix[1][1]:^5}] [{matrix[1][2]:^5}]')
print(f'[{matrix[2][0]:^5}] [{matrix[2][1]:^5}] [{matrix[2][2]:^5}]')
