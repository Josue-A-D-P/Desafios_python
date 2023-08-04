# Desafio 1008 salário

funcionarios = {1 : 5.50 }

print(funcionarios[1])


Num_f = int(input("Digite o numero do funcionario: "))
V_hora = int(input('Digite o valor a receber pro hora: '))
H_trabalhadas = float(input('Digite quantas horas trabalhadas: '))

salario = V_hora * H_trabalhadas

print(f'NUMBER = {Num_f}')
print(f'SALARY = U$ {salario:.2f}')
