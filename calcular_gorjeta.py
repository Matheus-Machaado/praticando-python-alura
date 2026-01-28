from print_colorido import print_color
import re

def parse_valor_real(valor):
	if valor is None:
		return 0.0
	if isinstance(valor, (int, float)):
		return float(valor)

	s = str(valor).strip()
	s = s.replace("R$", "").strip()

	s = re.sub(r"[^0-9,.\-]", "", s)
	if not s or s == "-":
		return 0.0

	last_dot = s.rfind(".")
	last_comma = s.rfind(",")

	if last_dot != -1 and last_comma != -1:
		if last_comma > last_dot:
			s = s.replace(".", "").replace(",", ".")
		else:
			s = s.replace(",", "")

	elif last_comma != -1:
		s = s.replace(".", "").replace(",", ".")

	else:
		s = s.replace(",", "")

	try:
		return float(s)
	except ValueError:
		return 0.0

def formatar_valor_real(valor):
	return f"R$ {valor:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")

def calcular_gorjeta(conta, gorjeta):
	try:
		procentagem_formatada = gorjeta / 100

		valor_gorjeta_float = conta * procentagem_formatada
		valor_total_float = conta + valor_gorjeta_float

		return formatar_valor_real(valor_gorjeta_float), formatar_valor_real(valor_total_float)
	except Exception as e:
		print_color("red", f"Erro geral ao calcular gorjeta: {e}")
		return None

if __name__ == "__main__":
	while True:
		valor_conta = input("Digite o valor da conta: ")
		porcentagem_gorjeta = input("Digite a porcentagem de gorjeta: ")

		try:
			valor_conta_float = parse_valor_real(valor_conta)
			porcentagem_gorjeta_int = int(re.sub(r"\D", "", porcentagem_gorjeta))
			break
		except Exception as e:
			print_color("red", f"Valor conta({valor_conta}) ou procentagem gorjeta({porcentagem_gorjeta}) invalidos: {e}, tente novamente \n")

	resultado = calcular_gorjeta(valor_conta_float, porcentagem_gorjeta_int)
	if resultado:
		valor_gorjeta, valor_total = resultado

		print_color("yellow", f"\nValor da gorjeta: {valor_gorjeta}")
		print_color("green", f"Total a pagar: {valor_total}")
