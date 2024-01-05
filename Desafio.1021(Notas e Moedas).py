#Desafio Notas e Moedas

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