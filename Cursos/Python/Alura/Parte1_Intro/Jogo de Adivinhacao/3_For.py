print ("---------------------------------------------------------")
print ("           Bem vindo ao jogo de Adivinhação")
print ("---------------------------------------------------------")

numero_secreto = 42
tentativas = 3

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

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("VOCÊ ACERTOU!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o numero secreto.")
            print ("---------------------------------------------------------")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o numero secreto.")
            print ("---------------------------------------------------------")

    rodada = rodada + 1

print("Fim de Jogo")
