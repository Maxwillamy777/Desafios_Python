a = int(float(input('O primeiro valor: ')))
b = int(float(input('O segundo valor: ')))
if a > b:
    print("O maior valor é {}".format(a))
if b > a:
    print("O maior valor é {}".format(b))
elif a == b:
    print("Os valores são iguais!")
