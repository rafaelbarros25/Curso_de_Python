# crie um programa q leia o comprimento de 3 retas e diga ao usuario se ele pode formar um triangulo
#Em qualquer triângulo, a soma das medidas de dois lados é sempre maior que a medida do terceiro.

a=float(input("Digite o primeiro comprimento: "))
b=float(input("Digite o segundo comprimento: "))
c=float(input("Digite o terceiro comprimento "))
if a+b>c and a+c>b:
    print("Os comprimentos citados PODEM formar um triangulo")
else:
    print("Os comprimentos citados NAO PODEM formar um triangulo")

