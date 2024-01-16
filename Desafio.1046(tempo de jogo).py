# Desafio tempo de jogo

inicio, fim = map(int, input().split())
tempo_de_jogo = 0


if inicio == fim:
    tempo_de_jogo = 24

elif inicio > fim:
    for x in range(inicio,24):
        tempo_de_jogo += 1
        print(x)

    if fim != 0:
        for x in range(0,fim):
            tempo_de_jogo += 1

else:
    for x in range(inicio,fim):
        tempo_de_jogo += 1


print(f"O JOGO DUROU {tempo_de_jogo} HORA(S)")