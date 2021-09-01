# converter entrada em número
def converter_num(valor):
    try:
        valor = int(valor)
        return valor

    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converter_num(input('Digite um número: '))

    if numero is None:
        print('Erro: isso não é um número')
    else:
        print(numero * 5)