# Crie um programa q gere 5 numeros aleatorios e coloque numa tupla
# depois, mostre a listagem dos numeros gerados e tambem indique o menor e o maior valor
from random import randint
# para criar uma tupla com 5 numeros ele abriu parenteses antes e fez randint 5 vezes:
n = (randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10))
maior=menor=0
for c in n:
    if c > maior:
        maior=c
print (n)
print(f"O maior valor da lista é {max(n)}") #max e min sao funcionalidades da Tupla e de outros metodos
print(f"O menor valor da lista é {min(n)}")
