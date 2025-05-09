numero = int(input("Introduce un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print(f"El factorial de {numero} es {factorial}")
