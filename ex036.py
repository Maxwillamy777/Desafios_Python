casa = int(float(input("Qual é o preço da casa? R$: ")))
salario = int(float(input('Por favor, qual é seu sálario para procedermos? R$: ')))
anos = int(input('Quantos anos vc pretende pagar?: '))
prest = anos * 12
prestacao = casa / prest
if prestacao >= salario * 30 / 100:
    print('Certo , seu empréstimo será concedidio !')
else:
    print('Lamento , seu empréstimo está negado !')
