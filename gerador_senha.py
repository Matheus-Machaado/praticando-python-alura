import random

from print_colorido import print_color

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
	print_color("green", f"Senha gerada: {gerar_senha()}")
