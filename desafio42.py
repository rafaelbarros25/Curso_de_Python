# refaça o desafio 35 acrescentando q tipo de triangulo sera formado:
# Equilatero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno todos os lados diferentes

a=float(input("Digite o primeiro comprimento: "))
b=float(input("Digite o segundo comprimento: "))
c=float(input("Digite o terceiro comprimento: "))
if a+b>c and a+c>b:
    print("Os comprimentos citados PODEM formar um triangulo")
    if a == b and a == c:
        print("O triangulo formado será EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("O triangulo formado será ISOSCELES")
    elif a != b and a != c and b != c:
        print("O triangulo sera ESCALENO")
else:
    print("Os comprimentos citados NÃO PODEM formar um triangulo")

#condiçao aninhada
# uma condiçao dentro da outra


