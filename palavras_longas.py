from print_colorido import print_color

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
			print_color("yellow", "Digite um texto valido!\n")
		else:
			break

	palavras = palavras_longas(texto)

	if not palavras:
		print_color("cyan", "\nNenhuma palavra longa foi encontrada no texto.")
	else:
		print_color("green", f"\nPalavras longas encontradas: {palavras}")
