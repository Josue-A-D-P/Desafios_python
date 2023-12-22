codigo_peca_1, numero_peca_1, valor_peca_1 = map(float, input().split())
codigo_peca_2, numero_peca_2, valor_peca_2 = map(float, input().split())

valor_a_pagar = (numero_peca_1 * valor_peca_1) + (numero_peca_2 * valor_peca_2)

print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")