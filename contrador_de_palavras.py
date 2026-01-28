import re

from colorama import  Fore, Style
import unicodedata

def limpar_texto(texto):
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        char for char in texto
        if unicodedata.category(char) != "Mn"
    )
    texto = re.sub(r"[^a-zA-Z]", "", texto)

    return texto.lower()

def contador_palavras(frase_lista):
    palavras_lista = str(frase_lista).split()

    palavras_validas = []
    for palavra in palavras_lista:
        palavra_limpa = limpar_texto(palavra)
        if palavra_limpa not in palavras_validas:
            palavras_validas.append(palavra_limpa)

    return len(palavras_validas)

if __name__ == "__main__":
    while True:
        try:
            frase = str(input("Digite uma frase para contar as palavras: "))
            if not frase:
                print(f"{Fore.YELLOW}Frase invalida, tente novamente{Style.RESET_ALL}")
            else:
                break

        except Exception as e:
            print(f"{Fore.RED}Frase invalida: '{e}', tente novamente{Style.RESET_ALL}")

    contagem = contador_palavras(frase)
    if contagem == 0:
        print(f"{Fore.YELLOW}Nenhuma palavra foi contabilizada na frase '{frase}'{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}{contagem} contabilizadas na frase '{frase}'{Style.RESET_ALL}")