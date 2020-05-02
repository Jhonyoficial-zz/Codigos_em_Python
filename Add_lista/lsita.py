from os import system
from time import sleep

variavel = 1
alunos = []
while(variavel == 1):
    nome = str(input('digite o nome do aluno ou digite SAIR" para sair: '))
    if(nome != 'sair'):
        alunos.append(nome.title().strip())
    elif(nome == 'sair'):
        variavel = False
        print('você escolheu sair!')
        sleep(3)
system('cls')
for i in range(len(alunos)):
    print(alunos[i], end=', ')
