import forca
import adivinhação1

print("*********************************")
print("*******Escolha seu jogo**********")
print("*********************************")

print("(1) Forca (2)Adivinhação")
jogo= int(input("Qual jogo? R: "))
if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhação1.jogar()