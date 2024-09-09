# crie um programa q mostre na tela uma contagem regressiva para o estouro dos fogoss de artificio,
# # indo de 10 a 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("FELIZ ANO NOVO!!!")


