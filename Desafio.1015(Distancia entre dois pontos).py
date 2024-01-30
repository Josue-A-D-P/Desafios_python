# Desafio 1015 distancia entre dois pontos:

'''Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, 
p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a 
vírgula, segundo a fórmula

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de 
ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto 
decimal.

Exemplo de Entrada:
1.0 7.0
5.0 9.0

Exemplo de Saída:
4.4721'''


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

result = ((x2 - x1)** 2 + (y2 - y1)** 2) ** 0.5

print(f"{result:.4f}")