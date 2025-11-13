# Importando biblioteca de Expressões Regulares
import re

def receber_dados():
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
            # Verificando se é só 1 palavra
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

def contar_palavra(frase, palavra):
    """Conta as ocorrências de uma palavra numa frase"""
    # Removendo a pontuação ".,;:?!—/\()[]{} e sanitizando a frase
    frase = re.sub(r"[\".,;:?!—/\\()[\]{}]", '', frase).lower().split()

    # Deixando a palavra em minúsculo
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

def testa_contar_palavra():
    # Listas de amostras de conteúdo para testar
    input_frase = ["O tempo passa... e os seus sonhos, ainda estão no papel?", "A vida é arte, artesão", "Oi, como vai?"]
    input_palavra = ['Sonhos', 'arte', 'vai']
    output_esperado = [1, 1, 1]

    print(">>> TESTANDO conta_plavra()")
    for _ in range(len(output_esperado)):
        frase = input_frase[_]
        palavra = input_palavra[_]
        esperado = output_esperado[_]

        print(f"Frase: {frase}\nPalavra: {palavra}")

        resultado = contar_palavra(frase, palavra)
        if resultado == esperado:
            estado = "OK"
        else:
            estado = "Falhou"
        
        print(f"Estado: {estado} ", end='')
        #print(f"| Resultado: {resultado}", end='')
        print('\n' + '-' * 30)

if __name__ == "__main__":
    frase, palavra = receber_dados()
    qtd_ocorrencias = contar_palavra(frase, palavra)

    if qtd_ocorrencias:
        if qtd_ocorrencias == 1:
            subst = 'vez'
        else:
            subst = 'vezes'
        print(f"A palavra '{palavra}' foi encontrada {qtd_ocorrencias} {subst}.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada!")
    
    # Debugging
    #testa_contar_palavra()
