# crie um programa q leia 2 notas de um aluno e calcule sua media, mostrando no final de acordo com a media a mensagem:
# abaixo de 5 : reprovado
# entre 5 e 6.9: recuperaçao
# acima de 7: aprovrado
n1=float(input("Digite sua primeira nota: "))
n2=float(input("Digite sua segunda nota: "))
media=(n1+n2)/2
print("Sua media final foi {:.2f}.".format(media))
if media < 5:
    print("Deu mole, vc foi reprovado")
elif media >=5 and media<=6.9:
    print("Vc esta em recuperacao")
else:
    print("Vc foi aprovado")
