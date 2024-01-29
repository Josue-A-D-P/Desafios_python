# Desafio 1046 tempo de jogo:

'''Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

Exemplo de Entrada:
16 2

Exemplo de Saída:
O JOGO DUROU 10 HORA(S)'''


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