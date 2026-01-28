import random
from colorama import Fore, Style

ESCOLHAS_LIST = ["pedra", "papel", "tesoura", "poder divino"]

def pedra_papel_tesoura(elemento):
    escolha_bot = random.choice(ESCOLHAS_LIST)

    if elemento == escolha_bot:
        return {"status": "empate", "escolha_bot": escolha_bot}
    elif (elemento == "pedra" and escolha_bot == "papel") or (elemento == "papel" and escolha_bot == "tesoura") or (elemento == "tesoura" and escolha_bot == "pedra"):
        return {"status": "perdeu", "escolha_bot": escolha_bot}
    elif elemento == "poder divino":
        return {"status": "fodeu o amigo", "escolha_bot": escolha_bot}
    else:
        return {"status": "venceu", "escolha_bot": escolha_bot}

if __name__ == "__main__":
    print(f"{Fore.CYAN}=== Lets play? ===\n{Style.RESET_ALL}")

    while True:
        print(f"{Fore.CYAN}Escolha entre as opcoes: {Style.RESET_ALL}")
        for opcao in ESCOLHAS_LIST:
            if opcao != "poder divino":
                print(f"{Fore.CYAN}{opcao.title()}{Style.RESET_ALL}")

        escolha = input().lower().strip()
        if escolha not in ESCOLHAS_LIST:
            print(f"{Fore.YELLOW}Opcao invalida, tente novamente\n{Style.RESET_ALL}")
        else:
            break

    resultado = pedra_papel_tesoura(escolha)
    status = resultado["status"]

    if status == "empate":
        print(f"{Fore.MAGENTA}\nEmpate!{Style.RESET_ALL}")
    elif status == "perdeu":
        print(f"{Fore.RED}\nVoce {status}, o computador escolheu {resultado["escolha_bot"]}!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}\nVoce {status}, o computador escolheu {resultado["escolha_bot"]}!{Style.RESET_ALL}")