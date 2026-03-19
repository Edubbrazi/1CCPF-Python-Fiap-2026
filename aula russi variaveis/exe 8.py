# Entrada de dados da Peça 1
nome_peca1 = input("Digite o nome da peça 1: ")
quant_peca1 = int(input(f"Quantas unidades de {nome_peca1} você quer? "))
valor_peca1 = float(input(f"Qual o valor unitário de {nome_peca1}? R$ "))

# Entrada de dados da Peça 2
nome_peca2 = input("\nDigite o nome da peça 2: ")
quant_peca2 = int(input(f"Quantas unidades de {nome_peca2} você quer? "))
valor_peca2 = float(input(f"Qual o valor unitário de {nome_peca2}? R$ "))

# Cálculos
total_peca1 = quant_peca1 * valor_peca1
total_peca2 = quant_peca2 * valor_peca2
valor_total_compra = total_peca1 + total_peca2

# Exibição dos Resultados
print("-" * 40)
print(f"Subtotal {nome_peca1}: R$ {total_peca1:.2f}")
print(f"Subtotal {nome_peca2}: R$ {total_peca2:.2f}")
print(f"VALOR TOTAL A PAGAR: R$ {valor_total_compra:.2f}")
print("-" * 40)