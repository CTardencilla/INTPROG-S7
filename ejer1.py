
N = int(input("Introduce un número entero positivo: "))


if N > 0:
    suma = 0  
    for i in range(1, N + 1):
        suma += i  
    print("La suma de los números desde 1 hasta", N, "es:", suma)
else:
    print("El número debe ser un entero positivo.")
