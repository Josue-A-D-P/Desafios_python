# Desafio salário com bônus:

Vendedor = input()
salario_vendedor = float(input())
Vendas = float(input())

comissao = Vendas * 15 / 100
salario = salario_vendedor + comissao
print(f'TOTAL = R$ {salario:.2f}')