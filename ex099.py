def highest(*num):
    print(30 * '=-')
    print('Analyzing past values...')
    print(f'{num} They were informed {len(num)} values in total.')
    print(f'The highest value reported {max(num)}.')
    print(30 * '=-')


highest(1, 2, 3, 4, 1, 2, 3, 55, 77, 88, 102, 0)
