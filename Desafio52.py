#Crie um programa q leia um numero inteiro e diga se ele é ou nao um numero primo.
n=int(input("Digite um numero: "))
tot = 0
for c in range (1, n+1): #ele criou isso para dividir por todos os numeros ate o numero digitado
    if n%c==0:
        print("\033[33m", end="")
        tot = tot + 1 # isso é para verificar por qtos numeros o numero digitado é divisivel
    else:
        print ("\033[31m", end="")
    print("{} ".format(c), end="")
print("\n\033[mO numero {} foi divisivel {} vezes". format (n,tot))
if tot==2:
    print("e por isso o número É PRIMO")
else:
    print("e por isso o número NÃO É PRIMO")
