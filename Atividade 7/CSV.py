import csv

def coletar_e_escrever_dados_csv(nome_arquivo):
    
    dados_pessoas = []
    titulos = ["Nome", "Idade", "Cidade"]

    print("--- Coletor de Dados para CSV ---")
    print("Digite as informações de cada pessoa. Digite 'fim' para o nome para encerrar.")

    while True:
        nome = input("Nome (ou 'fim' para encerrar): ").strip() 

        if nome.lower() == 'fim':
            break 

        idade = None
        while idade is None:
            try:
                idade_str = input("Idade: ")
                idade = int(idade_str)
                if idade < 0:
                    print("Idade não pode ser negativa. Digite novamente.")
                    idade = None 
            except ValueError:
                print("Entrada inválida para idade. Digite um número inteiro.")
        
        cidade = input("Cidade: ").strip()

        
        dados_pessoas.append({"Nome": nome, "Idade": idade, "Cidade": cidade})
        print("Pessoa adicionada. Continue ou digite 'fim' para o nome para encerrar.")
        print("-" * 30) 

    if not dados_pessoas:
        print("Nenhum dado foi inserido. O arquivo CSV não será criado.")
        return 

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=titulos)
            writer.writeheader()
            writer.writerows(dados_pessoas)

        print(f"\nDados de {len(dados_pessoas)} pessoas escritos com sucesso no arquivo '{nome_arquivo}'.")

    except IOError as e:
        print(f"Erro de E/S ao escrever no arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


arquivo_saida = "pessoas_usuario.csv"

if __name__ == "__main__":
    coletar_e_escrever_dados_csv(arquivo_saida)