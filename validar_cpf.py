from colorama import Fore, Style

def formatar_documento(d):
    if len(d) == 11:
        return f"{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}"
    elif len(d) == 14:
        return f"{d[:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:]}"
    else:
        print(f"{Fore.RED}Documento invalido para formatacao '{d}'{Style.RESET_ALL}")
        return None

def limpar_documento(valor):
    caracteres_limpar = [".", "-", "/"]

    for caracter in caracteres_limpar:
        valor = str(valor).replace(caracter, "")

    return valor

if __name__ == "__main__":
    documento = None
    while True:
        try:
            documento = input("Digite seu documento: ")
            documento_limpo = limpar_documento(documento)
            if not documento_limpo:
                print(f"{Fore.YELLOW}Valor documento invalido '{documento}', tente novamente \n{Style.RESET_ALL}")
                continue

            documento_limpo = int(documento_limpo)
            break
        except Exception as e:
            if documento:
                print(f"{Fore.RED}Valor documento invalido '{documento}': {e} \n{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Valor documento invalido: {e} \n{Style.RESET_ALL}")

    documento_str = str(documento_limpo)
    if len(documento_str) == 11:
        print(f"{Fore.GREEN}\nDocumento CPF valido '{formatar_documento(documento_str)}'{Style.RESET_ALL}")
    elif len(documento_str) == 14:
        print(f"{Fore.GREEN}\nDocumento CNPJ valido '{formatar_documento(documento_str)}'{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}\nDocumento invalido '{documento}'{Style.RESET_ALL}")