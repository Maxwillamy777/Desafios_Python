pessoa = dict()
galera = list()
soma = media = 0
while True:
        pessoa.clear()
        pessoa['nome'] = str(input('Nome: '))
        while True:
          pessoa['sexo'] = str(input('Sexo: [m/f] ')).upper()[0]
          if pessoa['sexo'] in 'FM':
              break
          print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['idade'] = int(input('Idade: '))
        soma += pessoa['idade']
        galera.append(pessoa.copy())
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            if resp in 'SN':
                break
        if resp == 'N':
            break
print('-=' * 30)
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f' B) A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end=',')
for p in galera:
    if p['sexo'] == 'Ff':
        print(f'{p["nome"]} ', end='')
print(f' D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')

