#Crie um programa q tenha uma funçao chamada area q receba as dimensoes de um terreno retangular (largura e comprimento) e
# mostre a area do terreno.













def area(a, b):
    x = a*b
    print(f'A area de um terreno de {a} x {b} é de {x}')



larg=float(input("Digite a largura: "))
comp=float(input("Digite o comprimento: "))
area(larg, comp)
