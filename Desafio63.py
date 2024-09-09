# crie um programa q leia um numero n inteiro qualquer e mostre na tela os n primeiros elemento de uma sequencia de Fibonacci
print("#"*30)
print("SEQUENCIA DE FIBONACCI")
print("#"*30)
n=int(input("Digite quantos termos vc quer mostrar: "))
t1=0 #esses dois primeiros termos (t1 e t2 ja sao definidos
t2=1
print("~"*30)
print("{} -> {}".format(t1, t2), end="")
cont=3 #contador começa no 3 pq os dois primeiros termos ele ja mostrou
while cont<= n:
    t3= t2 + t1
    print(" -> {}".format(t3), end="")
    t1=t2
    t2=t3 # agora ele mudou o t1 para ser o t2 e o t2 para ser o t3 para os numeros andarem pra frente
    cont = cont + 1
print(" -> FIM")
print("~"*30)


#