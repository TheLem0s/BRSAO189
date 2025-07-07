print("Digite números inteiros (ou 'fim' para encerrar).")

pares = 0
impares = 0

while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

print("\n--- Resumo ---")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
