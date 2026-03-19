# Lendo os valores de entrada e convertendo para float (número decimal)
nota_a = float(input("Digite a nota A: "))
nota_b = float(input("Digite a nota B: "))

# Calculando a média aritmética
# É importante usar parênteses para garantir que a soma ocorra antes da divisão
media = (nota_a + nota_b) / 2

# Exibindo o resultado
print(f"A média aritmética do aluno é: {media:.1f}")