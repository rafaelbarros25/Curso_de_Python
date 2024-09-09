# crie um programa q leia um numero qq e mostre o seu fatorial:
# ex 5!= 5x4x3x2x1=120
# essa é a maneira mais simples usando factorial de math
from math import factorial
valor=int(input("Digite um numero para calcular seu Fatorial: "))
f = factorial(valor)
print(f)

# agora ele quis fazer manualmente, usando while
valor=int(input("Digite um numero para calcular seu Fatorial: "))
c=valor
f=1
while c>0:
    print("{}".format(c), end="") # ele coloca o end= para deixar tudo na mesma linha
    print(" x " if c >1 else " = ", end="") # ele colocou if dentro do print
    f=f*c
    c=c-1 #
print(f)



