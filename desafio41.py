# crie um programa q leia o ano de nascimento e mostre a categoria
# ate 9 anos: Mirim
# ate 14 infantil
#ate 19 junior
# acima : Master
dob=int(input("Digite sue ano de nascimento: "))
idade=2023-dob
if idade<=9:
    print("Sua categoria é Mirim")
elif idade>9 and idade<=14:
    print("Sua categoria é Infantil")
elif idade<=19:
    print("Sua categoria é Junior")
else:
    print("Sua categoria é Master")
# nesse desafio ele fez igaul ao desafio do alistamento, fez o import da data
# from datetime import date
# atual = date.today().year
# outra informaçao é, nao é preciso colocaar elif idade>9 and idade<=14, pois se ele fosse menos q nove ja ficaria na primeira condiçao,
# entao pode ficar apenas elif idade<=14
