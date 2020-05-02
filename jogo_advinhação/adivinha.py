from random import randint
import os

num = randint(1,10)
cont = 0
tentativas = 0
while cont == 0:
    palpite = int(input('digite um numero entre 1 e 10?  '))
    os.system('cls')
    tentativas += 1
    if palpite == num:
        print(f'você acertou em {tentativas} tentativas!')
        cont = 1

    elif palpite > num:
        print('digite um numero menor !')
    else: 
        print('digite um numero maior! ')

    

