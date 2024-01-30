#Desafio 1045 tipos de triangulo:

'''Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o 
lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três 
lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C 
(0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.

Exemplos de Entrada:
7.0 5.0 7.0

Exemplos de Saída:
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES'''


def classificar_triangulo(a, b, c):
    lados = sorted([a, b, c], reverse=True)
    a, b, c = lados

    
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
        return

    
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

    
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")


a, b, c = map(float, input().split())

classificar_triangulo(a, b, c)

