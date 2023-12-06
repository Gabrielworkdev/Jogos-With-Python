
def jogarForca():
    print("*********************************\n")
    print ("*** BEM VINDO AO JOGO DE FORCA ***\n")
    print("********************************* \n")

    arquivo = open("palavras.txt", "r") #selecionando a palavra aleatoriamente
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        

    arquivo.close()
    print(palavras)

    palavra_secreta = "banana".upper()#fixando a palavra como caixa alta
    letra_acertada = [] #onde os acertos entram
    
    for letra in palavra_secreta: #FOR PARA AUTO INCRIMENTO DOS ESPAÇOS DE ACORDO COM O CHUTE
        letra_acertada.append("_")

    enforcou = False # variavel booleana - RETORNA FALSO OU VERDADEIRA 
    acertou = False
    erros = 0 #tentativas

    #enquanto n se enforcouo E n acertou - segue o jogo
    while(not enforcou and not acertou): #palavras chave no python sempre se usa em letras minúscula
        
        chute = input("Qual Letra?")
        chute = chute.strip().upper()#usado para retirar os espaços no inicio e final
        
        # for verificque a letra dentro de palavra !
        if(chute in palavra_secreta):#verificando se  o chute condis dentro de palavra secreta
            index = 0 #posição de cada letra.
            for letra in palavra_secreta: #in verificando o valor dentro da variável
                if (chute.upper() == letra.upper()):#coloca o texto em maiúsculo
                    letra_acertada[index] = letra #guardando as letras corretas inseridas pela usuario
                index = index + 1 #incrimentando a dados  a cada letra 
        else:
            erros = erros + 1 #incrmento
            print("errou, tente novamente!")
        enforcou = erros == 6 #limitando a 6 tentativas
        acertou = "_" not in letra_acertada #enquanto n acertou n deve estar dentro de letras acertadas
        print(letra_acertada)#imprimindo os espaços vazios 
    if(acertou):
        print("Parabéns, você acertou todas as letras!")
    else:
        print("Você perdeu, tente novamente")
    print("Fim do Jogo!")
if(__name__ == "__main__"): #verificando se a variavel possui valor especial e só executa quando selecionamos a mesma.
    jogarForca()