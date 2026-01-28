import random

from print_colorido import print_color

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
	print_color("cyan", "=== Lets play? ===\n")

	while True:
		print_color("cyan", "Escolha entre as opcoes: ")
		for opcao in ESCOLHAS_LIST:
			if opcao != "poder divino":
				print_color("cyan", opcao.title())

		escolha = input().lower().strip()
		if escolha not in ESCOLHAS_LIST:
			print_color("yellow", "Opcao invalida, tente novamente\n")
		else:
			break

	resultado = pedra_papel_tesoura(escolha)
	status = resultado["status"]

	if status == "empate":
		print_color("magenta", "\nEmpate!")
	elif status == "perdeu":
		print_color("red", f"\nVoce {status}, o computador escolheu {resultado['escolha_bot']}!")
	else:
		print_color("green", f"\nVoce {status}, o computador escolheu {resultado['escolha_bot']}!")