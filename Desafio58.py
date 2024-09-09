# melhore o jogo do desafio 28 onde o comupatador vai pensar em numero entre 0 e 10.
# o jogador vai tentar advinhar ate acertar, mostrando no final quantos palpites foram necessarios p vencer.
import random
print("-----Vai Começar o jogo----")
r= random.randint(1, 10)
n=int(input("Escolha um numero entre 1 e 10: "))
count=1
while r != n:
    print("Que Pena!!! Voce Perdeu!!!")
    print("Tente novamente")
    n = int(input("Escolha um numero entre 1 e 10: "))
    count=count+1
print("Boa!!! Voce Ganhou")
print("Voce precisou de {} tentativas".format(count))