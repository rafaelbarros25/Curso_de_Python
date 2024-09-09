# crie um programa q leia varios numeros e coloque-os em uma lista.
# depois disso crie duas listas extras q vao conter apenas valoress pares e impares.
# ao final mostre as 3 listas

lista=[]
pares=[]
impares=[]
while True:
    valor=int(input("Digite um valor: "))
    lista.append(valor)
    if valor%2==0:
        pares.append(valor)
    else:
        impares.append(valor)
    cont=str(input("Quer continuar? (S/N): ")).strip().upper()[0]
    if cont=="N":
        break
print(f"Os numeros digitados foram{lista}")
print(f"Os numeros pares digitados foram {pares}")
print(f"Os numeros impares digitados foram {impares}")
#soluçao do Guanabara:
#for i, v in enumerate(lista):
 #   if v%2==0:
  #      pares.append(v)
   # elif v%2==1:
    #    impares.append(v)