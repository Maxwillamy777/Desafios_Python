conj = []
x = 0
r = 0
while True:
    name = str(input('Name: '))
    conj.append([])
    r += 1
    n1 = float(input('Note 1: '))
    n2 = float(input('Note 2: '))
    conj[x].append(name)
    conj[x].append(n1)
    conj[x].append(n2)
    conj[x].append((n1 + n2) / 2)
    ans = str(input('Want continue [y/n]? ').lower())
    if ans[0] == 'n':
        break
    else:
        x += 1
for cont in range(0, r):
    print(f'Student: {conj[cont][0]} and its average: {conj[cont][3]}.')
while True:
    num = int(input('Number: '))
    print(f'{conj[num][0]} your notes: {conj[num][2]},{conj[num][3]}.')
    if num == 999:
        break
print('Finashed!')
