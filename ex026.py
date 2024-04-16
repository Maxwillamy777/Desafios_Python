frase = str(input("Escreva uma frase:")).strip()
print('Quantidade de a na frase: {}'.format(frase.lower().count('a')))
print('A posição que aparece o primeiro A: {}'.format(frase.lower().find('a')))
print(('A posição que aparece o último A: {}'.format(frase.lower().rfind('a'))))

