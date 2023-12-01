import random
def jogarAdvinhacao():
    print("*********************************\n")
    print ("**** JOGO DE ADIVINHAÇÃO **** \n\n")
    print("********************************* \n")
    #declarando o número secreto

    #numero_secreto = 42
    #criando funcao 

    #aplicando o random para gerar um numero aleatório em toda rodada
    numero_secreto = random.randrange(1,101)

    numero_maior = 101
    totalTentativas = 0
    pontos = 1000
   # print(numero_secreto)

    print("Qual é o nível de dificuldade ?\n")
    print("(1) Fácil (2) Médio (3) Difícil \n") 
    nível = int(input("Defina o nível: "))
    #condicao para tentativas de acordo com o nível escolhido
    if (nível ==1):
        totalTentativas = 20
    elif (nível == 2):
        totalTentativas = 10
    else: 
        totalTentativas = 5



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
            print("você acertou! e fez {} pontos".format(pontos))
            break
    #adicionando novas tentativas ao usuário
        else :
            if(maior):
                print("VocÊ errou ! O seu chute foi menor do que o número secreto ")
            if(media):
                print("O número que digitou é maior do que o permitido, tente novamente!")
            elif (menor):
                print("VocÊ errou ! O seu chute foi maior do que o número secreto ")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print("")
        print("")
    print("Fim do Jogo!")

if(__name__ == "__main__"): #verificando se a variavel possui valor especial
    jogarAdvinhacao()