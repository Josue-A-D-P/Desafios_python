Valor = float(input())

N_100 = 0
N_50 = 0
N_20 = 0
N_10 = 0
N_5 = 0
N_2 = 0

M_1 = 0
M_50 = 0
M_25 = 0
M_10 = 0
M_05 = 0
M_01 = 0

while Valor > 0.00:
    if Valor >= 100.00:
        N_100 += 1
        Valor -= 100.00
    
    elif Valor >= 50.00:
         N_50 += 1
         Valor -= 50.00

    elif Valor >= 20.00:
         N_20 += 1
         Valor -= 20.00

    elif Valor >= 10.00:
         N_10 += 1
         Valor -= 10.00

    elif Valor >= 5.00:
         N_5 += 1
         Valor -= 5.00

    elif Valor >= 2.00:
        N_2 += 1
        Valor -= 2.00

    elif Valor >= 1.00:
        M_1 += 1
        Valor -= 1.00

    elif Valor >= 0.50:
        M_50 += 1
        Valor -= 0.50

    elif Valor >= 0.25:
        M_25 += 1
        Valor -= 0.25

    elif Valor >= 0.10:
        M_10 += 1
        Valor -= 0.10

    elif Valor >= 0.05:
        M_05 += 1
        Valor -= 0.05

    else:
        Valor > 0.01
        M_01 += 1
        Valor -= 0.01




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