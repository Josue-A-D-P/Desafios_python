# Desafio 1048 Aumento de salario:

'''A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a 
tabela abaixo:


Salário	Percentual de Reajuste:
    0 - 400.00          15%
    400.01 - 800.00     12%
    800.01 - 1200.00    10%
    1200.01 - 2000.00   7%
    Acima de 2000.00    4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste 
ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser 
apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada:
400.00

Exemplo de Saída:
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %'''


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