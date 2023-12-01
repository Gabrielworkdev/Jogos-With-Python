
def jogarForca():
    print("*********************************\n")
    print ("*** BEM VINDO AO JOGO DE FORCA ***\n")
    print("********************************* \n")

    palavra_secreta = "banana"

    enforcou = False # variavel booleana - RETORNA FALSO OU VERDADEIRA 
    acertou = False
    #enquanto n se enforcouo E n acertou - segue o jogo
    while(not enforcou and not acertou): #palavras chave no python sempre se usa em letras minúscula
        
        chute = input("Qual Letra?")
        # for verificque a letra dentro de palavra !

        index = 0 #posição de cada letra.
        for letra in palavra_secreta:
            if (chute == letra):
                 print("Encontrei a letra  na posição ")#.format(letra, index)) #interpolação de string
            index = index +1 #incrimentando a dados  a cada letra 

    print("Jogando...")
             
    print("Fim do Jogo!")
if(__name__ == "__main__"): #verificando se a variavel possui valor especial e só executa quando selecionamos a mesma.
    jogarForca()