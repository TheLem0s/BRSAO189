import urllib.request
import json
import datetime

def consultar_cotacao_moeda_urllib():

    print("--- Consulta de Cotação de Moeda (AwesomeAPI) ---")
    print("Códigos de moedas comuns: USD (Dólar Americano), EUR (Euro), GBP (Libra Esterlina)")
    
    moeda_desejada = input("Digite o código da moeda desejada (ex: USD): ").upper()
    
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_desejada}-BRL"
    
    try:
        
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
        
        dados_cotacao = json.loads(html) 
        
        chave_par_moeda = moeda_desejada + "BRL"
        
        if chave_par_moeda in dados_cotacao:
            cotacao = dados_cotacao[chave_par_moeda]
            
            valor_atual = float(cotacao['bid'])
            valor_maximo = float(cotacao['high'])
            valor_minimo = float(cotacao['low'])
            timestamp_atualizacao = int(cotacao['timestamp'])
            
            data_hora_atualizacao = datetime.datetime.fromtimestamp(timestamp_atualizacao)
            
            print(f"\n--- Cotação {moeda_desejada}/BRL ---")
            print(f"Moeda: {moeda_desejada}")
            print(f"Valor Atual (Compra): R$ {valor_atual:.4f}")
            print(f"Valor Máximo (24h): R$ {valor_maximo:.4f}")
            print(f"Valor Mínimo (24h): R$ {valor_minimo:.4f}")
            print(f"Última Atualização: {data_hora_atualizacao}")
            
        else:
            print(f"Não foi possível encontrar a cotação para '{moeda_desejada}'. Verifique o código da moeda.")
            print("Resposta da API (para depuração):", json.dumps(dados_cotacao, indent=2))
            
    except urllib.error.URLError as e:
        print(f"Erro ao conectar à API: {e.reason}")
        print("Verifique sua conexão com a internet ou o código da moeda.")
    except json.JSONDecodeError as e:
        print(f"Erro ao processar os dados da API. Formato JSON inválido: {e}")
        print("Resposta bruta da API (se disponível):", html if 'html' in locals() else "N/A")
    except KeyError as e:
        print(f"Erro ao processar os dados da API: Chave esperada ausente - {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

consultar_cotacao_moeda_urllib()