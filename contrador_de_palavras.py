import re
import unicodedata

from print_colorido import print_color

def limpar_texto(texto):
	texto = unicodedata.normalize("NFD", texto)
	texto = "".join(
		char for char in texto
		if unicodedata.category(char) != "Mn"
	)
	texto = re.sub(r"[^a-zA-Z]", "", texto)

	return texto.lower()

def contador_palavras(frase_lista):
	palavras_lista = str(frase_lista).split()

	palavras_validas = []
	for palavra in palavras_lista:
		palavra_limpa = limpar_texto(palavra)
		if palavra_limpa and palavra_limpa not in palavras_validas:
			palavras_validas.append(palavra_limpa)

	return len(palavras_validas)

if __name__ == "__main__":
	while True:
		try:
			frase = str(input("Digite uma frase para contar as palavras: "))
			if not frase:
				print_color("yellow", "Frase invalida, tente novamente")
			else:
				break

		except Exception as e:
			print_color("red", f"Frase invalida: '{e}', tente novamente")

	contagem = contador_palavras(frase)
	if contagem == 0:
		print_color("yellow", f"Nenhuma palavra foi contabilizada na frase '{frase}'")
	else:
		print_color("green", f"{contagem} palavras contabilizadas na frase '{frase}'")