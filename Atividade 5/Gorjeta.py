conta = float(input("Valor da conta: R$ "))
porcentagem = float(input("Porcentagem: "))

gorjeta = conta * (porcentagem / 100)
total = conta + gorjeta

print(f"Valor da conta é R$ {conta}")
print(f"Valor da gorjeta é R$ {gorjeta}")
print(f"Valor total com a gorjeta é R$ {total}")