#Crie um tupla com os 20 primeiros colocados do camp brasileiro, em ordem de colocaçao.
#Depois mostre:
#a- Apenas os 5 primeiros colocados
#b- os ultimos 4
#C- lista com os times em ordem alfabetica
#d - em q posiçao esta o chapecoense
tabela=("Botafogo", "Palmeiras", "Cruzeiro", "Fortaleza", "São Paulo", "Fluminense", "Grêmio", "Inter", "Bahia", "Atletico-PR", "Vasco", "Bragantino", "Cuiaba", "Santos", "Atlético-MG", "Flamengo", "Corinthians", "Goiás", "Chapecoense", "America-MG")
print("-="*15)
print(f"Os cinco primeiros colocados do campeonato brasileiro são: {tabela[0:5]}")
print("-="*15)
print(f"Os ultimos 4 times do campeonato brasileiro são: {tabela[16:]}")
print("-="*15)
print(f"A tabela do campeonato brasileiro em ordem alfabética é: {sorted(tabela)}")
print("-="*15)
chape=tabela.index("Chapecoense")
print (f"A posiçao do Chapecoense é {chape+1}")

#tambem pode fazer assim:
#for time in tabela:
 #   print (time)


