# desafio 6: Crie um algoritmo q leia o numero e mostre seu dobro, triplo e raiz quadrada
num = input("Digite um numero: ")
x = float(num)
print("O seu dobro é:", x*2)
print("O seu triplo é:", x*3)
print("Sua raiz quadrada é:", x**0.5)

#resolucao do Guanabara

n = int(input("Digite um numero: "))
d = n*2
t = n*3
r = n**(1 / 2)
print("O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é {:.2f}".format(n,d,n,t,n,r))
#na linha de cima, o :.2f serve para serve para limitar a 2 casas decimais flutuantes
