# Desafio idade em dias

idade = int(input())

ano = idade // 365
mes = (idade % 365) // 30
dias = (idade % 365) % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")