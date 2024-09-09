# crie um programa q leia um numero de 0 a 9999 e mostre cada um dos digitos separados
# ex; digite um numero: 5648
# unidade: 8
# dezena: 4
# centena: 6
# milhar: 5
#num=(input("Digite um numero de 0 a 9999: "))
#print("A unidade é {}".format(num[3]))
#print("A dezena é {}".format(num[2]))
#print("A centena é {}".format(num[1]))
#print("O milhar é {}".format(num[0]))
# solucao do guanabara

num=int(input("Digite um numero de 0 a 9999: "))
u = num//1%10
d = num//10%10
c = num//100&10
m = num//1000%10
print("A unidade é {}".format(u))
print("A dezena é {}".format(d))
print("A centena é {}".format(c))
print("O milhar é {}".format(m))
