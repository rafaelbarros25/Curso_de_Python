# refaça o desafio 9 mostrando a tabuada de um numero q o usuario escolhers, agora utilizando o laço for
## desafio 9: faca um programa q leia um numero qualquer e mostre na tela sua tabuada
num = int(input("Digite um numero: "))
for c in range (1, 11):
    print("{} x {} = {}".format(num, c, num*c))

# o range vai ser a tabuada
