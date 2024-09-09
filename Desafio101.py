# Crie um programa q tenha uma funçao chamada voto() q vai receber como parametro o ano de nascimento de uma pessoa,
# retornado um valor literal indicando se uma pessoa tem voto Negado, Opcional ou Obrigatorio nas eleiçoes

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade=atual-ano
    if idade<18 and idade >=16 or idade >=65:
        return f'Com idade {idade}: Voto Opcional!'
    if idade >18 and idade <=65:
        return f'Com idade {idade}: Voto Obrigatório!'
    if idade<16:
        return f'Com idade {idade}: Voto Negado'

nasc = int(input('Em q ano vc nasceu? '))
print(voto(nasc))



# escopo de importaçao