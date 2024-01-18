#Desafio Tempo de jogo com minutos 

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
