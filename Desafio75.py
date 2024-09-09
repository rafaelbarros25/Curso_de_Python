# Crie um programa q leia 4 valores pelo teclado e guarde-os numa tupla, no final mostre:
#a- quantas vezes apareceu o valor 9
# b- em q posiçao foi digitado o primeiro valor 3
# c- quais foram os numeros pares
lista=(int(input("Digite o primeiro valor: ")),
int(input("Digite o segundo valor: ")),
int(input("Digite o terceiro valor: ")),
int(input("Digite o quarto valor: ")))
pares=("")
print(f"O seus numero digitados fora: {lista}")
print(f"Os valores pares digitados foram ", end="")
for c in lista:
    if c%2==0:
        print(c, end=" ")
if 9 in lista:
    print(f"O número 9 apareceu {lista.count(9)} vezes")
else:
    print("O número 9 nao foi digitado nenhuma vez")
if 3 in lista:
    print (f"O número 3 aparece na posiçao {lista.index(3)+1}.")
else:
    print (f"O número 3 não foi digitado nenhuma vez")