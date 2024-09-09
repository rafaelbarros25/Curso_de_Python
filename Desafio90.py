# faça um programa q leia o nome e media de um aluno, guardando tb a situaçao em um dicionario.
#no final mostre o conteudo da estrutura na tela.
# se media for maior ou igual a 7 ta aprovado

boletim={}
boletim['Nome']=str(input('Nome: '))
boletim['Média']=float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média']>=7:
    boletim['Situação']='Aprovado'
elif boletim['Média']<7:
    boletim['Situação']='Recuperação'
print(boletim)

for c, v in boletim.items():  # ele criou isso para ficar melhor apresentado
    print(f'{c} é igual {v}')

