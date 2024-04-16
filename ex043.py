p = float(input('Qual é seu peso? (kg) '))
a = float(input('Qual é seu tamanho? (m) '))
imc = p / (a * a)
print(' Seu IMC {:.1f} e a sua classificaçao:'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal, PARABÉNS!')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso!')
elif  imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida!')