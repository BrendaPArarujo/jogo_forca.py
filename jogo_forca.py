import random


def jogo():
    inicializa_jogo()
    sorteada = criar_lista().upper()
    palavra_lista = ["_" for i in sorteada]
    acertou = False
    enforcou = False
    erros = 0
    print(palavra_lista)
    while (not acertou and not enforcou):
        chute = pedir_chute()
        if chute in sorteada:
            verifica_letra(sorteada, chute, palavra_lista)
        else:
            erros += 1
            print(erros)
            desenha_forca(erros)

        print(palavra_lista)
        enforcou = erros == 7
        acertou = "_" not in palavra_lista
        if acertou:
            imprime_mensagem_vencedor()
        if (enforcou):
            imprime_mensagem_perdedor(sorteada)


def inicializa_jogo():
    print("----------------------------")
    print("Iniciando o jogo da forca!")
    print("----------------------------")


def criar_lista():
    lista = ["banana", "maca", "uva"]
    numero = random.randrange(0, len(lista))
    return lista[numero]


def pedir_chute():
    chute = input("Chute uma letra: ").upper()
    return chute


def verifica_letra(sorteada, chute, palavra_lista):
    index = 0
    for i in sorteada:
        if chute == i:
            palavra_lista[index] = chute
        index += 1


def imprime_mensagem_perdedor(word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogo()


