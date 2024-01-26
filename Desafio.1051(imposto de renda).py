#Desafio imposto de renda

salario = float(input())

imposto_1 = 0
imposto_2 = 0
imposto_3 = 0

if salario > 0.00 and salario <= 2000.00:
    print('Isento')
else:
    if salario > 4500.00:
        imposto_3 = (salario - 4500.00) * 28 / 100
        cont = salario - 4500.00
        salario = salario - cont
        imposto_2 = (salario - 3000.00) * 18 / 100
        cont = salario - 3000.00
        salario = salario - cont
        imposto_1 = (salario - 2000.00) * 8 / 100
    
    elif salario > 3000.00 and salario < 4500.00:
        imposto_2 = (salario - 3000.00) * 18 / 100
        cont = salario - 3000.00
        salario = salario - cont
        imposto_1 = (salario - 2000.00) * 8 / 100

    else:
        salario > 2000.00 and salario < 3000.00
        salario = salario - 3000.00
        imposto_1 = (salario - 2000.00) * 8 / 100

    tot_imposto = imposto_1 + imposto_2 + imposto_3

    print(f"R$ {tot_imposto:.2f}")