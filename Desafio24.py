# crie um programa q leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"

cid = str(input("Digite o nome de uma cidade: ")).strip()
# ele meteu .strip() para eliminar espacos em caso a pessoa digite alguns espacos antes de colocar o nome da cidade

print(cid[:5].upper() == "SANTO")
# ele meteu .upper() para formatar qq forma q o usuario escreve santo para maiuscula e comparar