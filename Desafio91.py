#faça um programa onde 4 jogadores joguem um dado e tenham rsultados aleatorios.
# guarde esses resultados em um dicionario.
#no final coloque esse dicionario em ordem, sabendo q o vencedor tirou o maior numero.

from time import sleep
from random import randint
from operator import itemgetter
jogo={'jogador1': randint(1,6),
      'jogador2': randint(1,6),
      'jogador3': randint(1,6),
      'jogador4': randint(1,6)}
print(jogo)
for j, s in jogo.items():
    print(f'O {j} tirou {s}')
    sleep(1)
#para colocar em ordem ele criou outro dicionario Ranking
ranking={}
# teve q importar outro elemento itemgetter
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)  #ordenar pelos numeros tirados, colocou reverse para ordenar do maior numero para o menor
print (ranking)
# o resultado vai sair em forma de lista
#entao na hora de tratar ele, tera q trastar como lista
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)