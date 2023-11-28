print("*********************************\n")
print ("JOGO DE ADIVINHAÇÃO \n\n")
print("********************************* \n")
#declarando o número secreto
numero_secreto = 42
numero_maior = 100
totalTentativas = 3
rodada = 1
#funcao .formart {rodada} de {totalTentaivas} baseada na string 
for rodada in range(1, totalTentativas +1 ):

    print("Tentativas {} de {}".format(rodada, totalTentativas))

    #interação com o usuário
    chute_str = input("digite o seu número de 1 a 100: ")

    #incluindo um texto 
    print("Você digitou", chute_str)

    #declarando que a palavra chute irá receber uma string
    #convertendo
    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior = chute < numero_secreto
    menor = chute > numero_secreto
    media = chute > numero_maior

    
    
    #comparando o valor digitado com o nº secreto "=="
    if (acertou):
        print("você acertou!")
        break
   #adicionando novas tentativas ao usuário
    else :
        if(maior):
            print("VocÊ errou ! O seu chute foi maior do que o número secreto ")
        if(media):
            print("O número que digitou é maior do que o permitido, tente novamente!")
        elif (menor):
            print("VocÊ errou ! O seu chute foi menor do que o número secreto ")
    print("")
    print("")
print("Fim do Jogo!")