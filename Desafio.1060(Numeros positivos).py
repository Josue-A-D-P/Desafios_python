# Desafio 1060 Numeros positivos:

'''Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos 
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada:
7
-5
6
-3.4
4.6
12

Exemplo de Saída:
4 valores positivos'''


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


