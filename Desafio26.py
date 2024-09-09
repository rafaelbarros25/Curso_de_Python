# crie um programa q leia a frase pelo teclado e mostre
# qtas vezes aparece a letra "a"
# em q posicao ela aprece pela primeira vez
# em q posicao ela aparece pela ulyima vez
frase=str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes.".format(frase.count("A")))
print("A primeira letra A aparece na posicao {}.".format(frase.find("A")+1))
# ele meteu o +1 para fazer mais sentido para o usuario
print("A ultima letra A aparece na posicao {}.".format(frase.rfind("A")+1))
#rfind comeca a contar da direita pra esquerda


# print(frase.find("a"))

