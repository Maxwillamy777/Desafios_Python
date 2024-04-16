list = list()
for cont in range(1, 11):
    value = int(input('Enter a value: '))
    if value in list:
        print('Duplicate value, I will not add it to the list!')
    else:
        list.append(value)
print(f'Your list:{list.sort()}')
