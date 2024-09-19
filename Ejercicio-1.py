short_min = -32,768
Short_max = 32,767
Long_min = -9223372036854775808
Long_max = 9223372036854775807
def short(num):
    if short_min  <= num <= Short_max:
        print(f"Valor convertido a short: {int(num)}")
    else:
        print("El valor está fuera del rango de short.")
def long(num):
    if Long_min <= num <= Long_max:
        print(f"Valor convertido a long: {int(num)}")
    else:
        print("El valor esta fuera del rango de long.")
while True:
    valorDecimal = float(input("Ingrese un numero decimal: "))
    short(valorDecimal)
    print(f"Valor convertido a int: {int(valorDecimal)}")
    long(valorDecimal)
    print(f"Valor convertido a float: {float(valorDecimal)}")

