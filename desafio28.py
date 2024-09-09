# Escreva um programa q faça o computador "pensar" em um numero inteiro entre 0 e 5 epeça para o usuario tentar descobrir qual foi o numero escolhido pelo pc.
# O programa devera escrever na tela se o usuario ganhou ou perdeu.

import random
print("-----Vai Começar o jogo----")
n=int(input("Escolha um numero entre 0 e 5: "))
#lista = [0,1,2,3,4]
r= random.randint(0, 5)
print(r)
if r == n:
    print("Boa!!! Voce Ganhou")
else:
    print("Que Pena!!! Voce Perdeu!!!")

# Soluçao Guanabara
# ele ja importou direto a funçao randint (random de numeros inteiros)
# from random import randint
#













