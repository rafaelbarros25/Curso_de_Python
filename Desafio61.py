# refaça o desafio 51, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da PA usando o while
primeiro=int(input("Digite o primeiro de sua PA: "))
razao=int(input("Digite a razao de sua PA: "))
termo=primeiro
cont= 1
while cont <=10:
    print("{} - ".format(termo), end="")
    termo=termo+razao
    cont=cont+1
print("FIM")


