print ("---------------------------------------------------------")
print ("           Bem vindo ao jogo de Adivinhação")
print ("---------------------------------------------------------")

numero_secreto = 42
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    print ("Tentantiva {} de {}".format(rodada, tentativas))
    chute_str = input ("Digite o seu numero: ")
    print ("Voce digitou", chute_str)
    print ("---------------------------------------------------------")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o numero secreto.")
            print ("---------------------------------------------------------")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o numero secreto.")
            print ("---------------------------------------------------------")

    rodada = rodada + 1

print("Fim de Jogo")
