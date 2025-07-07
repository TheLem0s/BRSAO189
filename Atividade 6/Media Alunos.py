def calcular_media_turma():
    
    print("Digite as notas (de 0 a 10). Digite 'fim' para encerrar.")

    total_notas = 0
    quantidade_notas_validas = 0

    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)

            if 0 <= nota <= 10:
                total_notas += nota
                quantidade_notas_validas += 1
            else:
                print("Erro: Nota inválida. Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número para a nota ou 'fim'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    print("\n--- Resumo da Turma ---")
    if quantidade_notas_validas > 0:
        media = total_notas / quantidade_notas_validas
        print(f"Total de notas válidas registradas: {quantidade_notas_validas}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida para calcular a média.")
    print("Programa encerrado.")

if __name__ == "__main__":
    calcular_media_turma()