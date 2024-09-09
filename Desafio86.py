#Crie um programa q crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado
#"Digite um valor para [0, 0]: "
#"Digite um valor para [0, 1]: "
#"Digite um valor para [0, 2]: "
#"Digite um valor para [1, 0]: "
#"Digite um valor para [1, 1]: "
#"Digite um valor para [1, 2]: "
#"Digite um valor para [2, 0]: "
#"Digite um valor para [2, 1]: "
#"Digite um valor para [2, 2]: "

matriz = [[0,0,0], [0,0,0],[0,0,0]] # ele ja criou as matrizes com a estruta e com elementos 0 paa depois ir substituindo.
for l in range(0,3): #criou l para linha e c para coluna
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range (0,3): # esse outro for é para mostrar a estrutura na tela
    for c in range (0,3):
        print(f'[{matriz[l][c]}]', end='')
    print() # toda vez q ele terminar um for, ele vai quebrar a linha

