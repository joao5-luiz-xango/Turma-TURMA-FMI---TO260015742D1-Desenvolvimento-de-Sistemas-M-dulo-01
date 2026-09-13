# 1 e 2. Entrada de dados (usamos float para aceitar casas decimais)
valor_total = float(input("Digite o valor total da compra (R$): "))

# 3. Verificação das regras de desconto
if valor_total < 200.00:
    porcentagem_desconto = 5
elif valor_total >= 200.00 and valor_total < 300.00:
    porcentagem_desconto = 10
else:
    porcentagem_desconto = 15

# 4 e 5. Cálculos dos valores
valor_desconto = valor_total * (porcentagem_desconto / 100)
valor_final = valor_total - valor_desconto

# 6 a 8. Exibição dos resultados (formatados com 2 casas decimais)
print(f"\n--- Resumo da Compra ---")
print(f"Valor original: R$ {valor_total:.2f}")
print(f"Desconto aplicado: {porcentagem_desconto}% (R$ {valor_desconto:.2f})")
print(f"Valor final a pagar: R$ {valor_final:.2f}")