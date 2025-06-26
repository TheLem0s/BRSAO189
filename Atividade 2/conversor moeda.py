valor_real = 100
taxa_dolar = 5.20
taxa_euro = 6.15 

valor_dolar = valor_real / taxa_dolar


valor_euro = valor_real / taxa_euro


print(f"O valor de R${valor_real:.2f} reais convertido para dolar é de {valor_dolar:.2f} dolares ")
print(f"O valor de R${valor_real:.2f} reais convertido para euro é de {valor_euro:.2f} euros")