# Desafio 1042 sort simples:

'''Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em 
ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Exemplo de Entrada:
7 21 -14

Exemplo de Saída:
-14
7
21

7
21
-14'''


valor_1, valor_2, valor_3 = map(int,  input().split())


lista = [valor_1, valor_2, valor_3]

lista_ordenada = sorted(lista)

for x in lista:
    print(x)

print()

for x in lista_ordenada:
    print(x)