def calculadora_basica_simples():

    while True: 
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)

            operacao = input("Digite a operação (+, -, *, /): ")

            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)

            resultado = None

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                print("Erro: Operação inválida. Por favor, digite uma das opções: +, -, *, /")
                continue 

            
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            break 

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite números válidos.")
        except ZeroDivisionError as e:
            print(f"Erro de operação: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
        
        print("Por favor, tente novamente.") 

if __name__ == "__main__":
    calculadora_basica_simples()