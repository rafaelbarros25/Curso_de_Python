#melhorar o desafio 61, perguntando ao usuario se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser q quer mostrar 0 termos
primeiro=int(input("Digite o primeiro de sua PA: "))
razao=int(input("Digite a razao de sua PA: "))
termo=primeiro
cont= 1
total=0 #total de termos q o programa vai mostrar
mais=10 #começou com 10 pq é assim q o programa começa, com 10 termos
while mais !=0:
    total=total+mais
    while cont <=total:
        print("{} - ".format(termo), end="")
        termo=termo+razao
        cont=cont+1
    print("PAUSA")
    mais=(int(input("Quantos termos quer mostrar a mais? ")))
print("FIM")
print("Progreçao finalizada com {} termos".format(total))