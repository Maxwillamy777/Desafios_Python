nome = str(input("Qual é seu nome? "))
if nome == 'Max':
    print("Seu nome é elegante!")
elif nome == 'Willamy' or nome == 'Lívia' or nome == "Valda":
    print('Que bom vê você aqui {}!'.format(nome))
elif nome in 'Angelina':
    print('Olá minha filha! ')
else:
    print('Seu nome é tão normal!')
