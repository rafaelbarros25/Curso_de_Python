#crie um programa leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.
import math
cata=float(input("Digite o comprimento do cateto oposto: "))
cato=float(input("Digite o comprimento do cateto adjacente: "))
hi = (cata**2 + cato**2) ** (1/2)
hipo=math.hypot(cata, cato)
print("O comprimento da hipotenusa é de {} ou {}".format(hi,hipo))


