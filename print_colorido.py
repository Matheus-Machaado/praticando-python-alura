from colorama import Fore, Style

def print_color(cor_nome, mensagem):
    cor = getattr(Fore, cor_nome.upper(), Fore.WHITE)
    print(cor + mensagem + Style.RESET_ALL)