import random

def jogar():

    boasvindas()
    palavra_secreta = palavra_randomica()

    letras_certas = qtde_letras(palavra_secreta)
    print(letras_certas)
    
    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()    
        
        if(chute in palavra_secreta):
            marca_chute(chute, letras_certas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
 
        enforcou = erros == 6
        acertou = "_" not in letras_certas       
        print (letras_certas)
    
    if(acertou):
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)
    print ("Fim do Jogo!")

def boasvindas():
    print ("---------------------------")
    print ("Bem vindo ao jogo de Forca!")
    print ("---------------------------")

def palavra_randomica():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def qtde_letras(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_certas[index] = letra
        index += 1

def imprime_msg_vencedor():
    print ("Você ganhou!")

def imprime_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("        ______________        ")
    print("       /              \       ")
    print("      /                \      ")
    print("   /\/                  \/\   ")
    print("   \ |   XXXX    XXXX   | /   ")
    print("    \|   XXXX    XXXX   |/    ")
    print("     |   XXX      XXX   |     ")
    print("     |                  |     ")
    print("      \___   XXXX   ___/      ")
    print("       |\    XXXX    /|       ")
    print("       | |          | |       ")
    print("       |  I I I I I I |       ")
    print("       |   I I I I I  |       ")
    print("        \_          _/        ")
    print("          \________/          ")

def desenha_forca(erros):
    print(" _______    ")
    print(" |/     |   ")

    if(erros == 1):
        print(" |    (o_O)  ")
        print(" |           ")
        print(" |           ")
        print(" |           ")    

    if(erros == 2):
        print(" |    (o_O)  ")
        print(" |      |    ")
        print(" |      |    ")
        print(" |           ") 

    if(erros == 3):
        print(" |    (o_O)  ")
        print(" |    \_|    ")
        print(" |      |    ")
        print(" |           ") 

    if(erros == 4):
        print(" |    (o_O)  ")
        print(" |    \_|_/  ")
        print(" |      |     ")
        print(" |           ") 

    if(erros == 5):
        print(" |    (o_O)  ")
        print(" |    \_|_/  ")
        print(" |      |    ")
        print(" |    _/     ") 

    if(erros == 6):
        print(" |    (x_x)   ")
        print(" |    \_|_/  ")
        print(" |      |    ")
        print(" |    _/ \_  ") 

if(__name__ == "__main__"):
    jogar()
