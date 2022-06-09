# Trabalho feito por Kauã Yuri e Fabiano

import os
import sys
import time
def jogar_novamente():
    print('Deseja jogar novamente? (1) Sim, (2) Não')
    novamente = int(input().strip())
    
    if(novamente == 1):
        jogar()
    elif(novamente == 2):
        print('Bom jogo! até mais!')
        time.sleep(3)
        os.system('cls')
        sys.exit(0)
        
def jogar(): 
    dica = 0
    print(f"Seja Bem-Vindo ao Jogo da Forca. \n")

    desafiante = input("Informe seu nome Desafiante: ").upper().strip()
    competidor = input("Informe seu nome Competidor: ").upper().strip()
    os.system('cls')

    print(f'\n {desafiante} complete as informações a seguir: \n')
    palavra_secreta = input('Informe a Palavra Chave: ').upper().strip()
    dica1 = input('Informe a dica nº 1: ')
    dica2 = input('Informe a dica nº 2: ')
    dica3 = input('Informe a dica nº 3: ')
    os.system('cls')

    quantidade = len(palavra_secreta)
    digitadas = []
    acerto = []
    erro = 0

    while True:
        senha = ""

        for letra in palavra_secreta:
            senha += letra if letra in acerto else "*"
        print(senha)

        if senha == palavra_secreta:
            print("Você acertou! Parabéns! Vencedor: ",competidor)
            break

        print('A palavra secreta contém ', quantidade, ' letras')
        print('Escolha uma das alternativa:')
        print("(1) Chutar Letra")
        print("(2) Pedir Dica")
        op = input()
        if op == "1":
            print()
        elif op == "2":
            if dica == 0:
                print("Dica nº 1: " + dica1)
                dica += 1
            elif dica == 1:
                print("Dica nº 2: " + dica2)
                dica += 1
            elif dica == 2:
                print("Dica nº 3: " + dica3)
                dica += 1 
            else:
                print("Você já solicitou todas as dicas do jogo! ):")
                dica += 1
        tentativa = input("\nDigite uma letra:").upper().strip()

        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_secreta:
                acerto += tentativa
            else:
                erro += 1
                print("Você errou! ")
            print("X==:==\nX  :   ")
            print("X  O   " if erro >= 1 else "X")
            linha2 = ""

            if erro == 2:
                linha2 = "  |   "
            elif erro == 3:
                linha2 = " \|   "
            elif erro >= 4:
                linha2 = " \|/ "

            print("X%s" % linha2)

            linha3 = ""
            if erro == 5:
                linha3 += " /     "
            elif erro >= 6:
                linha3 += " / \ "

            print("X%s" % linha3)
            print("X\n===========")

            if erro == 6:
                print("Você foi Enforcado! Vencedor: ",desafiante)         
                break

    if  erro == 6: 
        vencedor = desafiante
    elif senha == palavra_secreta: 
        vencedor = competidor
    conteudo = []       
    try:
        arquivo = open('historico.txt','r')
        conteudo = arquivo.readlines()
        arquivo.close()
        
    except:
        arquivo = open('historico.txt', 'w')
        arquivo.close()
    conteudo.append(palavra_secreta+' - ')
    conteudo.append(vencedor + '\n')
    arquivo = open('historico.txt','w')
    arquivo.write(''.join(conteudo))
    arquivo.close()
    arquivo = open("historico.txt","r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
    jogar_novamente()
    
jogar() 