valor = 5000

valor_formatado = f'R${valor:,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.')
print(valor_formatado)