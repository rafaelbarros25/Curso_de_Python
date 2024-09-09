# crie um programa q pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem, combrando £0.50 por km para viagens ate 200km e £0.45 para viagens mais longas.

dis=float(input("Qual a distancia da viagem? "))
if dis>200:
    preco=0.45*dis
else:
    preco=0.5*dis
print("O preço de sua passagem será de {:.2f} reais.".format(preco))

