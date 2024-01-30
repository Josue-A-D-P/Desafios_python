#Desafio 1036 Fórmula de Bhaskara:

'''Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se 
não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel 
calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma 
mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada 
mensagem.

Exemplos de Entrada:
10.0 20.1 5.1

Exemplos de Saída:
R1 = -0.29788
R2 = -1.71212'''


A, B, C = map(float, input().split())

try:
    delta = (B**2) - 4 * A * C

    x = delta ** (1/2)

    r1 = ((- B) + x) / (2 * A)  
    r2 = ((- B) - x) /(2 * A)   


    print(f"{r1:.5f}")
    print(f"{r2:.5f}")
except:
    print("Impossivel calcular")