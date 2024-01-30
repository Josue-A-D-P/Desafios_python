#Desafio 1047 Tempo de jogo com minutos:

'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir 
calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU xxx HORA(S) E YYY MINUTO(S)” .

Exemplo de Entrada:
7 8 9 10

Exemplo de Saída:
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)'''


hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

if hora_inicial == minuto_inicial and hora_final == minuto_final and hora_final == minuto_final:
    duracao_horas = 24
    duracao_minutos = 0

else:
    inicio_em_minutos = hora_inicial * 60 + minuto_inicial
    fim_em_minutos = hora_final * 60 + minuto_final

    duracao_em_minutos = (fim_em_minutos - inicio_em_minutos + 24 * 60) % (24 * 60)

    duracao_horas = duracao_em_minutos // 60
    duracao_minutos = duracao_em_minutos % 60


print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
