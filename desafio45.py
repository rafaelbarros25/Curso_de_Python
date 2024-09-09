# crie um programa q jogue JokenPo
import random
from time import sleep
print("#"*20,"VAMOS JOGAR JOKENPO","#"*20)
jogo=("Pedra", "Papel", "Tesoura")
print("""Suas Opções:
[0]Pedra
[1]Papel
[2]Tesoura""")
jogador=int(input("Escolha a sua opção: "))
computador=random.randint(0, 2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print("*"*20)
print("O computador escolheu {}.".format(jogo[computador]))
print("O jogador jogou {}.".format(jogo[jogador]))
print("*"*20)
if computador == 0:
    if jogador == 0:
        print ("Deu empate")
    elif jogador == 1:
        print("Parabéns!!!Você Ganhou!!!!!!!!!!!!!!!!!!!!!!!!")
    elif jogador == 2:
        print("Você PerdeuXXXXXXXX")
    else:
        print("Opção Inválida")
elif computador == 1:
    if jogador == 0:
        print ("Você PerdeuXXXXXXXXXXX")
    elif jogador == 1:
        print("Deu empate")
    elif jogador == 2:
        print("Parabéns!!!Você Ganhou!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("Opção Inválida")
elif computador == 2:
    if jogador == 0:
        print ("Parabéns!!!Você Ganhou!!!!!!!!!!!!!!!!!!!!!!!!")
    elif jogador == 1:
        print("Você PerdeuXXXXXXXXX!!!")
    elif jogador == 2:
        print("Deu empate")
    else:
        print("Opção Inválida")
