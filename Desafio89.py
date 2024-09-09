#Crie um programa q leia nome e duas notas de cada aluno
# no final mostre um boletim contendo a media de cada um e permita q o usuario possa consultar as notas de cada aluno
ficha = []
while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? (S/N) '))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}') # :<4 é para alinhar a esquerda com 4 caracteres
for i, a in enumerate(ficha):
    print (f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    opc=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc==999:
        print('Finalizando')
        break
    if opc <=len(ficha)-1: #len(ficha) é a quantidade de alunos cadastrados, -1 pq o primeiro aluno é 0
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') #opc é o numero do aluno, [0] é o nome e [1] sao as notas

