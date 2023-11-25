print("*********************************\n")
print ("JOGO DE ADIVINHAÇÃO \n\n")
print("********************************* \n")



#declarando o número secreto
numero_secreto = 42

totalTentativas = 3
rodada = 1

while( rodada <= totalTentativas ):
    print("Tentativas", rodada, "de", totalTentativas)

    #interação com o usuário
    chute_str = input("digite o seu número:  \n")

    #incluindo um texto 
    print("Você digitou", chute_str)
    #declarando que a palavra chute irá receber uma string
    #convertendo
    chute = int(chute_str)
    #comparando o valor digitado com o nº secreto "=="

    if (numero_secreto == chute):

        print("você acertou!")


    #adicionando novas oportunidas ao usuário



    else :
        if(chute > numero_secreto):

            print("VocÊ errou ! O seu chute foi maior do que o número secreto ")

        elif (chute < numero_secreto):

            print("VocÊ errou ! O seu chute foi menor do que o número secreto ")

    rodada = rodada + 1
    print("")
    print("")

    print("Fim do Jogo!")