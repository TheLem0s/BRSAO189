import csv
import os 

def ler_e_exibir_dados_csv(nome_arquivo):
   
    print(f"--- Lendo dados do arquivo '{nome_arquivo}' ---")

    
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Por favor, certifique-se de que o arquivo existe no mesmo diretório do script, ou forneça o caminho completo.")
        return

    try:
        
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            reader = csv.DictReader(arquivo_csv) 

            
            if reader.fieldnames is None or not all(col in reader.fieldnames for col in ["Nome", "Idade", "Cidade"]):
                print(f"Aviso: O arquivo '{nome_arquivo}' pode não ter os cabeçalhos esperados (Nome, Idade, Cidade).")
                print(f"Cabeçalhos encontrados: {reader.fieldnames}")
                
            print("\n--- Dados encontrados no arquivo CSV ---")
            
           
            for i, linha in enumerate(reader):
                print(f"Pessoa {i+1}:")
                print(f"  Nome: {linha.get('Nome', 'N/A')}")
                print(f"  Idade: {linha.get('Idade', 'N/A')}")
                print(f"  Cidade: {linha.get('Cidade', 'N/A')}")
                print("-" * 20) 

            if i == -1: 
                 print("O arquivo CSV está vazio ou contém apenas o cabeçalho.")


    except FileNotFoundError: 
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")


arquivo_entrada = "pessoas_usuario.csv" 


if __name__ == "__main__":
    ler_e_exibir_dados_csv(arquivo_entrada)