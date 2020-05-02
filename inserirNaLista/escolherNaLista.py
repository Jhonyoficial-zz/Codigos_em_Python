import random

lista = []

for c in range(5):
    a = str(input('digite o nome: '))
    lista.append(a)
print(random.choice(lista))