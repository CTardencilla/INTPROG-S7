suma_pares = 0
suma_impares = 0

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

    numero = int(input("Introduce otro número (0 para terminar): "))

print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")
