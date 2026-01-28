from colorama import Fore, Style

def contador_vogais(txt):
    vogais = "aeiou"
    quantidade = 0

    for letra in txt.lower():
        if letra in vogais:
            quantidade += 1

    return quantidade

if __name__ == "__main__":
    while True:
        texto = str(input("Digite um texto: "))
        if not texto:
            print(f"{Fore.YELLOW}Digite um texto valido!\n{Style.RESET_ALL}")
        else:
            break

    quantidade_vogais = contador_vogais(texto)

    if quantidade_vogais == 0:
        print(f"{Fore.CYAN}\nO texto '{texto}' nao contém vogais. {Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}\nO texto '{texto}' contém {quantidade_vogais} vogais. {Style.RESET_ALL}")