import Forca
import Adivinhação

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        Forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        Adivinhação.jogar()

        print("Fim do jogo")

if(__name__ == "__main__"):
    escolhe_jogo()
