import random
import linecache
import sys
import os

print("**************************")
print("BEM VINDO AO JOGO DA FORCA")
print("**************************\n\n\n")

class escolha:
    print("1 - Países\n2 - Nomes\n3 - Frutas\n4 - Geral")
    categoria = input("Em qual categoria você deseja brincar?")
    if categoria == "1":
        lista = "paises.txt"
    elif categoria == "2":
        lista = "nomes.txt"
    elif categoria == "3":
        lista = "frutas.txt"
    else:
        lista = "geral.txt"

    count = 0
    with open(lista, 'rb') as f:
        for line in f:
            count += 1

def main():
    lista = escolha.lista
    count = escolha.count
    y = random.randint(1, count)
    segredo = linecache.getline(lista, y).strip()
    segredo = segredo.upper()

    segredo_lista = list(segredo)
    x = 0
    forca = 3

    print("A palavra secreta tem {} letras!\n".format(len(segredo)))

    espaco = []

    for i in range(0, len(segredo)):
        espaco.append("_")

    print("           ", end="    ")
    print("".join(espaco))
    print("Você tem {} chances".format(forca))

    while espaco != segredo_lista and int(forca) > 0:
        chute = input("Chute uma letra: ")
        chute = chute.strip()
        if chute == "":
            continue
        if chute == "inicio":
            escolha.inicio()
        if chute.upper() in segredo:
            for x in range(0, len(segredo)):
                if chute.upper() in segredo[x]:
                    espaco[x] = segredo[x]
        elif chute.upper() not in segredo:
            forca = forca - 1
        print("           ", end="    ")
        print("".join(espaco))
        if forca > 0 and espaco != segredo_lista:
            print("Você tem {} chances".format(forca))
        elif forca <= 0 and espaco != segredo_lista:
            print("Você perdeu!")
            print("A palavra era {}\nTente de novo!\n".format(segredo))
            main()

        if espaco == segredo_lista:
            print("Você ganhou!!\nTente mais uma!\n")
            main()


main()