#Crie um programa q ajude o usuario a jogar na mega sena (1 a 60):
# O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros p cada jogo, cadastrando tudo em uma lista composta.
from random import randint
cont = 0
lista=[]
jogos=[]
quant=int(input("Quantos jogos vc quer q eu sorteie: "))
tot=1
while tot <= quant:
    cont=0
    while True:
        num=randint(1, 60)
        if num not in lista: # esse if é para nao repetir um numero no mesmo jogo
            lista.append(num)
            cont=cont+1
        if cont>=6:
            break # braeak qd a lista tem 6, criou um jogo
    lista.sort()
    jogos.append(lista[:]) # para cada jogo ele criou uma lista temporaria
    lista.clear()
    tot=tot+1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

