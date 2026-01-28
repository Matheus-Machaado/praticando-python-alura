import random
from print_colorido import print_color

if __name__ == "__main__":
    acertou = None
    numero_escolha_bot = random.randint(1, 100)

    while not acertou:
        while True:
            try:
                numero_escolha = int(input("\nTente adivinhar o número (1-100): "))
                break
            except ValueError as e:
                print_color("red", f"Entrada inválida: {e}")

        if numero_escolha_bot > numero_escolha:
            print_color("yellow", f"Muito baixo! Tente novamente: {numero_escolha}")
        elif numero_escolha_bot < numero_escolha:
            print_color("yellow", f"Muito alto! Tente novamente: {numero_escolha}")
        else:
            print_color("green", f"Parabéns! Você acertou o número {numero_escolha_bot}.")
            acertou = True