conj = {}
a = str(input('Named: '))
conj['nome'] = a
b = float(input(f'The average of {conj["nome"]}: '))
conj['média'] = b
if b < 60.0:
    conj['situação'] = 'disapproved'
elif b >= 60.0:
    conj['situação'] = 'Approved'
print(30 * "=")
print(f' - The name is {conj["nome"]}')
print(f' - The average is: {conj["média"]}.')
print(f' - The situation is {conj["situação"]}.')
print(30 * "=")
