#importando outros jogos 
import forca
import adivinhacao

print("*********************************\n")
print ("**** ESCOLHA SEU JOGO **** \n")
print("********************************* \n")

print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual jogo?")) #capturando o input #funcao biult


if (jogo == 1):
    print("Você escolheu: ")
    forca.jogarForca()
elif(jogo == 2):
    print("jogando adivinhação")
    adivinhacao.jogarAdvinhacao()


print("Fim do Jogo!")