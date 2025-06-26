produto = "Camiseta"
preco_original = 50
desconto = 20

valor_desconto = preco_original * (desconto / 100)

print(f"Produto: {produto}")
print(f"Valor total: R${preco_original:.2f}")
print(f"Porcentagem de desconto {desconto}%")
print(f"Valor final: R${valor_desconto:.2f}")

