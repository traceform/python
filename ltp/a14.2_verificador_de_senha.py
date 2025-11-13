import re

def receber_dados():
    """Recebe a senha"""
    while True:
        try:
            senha = input("Digite a senha: ")
            break
        except KeyboardInterrupt:
            print("\nPrograma encerrado.")
            quit()
        except:
            print(f"Algo deu errado, tente novamente.")
    return senha

def verificar_senha(senha):
    """Verifica a senha"""

    # Verificando se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    else:
        # Verificando se tem pelo menos uma letra maiúscula
        if re.search(r'[A-Z]', senha):
            # Se tem pelo menos uma minúscula
            if re.search(r'[a-z]', senha):
                # Se tem pelo menos um número
                if re.search(r'[\d]', senha):
                    # Se tem pelo menos um caractere especial
                    if re.search(r'[!@#$%^&*()]', senha):
                        return True
        return False

def testa_verificar_senha():
    amostras_input = ['1', '12345678', '123456789', '123456789aaa', '123456789AAA', '123456789aaaAAA', '123456789aaaAAA#%$!', 'S#nh4@$T1']
    esperado = [False, False, False, False, False, False, True, True]
    print(f">>> TESTANDO verificar_senha()")
    for _ in range(len(esperado)):
        input = amostras_input[_]
        print(f"{input} -> ", end='')
        resultado = verificar_senha(input)
        if resultado == esperado[_]:
            estado = "OK"
        else:
            estado = "Falhou"
        print(estado, end='')
        print(f" | Resultado: {resultado}", end='')
        print()

if __name__ == "__main__":
    # Debugging
    #testa_verificar_senha()

    senha = receber_dados()
    forca = verificar_senha(senha)
    if forca:
        print(f"A senha é forte!")
    else:
        print(f"""A senha é fraca! Atente-se às recomendações:
Mínimo de 8 caracteres
Deve conter letras maiúsculas e minúsculas
Deve conter pelo menos um número
Deve conter pelo menos um caractere especial (!@#$%^&*())""")
