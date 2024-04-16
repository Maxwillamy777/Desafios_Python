salario = float(input('Qual é o salário do funcionário ? R$: '))
aumento = (salario * 15 / 100) + salario if salario <= 1250.00 else (salario * 10 / 100) + salario
print ('O sálario do funcionário R${} e com aumento ficará R${}'.format(salario, aumento))
