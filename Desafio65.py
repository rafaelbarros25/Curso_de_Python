#crie um programa q leia varios numeros inteiros pelo teclado
# no final mostre a media entre todos os valores qual o maior, qual o menor.
# o programa deve perguntar ao usuario se ele quer ou nao continuar.
count=0
n=0
soma=0
maior=0
menor=0
parar="S"
while parar=="S":
    n = int(input("Digite um numero inteiro: "))
    parar = str(input("Deseja continuar(S/N): ")).strip().upper()[0]  # Zero entre chaves para considerar apenas a primeira letra
    count=count+1
    soma=soma+n
    if count== 1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n

print(f"A soma de todos os valores foi de {soma}")
print(f"A media dos valores digitados foi de {soma/count}")
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")

#n = int(input("Digite um numero inteiro (999 para parar): "))