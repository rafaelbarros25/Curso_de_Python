# crie um programa q leia a DOB de um jovem e informe, de acordo com a idade:
# # se ele ainda vai se alistar
# #se é a hora de se alistar
# # se ja passou do tempo de alistamento
# # O programa tambem devera mostrar o tempo q falta ou o tempo q passou do prazo
dob=int(input("Digite sue ano de nascimento: "))
idade=2023-dob
if idade==18:
    print("Está na hora de se alistar")
elif idade>18:
    print("Ja passou da hora de se alistar. Voce deveria ter se alistado a {} anos atras.".format(idade-18))
    print("O ano do seu alistamento foi em {}.".format(dob+18))
elif idade<18:
    print("Voce devera se alistar em {} anos.".format(18-idade))
# soluçao do guanabara
# ele fez o import da data usando o seguinte:
from datetime import date
atual = date.today().year
nasc=int(input("Digite sue ano de nascimento: "))
IDADE=atual-nasc
print(IDADE)
# de resto foi tudo parecido