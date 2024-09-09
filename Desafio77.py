#Crie um programa q tenha uma tupla com varias palavras.
#Depois, o prorama deve mostrar pra cada palavra, suas vogais
palavras=("Bola", "Jogador", "Juiz", "Campo", "Gol", "Apito", "Uniforme", "Treinador", "Falta")
for c in palavras:
    print(f"\nNa palavra {c}, aparecem as vogais: ", end="")
    for letra in c:
        if letra.lower() in "aeiou":
            print(letra.upper(), end=" ")