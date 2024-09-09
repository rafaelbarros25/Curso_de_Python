# Crie um programa q mostre a tabuada de varios numeros um de cada vez.
# o programa irá parar qd o numero solicitado for negativo.
while True:
    n = int(input("Digite o numero q deseja mostrar a tabuada: "))
    if n<0:
        break
    print("-"*30)
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, n * c))
    print("-"*30)
print("TABUADA ENCERRADA")


