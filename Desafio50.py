# crie um programa q leia seis numeros inteiros e mostre a soma apenas daqueles q forem pares. Se o valor for impar, desconsidere.
count=0
for c in range(1, 7):
    n=int(input("Digite um numero inteiro: "))
    if n % 2 == 0:
        count=count + n
print(count)
