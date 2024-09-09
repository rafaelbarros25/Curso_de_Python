# Crie um programa q jogue par ou impar.
# o Jogo sera interrompido qd o jogador perder msotrando o numeros de vitorias consecutivas.
print("****** VAMOS JOGAR PAR OU ÍMPAR *********")
count=0
while True:
    n=int(input("Digite digite um valor: "))
    escolha=str(input("Escolha Par ou Impar (P/I): ")).strip().upper()[0]
    import random
    computador=random.randint (1,10)
    soma=n+computador
    print(f"O computador escolheu {computador}, o resultado foi {soma}")
    if escolha == "P":
        if soma%2==0:
            print("vc venceu")
        elif soma%2!=0:
            print("Vc perdeu")
            break
    if escolha == "I":
        if soma%2!=0:
            print("vc Venceu")
        elif soma%2==0:
            print("Vc perdeu")
            break
    count=count+1
print(f"Voce venceu {count} consecutivas")
  #  count=count+1
