from time import sleep
def counter(a,b,c):
    print(30 * '=-')
    if c < 0:
        c = c * -1
    elif c == 0:
        c = 1
    print(f'Count from {a} to {b}, {c} by {c}:')
    if b >= a:
     b += 1
     for cont in range(a, b, c):
        sleep(0.5),print(cont, end=', ')
     print()
     print('End!')
    elif b < a:
        b -= 1
        for cont in range(a,b, -c):
            sleep(0.5), print(cont, end=', ')
        print()
        print('End!')
        print(30 * '=-')


counter(1,10,1)
counter(10,0,2)
print('Now it´s your to costomize the count!')
a = int(input('Start: '))
b = int(input('End: '))
c = int(input('Step: '))
counter(a,b,c)
