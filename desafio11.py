# desafio 11: faca um programa q leia a altura e largura da parede em metros, calcule a area e qtd de tinta necesserario. Sabendo q um litro pinta 2m2
alt=input("Digite aa altura em metros: ")
lar=input("Digite a largura em metro: ")
area=float(alt)*float(lar)
lit=area/2
print("Voce irá precisar de {} litros de tinta para pintar a area de {}m2 de sua parede.".format(lit,area))

#resolucao do Guanabara
