quantidade_livros = 3
preco_livro = 25

# Dados das canetas
quantidade_canetas = 2
preco_caneta = 5

# Cálculo dos subtotais e do total geral
total_livros = quantidade_livros * preco_livro
total_canetas = quantidade_canetas * preco_caneta
total_gasto = total_livros + total_canetas

# Exibindo o resultado
print(f"Total gasto com livros: R$ {total_livros}")
print(f"Total gasto com canetas: R$ {total_canetas}")
print("-" * 30)
print(f"O valor total da compra é: R$ {total_gasto:.2f}")