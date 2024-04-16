even = []
odd = []
list = []
g = (20 * '=')
print(f'{g}The list in even and odd!{g}')
while True:
    value = int(input('Enter a number for the list: '))
    list.append(value)
    if len(list) > 5:
        answer = str(input('Do you want to continue [y/n]? '))
        if value % 2 == 0:
            even.append(value)
        if value % 2 != 0:
            odd.append(value)
        if answer == 'n':
            break
        if answer != 'y' and 'n':
            print('I don´t understand, I removed the last value!')
            list.remove(value)
            if value in even:
                even.remove(value)
            else:
                odd.remove(value)
    elif value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
print(40 * '=')
print(f'You list{list}')
print(f'even number list{even}')
print(f'odd number list{odd}')
print(40 * '=')
