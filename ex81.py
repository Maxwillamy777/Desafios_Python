list = []
value = cont = 0
print(30 * '=')
print('List analysis!')
print(30 * '=')
while True:
    value = int(input('Enter a value: '))
    list.append(value)
    cont = str(input('You want continue or closed list [y/n]: ')).lower()
    if cont == 'n':
        break
    elif cont !=  'y' and 'n':
     print('Not undenstand, remove value!')
     list.remove(value)
print(40 * '=')
list.sort(reverse=True)
print(f'Quantity numbers: {len(list)}')
print(f'The value in orden descrecent {list}')
if 5 in list:
    print('have [5] in your list!')
else:
    print('Not have [5] in your list!')
print(40 * '=')



