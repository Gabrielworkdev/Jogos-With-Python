
def jogarForca():
    print("*********************************\n")
    print ("*** BEM VINDO AO JOGO DE FORCA ***\n")
    print("********************************* \n")

    palavra_secreta = "banana"
    letra_acertada = ["_","_","_","_","_","_"]

    enforcou = False # variavel booleana - RETORNA FALSO OU VERDADEIRA 
    acertou = False
    #enquanto n se enforcouo E n acertou - segue o jogo
    while(not enforcou and not acertou): #palavras chave no python sempre se usa em letras minúscula
        
        chute = input("Qual Letra?")
        chute = chute.strip()#usado para retirar os espaços no inicio e final
        # for verificque a letra dentro de palavra !

        index = 0 #posição de cada letra.
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):#coloca o texto em maiúsculo
                 letra_acertada[index] = letra #guardando as letras corretas inseridas pela usuario
            index = index + 1 #incrimentando a dados  a cada letra 
        print(letra_acertada)

    print("Jogando...")
             
print("Fim do Jogo!")
if(__name__ == "__main__"): #verificando se a variavel possui valor especial e só executa quando selecionamos a mesma.
    jogarForca()