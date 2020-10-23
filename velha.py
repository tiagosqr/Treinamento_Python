# Jogo da velha contra a maquina selecionando posição aleatória que está livre
# Para limpar a tela executar no terminal ou console
import os
import random
import time

velha = []
p1 = ""
p2 = ""
r = 1
v = ""


# Função para limpar tela verifica tipo de sistema
def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")
    return ""


# Função para criar a tela jogo da velha
def tela():
    limpa_tela()
    print("-" * 37)
    if r < 10:
        print("Rodada: {}".format(r))
    else:
        print("Fim do jogo não houve ganhador!")
    print("Player1: {}                 Player2: {}".format(p1, p2))
    print("-" * 37)
    print(" " * 12 + "." + "-" * 11 + ".")

    # Estrutura de repetição para desenha o grid do jogo
    for i in range(0, 3):
        print(" " * 12 + "|", end="")
        for n in range(0, 3):
            if n < 2 and i <= 2:
                print(f" {velha[i][n]} " + "|", end="")
            else:
                print(f" {velha[i][n]} |")
        if i < 2:
            print(" " * 12 + "|---|---|---|")
    print(" " * 12 + "'" + "-" * 11 + "'")
    print("-" * 37)

    # Verificar vencedor para imprimir na tela
    if v == "X" and p1 == "X":
        print("Player1 venceu a partida!")
        os.system("pause")
    elif v == "O" and p1 == "O":
        print("Player1 venceu a partida!")
        os.system("pause")
    elif v != "":
        print("Player2 venceu a partida!")
        os.system("pause")


# Função para verificar vencedor
def verifica_vencedor():
    global v
    for i in range(0, 3):
        if velha[i][0] == velha[i][1] and velha[i][1] == velha[i][2]:
            v = velha[i][2]
            break
        if velha[0][i] == velha[1][i] and velha[1][i] == velha[2][i]:
            v = velha[2][i]
            break
        if velha[0][0] == velha[1][1] and velha[1][1] == velha[2][2]:
            v = velha[2][2]
            break
        if velha[2][0] == velha[1][1] and velha[1][1] == velha[0][2]:
            v = velha[2][0]
            break


# Função para iniciar a logica do jogo
def jogar():
    global velha
    velha.clear()
    velha = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    dic_matriz = {}
    dic_matriz.clear()
    dic_matriz = {"1": "00", "2": "01", "3": "02", "4": "10", "5": "11", "6": "12", "7": "20", "8": "21", "9": "22"}
    global p1
    global p2
    global r
    r = 1
    global v
    v = ""

    limpa_tela()

    p1 = input("Player1 informe qual caractere deseja usar X ou O: ").upper()
    if p1 == "X":
        p2 = "O"
    else:
        p2 = "X"

    vez_jogada = random.randint(1, 2)

    while r <= 9:
        tela()
        if vez_jogada == 1:
            while True:
                posicao = input("Player1 qual posição deseja marcar: ")
                if posicao in list(dic_matriz.keys()):
                    velha[int(dic_matriz[posicao][0])][int(dic_matriz[posicao][1])] = p1
                    dic_matriz.pop(posicao)
                    vez_jogada = 2
                    time.sleep(1)
                    break
                else:
                    print("Posição informada não existe ou já está marcada.")
                    time.sleep(2)
                    tela()

        else:
            posicao = random.choice(list(dic_matriz.keys()))
            velha[int(dic_matriz[posicao][0])][int(dic_matriz[posicao][1])] = p2
            dic_matriz.pop(posicao)
            vez_jogada = 1
            print("Player2 marcou a posição {}".format(posicao))
            time.sleep(2)

        if r > 4:
            verifica_vencedor()
            if v != "":
                break

        r += 1

    tela()


# Menu jogo
while True:
    limpa_tela()
    print("-" * 20)
    opcao = int(input("1: jogar\n2: sair\n" + "-" * 20 + "\nEscolha uma opção:"))
    if opcao == 1:
        jogar()
    elif opcao == 2:
        print("Saindo do Jogo")
        break
    else:
        print("Opção invalida")