from print_colorido import print_color

def formatar_documento(d):
	if len(d) == 11:
		return f"{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}"
	elif len(d) == 14:
		return f"{d[:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:]}"
	else:
		print_color("red", f"Documento invalido para formatacao '{d}'")
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
				print_color("yellow", f"Valor documento invalido '{documento}', tente novamente \n")
				continue

			documento_limpo = int(documento_limpo)
			break
		except Exception as e:
			if documento:
				print_color("red", f"Valor documento invalido '{documento}': {e} \n")
			else:
				print_color("red", f"Valor documento invalido: {e} \n")

	documento_str = str(documento_limpo)
	if len(documento_str) == 11:
		print_color("green", f"\nDocumento CPF valido '{formatar_documento(documento_str)}'")
	elif len(documento_str) == 14:
		print_color("green", f"\nDocumento CNPJ valido '{formatar_documento(documento_str)}'")
	else:
		print_color("red", f"\nDocumento invalido '{documento}'")