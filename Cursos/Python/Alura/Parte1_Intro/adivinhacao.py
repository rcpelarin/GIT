import random

def jogar():
    print ("---------------------------------------------------------")
    print ("           Bem vindo ao jogo de Adivinhação")
    print ("---------------------------------------------------------")

    secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print ("Defina o nivel de dificuldade")
    print ("(1) Fácil   (2) Médio   (3) Difícil")
    nivel = int(input())

    if (nivel == 1):
        tentativas = 10
    elif (nivel == 2):
        tentativas = 8
    else:
        tentativas = 6

    for rodada in range (1, tentativas + 1):
        print ("Tentantiva {} de {}".format(rodada, tentativas))

        chute_str = input ("Digite um número entre 1 e 100: ")
        print ("Voce digitou", chute_str)
        print ("---------------------------------------------------------")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print ("Você deve digitar um número entre 1 e 100!")
            print ("---------------------------------------------------------")
            continue

        acertou = chute == secreto
        maior = chute > secreto
        menor = chute < secreto

        if(acertou):
            print("VOCÊ ACERTOU E FEZ {} PONTOS!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o numero secreto.")
                print ("---------------------------------------------------------")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o numero secreto.")
                print ("---------------------------------------------------------")
            pontos_perdidos = abs(secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
