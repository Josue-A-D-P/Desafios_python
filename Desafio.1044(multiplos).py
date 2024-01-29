#Desafio 1044 Multiplos:

'''Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

Exemplo de Entrada:
6 24

Exemplo de Saída:
Sao Multiplos'''


def sao_multiplos(A, B):
    if A % B == 0 or B % A == 0:
        return "Sao Multiplos"
    else:
        return "Nao sao Multiplos"

A, B = map(int, input().split())


resultado = sao_multiplos(A, B)
print(resultado)