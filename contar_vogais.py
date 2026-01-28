from print_colorido import print_color

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
			print_color("yellow", "Digite um texto valido!\n")
		else:
			break

	quantidade_vogais = contador_vogais(texto)

	if quantidade_vogais == 0:
		print_color("cyan", f"\nO texto '{texto}' nao contém vogais.")
	else:
		print_color("green", f"\nO texto '{texto}' contém {quantidade_vogais} vogais.")