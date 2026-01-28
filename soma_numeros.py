def somar_numeros(n1, n2):
    return n1 + n2

try:
    numero_1 = float(input("Digite o primeiro numero para somar: "))
    numero_2 = float(input("Digite o segundo numero para somar: "))

    resultado = somar_numeros(numero_1, numero_2)
    print(f"O resultado da soma entre '{numero_1}' e '{numero_2}' e = {resultado}")
except Exception as e:
    print(f"Erro ao fazer soma: {e}")