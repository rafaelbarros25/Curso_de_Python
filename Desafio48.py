# crie um programa q calcule a soma entre todos os numeres impares q sao multiplos de 3 no intervalo de 1 a 500.
soma=0
cont=0
for c in range (3,501,3):
   if c %3 ==0 and c%2!=0:
      cont=cont+1
      soma = soma + c
print("A soma de todos os {} valores solicitados é de {}.".format(cont,soma))

