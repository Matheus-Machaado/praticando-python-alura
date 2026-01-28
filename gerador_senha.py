import random
from colorama import Fore, Style

def gerar_senha():
    letras = "abcdefghijklmnopqrstuvwxyz"
    numeros = "123456789"
    especiais = "!@#$%&*"

    senha = [
        random.choice(letras),
        random.choice(letras.upper()),
        random.choice(numeros),
        random.choice(especiais)
    ]

    todos_caracteres = letras + letras.upper() + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)

    return "".join(senha)

if __name__ == "__main__":
    print(f"{Fore.GREEN}Senha gerada: {gerar_senha()}{Style.RESET_ALL}")