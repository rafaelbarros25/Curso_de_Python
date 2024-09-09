#faça um programa q leia nome, ano de nascimento, carteira de trabalho e cadastre-os (com idade) em um dicionario.
# se por acaso a CT (carteira de trabalho) for diferente de zero, o dicionario tb recebera o ano de contrataçao e o salario.
#calcule e acrescente, alem da idade, com qtos anos a pessoa vai se aposentar (35 anos de trabslho)
# se a carteira de trabalho 0. break
from datetime import date
atual = date.today()
ano= (atual.year)
dados={}
dados['Nome']=str(input('Nome: '))
anonasc=int(input('Ano de nascimento: '))
dados['Idade']=ano-anonasc
dados['Carteira de Trabalho']=int(input('Carteira de Trabalho: (digite 0 se não tiver): '))
if dados['Carteira de Trabalho']!=0:
    dados['Ano de Contratação']=int(input('Ano de contratação: '))
    dados['Salário']=float(input('Salário: R$ '))
    anoapo=(dados['Ano de Contratação']+35)
    idadeapo=anoapo-anonasc
    dados['Aposentadoria']=idadeapo
    print('-=' * 30)
    print(f'Voce irá se aposentar no ano de {anoapo}, com {idadeapo} anos.')
print('-='*30)
print(dados)

# aposentadoria=(ano de contrataçao + 35)-idade
for c, v in dados.items():
    print(f'{c} é igual {v}')



