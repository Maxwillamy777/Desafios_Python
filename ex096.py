print(' Terrain Control: ')
print(20 * '-')


def land(a,b):
    cal = a * b
    print(f' The area of land {a}x{b} and is {cal}m°')


a = float(input(' Width (m): '))
b = float(input(' Length (m): '))
land(a, b)
