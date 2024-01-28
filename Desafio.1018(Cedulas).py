#Desafio 1018 Cédulas:

'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.

Exemplo de Entrada:
576

Exemplo de Saída:
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00'''


Valor = int(input())
print(Valor)
nt_100 = 0
nt_50 = 0
nt_20 = 0
nt_10 = 0
nt_5 = 0
nt_2 = 0
nt_1 = 0

while Valor > 0:
    
    if Valor >= 100:
        Valor = Valor - 100
        nt_100 += 1

    elif Valor < 100 and Valor >= 50:
        Valor = Valor - 50
        nt_50 += 1

    elif Valor < 50 and Valor >= 20:
        Valor = Valor - 20
        nt_20 += 1

    elif Valor < 20 and Valor >= 10:
        Valor = Valor - 10
        nt_10 += 1

    elif Valor < 10 and Valor >= 5:
        Valor = Valor - 5
        nt_5 += 1

    elif Valor < 5 and Valor >= 2:
        Valor = Valor - 2
        nt_2 += 1

    else:
        Valor < 2 and Valor >= 1
        Valor = Valor - 1
        nt_1 += 1


print(f"{nt_100} nota(s) de R$ 100,00")
print(f"{nt_50} nota(s) de R$ 50,00")
print(f"{nt_20} nota(s) de R$ 20,00")
print(f"{nt_10} nota(s) de R$ 10,00")
print(f"{nt_5} nota(s) de R$ 5,00")
print(f"{nt_2} nota(s) de R$ 2,00")
print(f"{nt_1} nota(s) de R$ 1,00")