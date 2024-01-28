# Desafio 1002  Área do circulo:

'''A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

Entrada
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

Saída
Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double).

Exemplos de Entrada:
2.00

Exemplos de Saída:
A=12.5664'''


n = 3.14159
raio = float(input())
raio = raio ** 2 * n

print(f'A={raio:.4f}')