# coding: utf-8

idade = input('qual a sua idada? ')


if not idade.isnumeric():
    print('digite apenas números!')
else:
    idade = int(idade)
    msg = 'pode acessar' if idade >= 18 else 'não pode acessar'
    print(msg)
