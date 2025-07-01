import urllib.request
import json


def gerar_perfil_usuario_aleatorio():
   
    url = "https://randomuser.me/api/"
    
    try:
        
        with urllib.request.urlopen(url) as response:
            if response.getcode() != 200:
                raise urllib.error.HTTPError(url, response.getcode(), "Erro HTTP", response.info(), None)
            
            
            dados_brutos = response.read().decode('utf-8')
        
        dados = json.loads(dados_brutos) 
        
        
        usuario = dados['results'][0]
        
       
        nome_titulo = usuario['name']['title']
        nome_primeiro = usuario['name']['first']
        nome_ultimo = usuario['name']['last']
        
        email = usuario['email']
        pais = usuario['location']['country']
        
        
        print("--- Perfil de Usuário Aleatório ---")
        print(f"Nome: {nome_titulo}. {nome_primeiro} {nome_ultimo}")
        print(f"Email: {email}")
        print(f"País: {pais}")
        
    except urllib.error.URLError as e:
        print(f"Erro ao conectar à API: {e.reason}")
        print("Verifique sua conexão com a internet.")
    except urllib.error.HTTPError as e:
        print(f"Erro HTTP ao acessar a API: {e.code} - {e.reason}")
    except json.JSONDecodeError as e:
        print(f"Erro ao processar os dados da API. Formato JSON inválido: {e}")
        print("Resposta bruta da API (se disponível):", dados_brutos if 'dados_brutos' in locals() else "N/A")
    except KeyError as e:
        print(f"Erro ao processar os dados da API: Chave esperada ausente - {e}")
        print("Estrutura JSON inesperada. Resposta da API (para depuração):", json.dumps(dados, indent=2) if 'dados' in locals() else "N/A")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    gerar_perfil_usuario_aleatorio()