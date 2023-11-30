#importando outros jogos 
import forca
import adivinhacao

print("*********************************\n")
print ("**** ESCOLHA SEU JOGO **** \n")
print("********************************* \n")

print("(1) Forca (2) adivinhação")
jogo = int(input("Qual jogo?")) #capturando o input #funcao biult


if (jogo == 1):
    print("Você escolheu: ")
elif(jogo ==2):
    print("jogando adivinhação")


print("Fim do Jogo!")