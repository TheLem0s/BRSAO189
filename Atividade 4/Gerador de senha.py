import random
import string

qtd = int(input("Quantidade de caracteres para sua senha: "))
senha = string.ascii_letters + string.digits + string.punctuation

resultado = ''.join(random.choice(senha) for _ in range(qtd))

print(f"A senha é: {resultado}")

