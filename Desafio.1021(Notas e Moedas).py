#Desafio 1021 Notas e Moedas:

'''Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor 
monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode 
ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são 
de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, 
conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada:
576.73

Exemplo de Saída:
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01'''


valor = float(input())

list =(
100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 
1.00,  0.50, 0.25, 0.10, 0.05, 0.01,
)

N_100 = valor // list[0]
resto = valor % list[0]
N_50 = resto // list[1]
resto = resto % list[1]
N_20 = resto // list[2]
resto = resto % list[2]
N_10 = resto // list[3]
resto = resto % list[3]
N_5 = resto // list[4]
resto = resto % list[4]
N_2 = resto // list[5]
resto = resto % list[5]

M_1 = resto // list[6]
resto = resto % list[6]
M_50 = resto // list[7]
resto = resto % list[7]
M_25 = resto // list[8]
resto = resto % list[8]
M_10 = resto // list[9]
resto = resto % list[9]
M_05 = resto // list[10]
resto = resto % list[10]
M_01 = resto / list[11]
resto = resto % list[11]


print("NOTAS:")
print(f"{N_100:.0f} nota(s) de R$ 100.00")
print(f"{N_50:.0f} nota(s) de R$ 50.00")
print(f"{N_20:.0f} nota(s) de R$ 20.00")
print(f"{N_10:.0f} nota(s) de R$ 10.00")
print(f"{N_5:.0f} nota(s) de R$ 5.00")
print(f"{N_2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{M_1:.0f} moeda(s) de R$ 1.00")
print(f"{M_50:.0f} moeda(s) de R$ 0.50")
print(f"{M_25:.0f} moeda(s) de R$ 0.25")
print(f"{M_10:.0f} moeda(s) de R$ 0.10")
print(f"{M_05:.0f} moeda(s) de R$ 0.05")
print(f"{M_01:.0f} moeda(s) de R$ 0.01")