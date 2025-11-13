def recebe_dados():
    """Recebe a frase e a palavra"""
    while True:
        try:
            frase = input("Digite uma frase: ")
            break
        except KeyboardInterrupt:
            print("\nPrograma terminado.")
            quit()
        except:
            print("Algo deu errado. Tente novamente! ")
    while True:
        try:
            palavra = input("Digite uma palavra: ")
            if len(palavra.split()) > 1:
                raise Exception("Digite apenas 1 palavra!")
            break
        except KeyboardInterrupt:
            print("\nPrograma terminado.")
            quit()
        except Exception as e:
            print(e)
        except:
            print("Algo deu errado. Tente novamente! ")
    return frase, palavra

def conta_palavra(frase, palavra):
    """Conta as ocorrências de uma palavra numa frase"""
    # Sanitizando a frase e removendo alguns caracteres especiais
    # SUBSTITUIR POR EXPRESSÕES REGULARES
    frase = frase.replace(',','').replace('.','').replace(':', '').replace(';', '').replace('!','').replace('?','').lower().split()
    palavra = palavra.strip().lower()

    # Debugging
    #print(frase)
    #print(palavra)

    # Vendo se há pelo menos uma ocorrÊncia de palavra em frase
    if palavra in frase:
        # Contando a quantidade de ocorrências de palavra em frase
        return frase.count(palavra)
    else:
        return None

def testa_conta_palavra():
    input_frase = ["O tempo passa... e os seus sonhos, ainda estão no papel?", "A vida é arte, artesão"]
    input_palavra = ['sonhos', 'arte']
    esperado = [1, 1]
    print(">>> TESTANDO conta_plavra()")
    for _ in range(len(esperado)):
        frase = input_frase[_]
        palavra = input_palavra[_]
        print(f"Frase: {frase}\nPalavra: {palavra}")
        resultado = conta_palavra(frase, palavra)
        if resultado == esperado[_]:
            estado = "OK"
        else:
            estado = "Falhou"
        print(f"Estado: {estado} ", end='')
        print(f"| Resultado: {resultado}", end='')
        print()

if __name__ == "__main__":
    frase, palavra = recebe_dados()
    qtd_ocorrencias = conta_palavra(frase, palavra)

    if qtd_ocorrencias:
        print(f"A palavra {palavra} foi encontrada {qtd_ocorrencias} vezes.")
    else:
        print(f"A palavra {palavra} não foi encontrada!")
    
    # Debugging
    #testa_conta_palavra()
