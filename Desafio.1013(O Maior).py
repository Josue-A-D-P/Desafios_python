#Desafio 1013 O maior:

'''Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada:
7 14 106

Exemplos de Saída:
106 eh o maior'''

a, b, c = map(int,input().split())

if a > b:
    result = a
else:
    result = b

if result < c:
    result = c

print(f"{result} eh o maior")
