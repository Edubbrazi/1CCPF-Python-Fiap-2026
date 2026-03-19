# Entrada de dados
valor_produto = float(input("Digite o valor do produto: R$ "))
valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))

# Cálculo do troco
troco = valor_pago - valor_produto

# Verificação e exibição do resultado
if troco > 0:
    print(f"O valor do troco é: R$ {troco:.2f}")
elif troco == 0:
    print("Não há troco. O valor pago é exato.")
else:
    # Caso o valor pago seja menor que o custo do produto
    falta = abs(troco)
    print(f"Valor insuficiente! Ainda faltam R$ {falta:.2f}")