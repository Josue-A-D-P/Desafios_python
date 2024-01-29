#Desafio 1043 triângulo:

'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

Exemplo de Entrada:
6.0 4.0 2.0

Exemplo de Saída:
Area = 10.0'''


A, B, C = map(float, input().split())


if (B - C) < A < (B + C) and (A - C) < B < (A + C) and (A - B) < C < (A + B):
    perimetro_tri = A + B + C
    print(f"Perimetro = {perimetro_tri:.1f}")

else:
    area_trap = (A + B)  * C / 2
    print(f"Area = {area_trap:.1f}")