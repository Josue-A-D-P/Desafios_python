#Desafio conversão de tempo:

segundos = int(input())

minutos = segundos // 60
segundos = segundos % 60
horas = minutos // 60
minutos = minutos % 60


print(f"{horas:.0f}:{minutos:.0f}:{segundos :.0f}")