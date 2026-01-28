from print_colorido import print_color

def somar(n1, n2):
    return {"calculo": f"{n1} + {n2}", "resultado_calculo": n1+n2}

def subtrair(n1, n2):
    return {"calculo": f"{n1} - {n2}", "resultado_calculo": n1-n2}

def multiplicar(n1, n2):
    return {"calculo": f"{n1} * {n2}", "resultado_calculo": n1*n2}

def dividir(n1, n2):
    return {"calculo": f"{n1} / {n2}", "resultado_calculo": n1/n2}

if __name__ == "__main__":
    operacoes = ["+", "_", "*", "/"]

    numero_1 = None
    numero_2 = None
    while True:
        try:
            numero_1 = int(input("Digite o primeiro número: "))

            while True:
                operacao = input("Escolha a operação (+, -, *, /):")

                if operacao not in operacoes:
                    print_color("red", "Opção inválida")
                    continue
                break

            while True:
                try:
                    numero_2 = int(input("Digite o segundo número: "))
                    break
                except ValueError:
                    print_color("red", "Erro: Entrada inválida. Digite apenas números.")

            break
        except ValueError:
            print_color("red", "Erro: Entrada inválida. Digite apenas números.")

    resultado = None
    if operacao == "+":
        resultado = somar(numero_1, numero_2)

    elif operacao == "-":
        resultado = subtrair(numero_1, numero_2)

    elif operacao == "*":
        resultado = multiplicar(numero_1, numero_2)

    elif operacao == "/":
        resultado = dividir(numero_1, numero_2)

    print_color("green", f"O calculo {resultado['calculo']} é {resultado['resultado_calculo']}")