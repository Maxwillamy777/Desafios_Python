temp = []
prince = []
while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: ')))
    if len(prince) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prince.append(temp[:])
    temp.clear()
    answer = str(input('Do you want continue? [y/n]'))
    if answer in 'Nn':
        break
print('-=' * 30)
print(f'In total, it was registered [{len(prince)}] peoples.')
print(f'The heaviest weight was {mai}Kg. weight of ', end='')
for p in prince:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'The lowest weight was {men}Kg. weight of ', end='')
for p in prince:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
