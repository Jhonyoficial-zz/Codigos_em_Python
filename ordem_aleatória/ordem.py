import random

nomes = ['jhony','david','mateus','lucas']
# escolha = random.choice(nomes)

random.shuffle(nomes)

for i in range(len(nomes)):
    print(nomes[i])