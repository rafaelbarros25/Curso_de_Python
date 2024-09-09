#crie um programa q leia o ano de nascimento de 7 pessoas.
# No final mostre quantas pessoas ainda nao atingiram a maioridade e qtas ja sao maiores. Maioridade 21 anos
count=0
menor=0
from datetime import date
atual = date.today().year
for c in range(1, 8):
    n=int(input("Digite seu ano de nascimento: "))
    idade=atual-n
    if idade >= 21:
        count=count+1
    else:
        menor=menor+1
print("Dessas 7 pessoas, {} ainda nao atingiram a maioridade e {} ja sao maiores de idade.".format(menor,count))
