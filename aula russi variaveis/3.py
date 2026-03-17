def calcular_delta(a, b, c):
  delta = (b ** 2) - (4 * a * c)

  return delta

coef_a = float(input("Digite o valor de a: "))
coef_b = float(input("Digite o valor de b: "))
coef_c = float(input("Digite o valor de c: "))

resultado = calcular_delta(coef_a, coef_b, coef_c)

print(f"O valor de delta é: {resultado}")