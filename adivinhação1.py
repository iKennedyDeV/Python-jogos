import random
def jogar():
        print("*********************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("*********************************")

        numero_secreto = random.randint(1,100)
        total_de_tentativas = 0
        pontos = 50
        print("Escolha o nivel de dificuldade")
        print("(1)Facil (2)medio (3)dificil")
        try:
            nivel =int(input("defina o valor:"))
        except:
            print("insira valor indicado")
            print("(1)Facil (2)medio (3)dificil")
            nivel = int(input("defina o valor:"))
        if( nivel == 1):
             total_de_tentativas = 20
        elif(nivel == 2):
             total_de_tentativas = 10
        else:
             total_de_tentativas = 5

        for rodada in range(1, total_de_tentativas + 1):
            print("_________________________________________________________")
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute_str = input("Digite um número entre 1 e 10: ")
            print("Você digitou " , chute_str)
            chute = int(chute_str)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 10!")
                continue

            acertou = chute == numero_secreto
            maior= chute > numero_secreto
            menor= chute < numero_secreto

            if(acertou):

                print("Você acertou!")
                break
            else:
                if(maior):
                    print("Você errou! O seu chute foi maior do que o número secreto.")
                    ponto_perdido = abs(numero_secreto - chute)
                    pontos -= ponto_perdido
                elif(menor):

                    print("Você errou! O seu chute foi menor do que o número secreto.")
                    ponto_perdido = abs(numero_secreto - chute)
                    pontos -= ponto_perdido


        print("Fim do jogo")
        print(pontos)
if(__name__ == "__main__"):
  jogar()


  
