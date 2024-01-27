# Desafio Numeros positivos

v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())
cont = 0.0
list_num = v1,v2,v3,v4,v5,v6

for x in list_num:
    if x > 0.0:
        cont += 1
print(f'{int(cont)} valores positivos')


