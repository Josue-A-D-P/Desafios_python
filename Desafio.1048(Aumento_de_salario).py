

salario = float(input())

if salario <= 400.0:
    percentual = 15

elif salario <= 800.0:
    percentual = 12

elif salario <= 1200.0:
    percentual = 10

elif salario <= 2000.0:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual / 100.0
novo_salario = salario + reajuste

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')