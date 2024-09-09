# Crie um programa q leia um numero real qualquer pelo teclado e mostre na tela sua porcao inteira.
import math
num = float(input("Digite um numero qualquer: "))
par = math.trunc(num)
print("A parte inteira do numero {} é {}".format(num,par))

#resolucao do Guanabara

from math import trunc
print("A parte inteira do numero {} é {}".format(num,trunc(par)))

