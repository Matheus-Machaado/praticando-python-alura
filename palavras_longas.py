from colorama import Fore, Style

def palavras_longas(txt):
    palavras_list = str(txt).split()

    palavras_grandes = []
    for palavra in palavras_list:
        if len(palavra) > 10:
            palavras_grandes.append(palavra)

    return palavras_grandes

if __name__ == "__main__":
    while True:
        texto = str(input("Digite um texto: "))
        if not texto:
            print(f"{Fore.YELLOW}Digite um texto valido!\n{Style.RESET_ALL}")
        else:
            break

    palavras = palavras_longas(texto)

    if not palavras:
        print(f"{Fore.CYAN}\nNenhuma palavra longa foi encontrada no texto.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}\nPalavras longas encontradas: {palavras}{Style.RESET_ALL}")