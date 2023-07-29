

salario = float(2000.00)

if salario <= 400.00:
    percentual = 15

elif salario <= 800.00:
    percentual = 12

elif salario <= 1200.00:
    percentual = 10

elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

reajuste = percentual * salario / 100
novo_salario = reajuste + salario

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print('Em percentual:', percentual, '%')