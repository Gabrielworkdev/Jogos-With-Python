print("*********************************")
print("")
print("")
print("")
print ("JOGO DE ADIVINHAÇÃO")
print("*********************************")
print("")
print("")
print("")


#declarando o número secreto
numero_secreto = 42

#interação com o usuário
chute_str = input("digite o seu número:  \n")

#incluindo um texto 
print("Você digitou", chute_str)
#declarando que a palavra chute irá receber uma string
chute = int(chute_str)
#comparando o valor digitado com o nº secreto "=="
if (numero_secreto == chute):

    print("você acertou!")
else:
    print("Você errou!")

print("Fim do Jogo!")