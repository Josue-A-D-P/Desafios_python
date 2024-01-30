# Desafio 1006 Media2:

'''Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, 
calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem 
peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o 
ponto decimal e com um espaço em branco antes e depois da igualdade.

Exemplos de Entrada:
5.0
6.0
7.0

Exemplos de Saída:
MEDIA = 6.3'''


A = float(input())
B = float(input())
C = float(input())
PESO = 10.0

A = A * 2.0
B = B * 3.0
C = C * 5.0

print(f'MEDIA = {(A + B + C) / PESO:.1f}')