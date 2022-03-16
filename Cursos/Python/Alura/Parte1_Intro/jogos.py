import forca
import adivinhacao

def escolha_jogo():
    print ("---------------------------")
    print ("----Escolha o seu Jogo-----")
    print ("---------------------------")

    print ("(1) Forca  (2) Adivinhação")

    jogo = int(input ("Qual jogo? "))

    if(jogo == 1):
        print ("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print ("Jogando Adivinhação")
        adivinhacao.jogar()
    print ("Fim do Jogo!")

if(__name__ == "__main__"):
    escolha_jogo()