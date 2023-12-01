#importando outros jogos 
import forca
import adivinhacao

def escolheJogo():
    print("*********************************\n")
    print ("**** ESCOLHA SEU JOGO **** \n")
    print("********************************* \n")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo?")) #capturando o input #funcao biult


    if (jogo == 1):
        print("Você escolheu o jogo de Forca \n ")
        forca.jogarForca()
    elif(jogo == 2):
        print("Você escolheu o jogo de adivinhação \n")
        adivinhacao.jogarAdvinhacao()


    print("Fim do Jogo!")
if (__name__ == "__main__"):
    escolheJogo()