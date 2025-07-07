def verificar_senha_forte():
    
    while True:
        senha = input("Digite sua senha: ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            print("Erro: A senha deve ter pelo menos 8 caracteres.")
            continue

        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break
        
        if not tem_numero:
            print("Erro: A senha deve conter pelo menos um número.")
            continue

        print("Sucesso! A senha é forte.")
        break

if __name__ == "__main__":
    verificar_senha_forte()