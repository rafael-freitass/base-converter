# função principal
def main():
    print("Escreva o número para converter")
    num = str(input("Número: "))
    print("Escreva a base do número: ('binario: 2', 'decimal: 10', 'octal: 8' ou 'hexadecimal: 16')")
    base = int(input("base: "))

    if base in [2, 8, 10, 16]:
        inputToDecimal = base_to_decimal(num, base)

        print("Base 2: ", decimal_to_base(inputToDecimal, 2))
        print("Base 10: ", inputToDecimal)
        print("Base 8: ", decimal_to_base(inputToDecimal, 8))
        print("Base 16: ", decimal_to_base(inputToDecimal, 16))

    else:
        print("Valor inválido! ")
        main()

    continuar_programa()


# converter todos os numeros para decimal
def base_to_decimal(num, base):
    decimal = 0

    dicionario = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    for i in range(len(num)):
        pot = base ** (len(num) - 1 - i)
        binario = dicionario[num[i]] * pot
        decimal += binario
    return decimal


# converter os decimais para as bases
def decimal_to_base(num, base):
    dicionario = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    binario = int(num)
    resto = ''

    while binario > 0:
        if base == 16:
            hexaValue = dicionario[binario % base]
            resto = str(hexaValue) + resto
        else:
            resto = str(binario % base) + resto

        binario = int(binario / base)
    return resto


# loop para continuar programa
def continuar_programa():
    print("\nContinuar programa? (s/n)")
    inp = input("resposta: ")
    if inp == 's' or inp == 'S':
        main()


main()
