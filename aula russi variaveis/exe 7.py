# Lendo as notas do aluno
nota_a = float(input("Digite a nota A: "))
nota_b = float(input("Digite a nota B: "))

# Definindo os pesos
peso_a = 4
peso_b = 6

# Calculando a média ponderada
# Fórmula: (NotaA * PesoA + NotaB * PesoB) / (Soma dos Pesos)
media_ponderada = (nota_a * peso_a + nota_b * peso_b) / (peso_a + peso_b)

# Exibindo o resultado formatado
print(f"A média ponderada do aluno é: {media_ponderada:.1f}")