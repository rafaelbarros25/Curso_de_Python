# crie um programa q vai ler vairios numeros e colocar numa lista
#Depois mostre:
#a- Quantos numeros foram digitados
# B- a lista de valores ordenada de forma descrecente
#C - se o valor 5 foi digitado e esta ou nao na lsita
# O valor 5 foi encontrado na lista
lista=[]
while True:
    valor=int(input("Digite um valor: "))
    lista.append(valor)
    cont=str(input("Quer continuar? (S/N): ")).strip().upper()[0]
    if cont=="N":
        break
print(f"Foram digitados {len(lista)} números.")
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print ("O valor 5 foi digitado")
else:
    print("O valor 5 não foi digitado")
