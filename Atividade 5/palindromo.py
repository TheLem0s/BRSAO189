txt = input("Insira a palavra para conferir se é um palíndromo: ")


if txt == txt[::-1]:
    print(f"Sim")
else: 
    print(f"Não")

