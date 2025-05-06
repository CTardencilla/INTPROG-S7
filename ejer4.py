
N = int(input("Introduce la cantidad de calificaciones: "))

if N > 0:
    suma = 0  

   
    for i in range(N):
        calificacion = float(input(f"Introduce la calificación #{i + 1}: "))
        suma += calificacion

    
    promedio = suma / N
    print("El promedio de las calificaciones es:", promedio)
else:
    print("La cantidad debe ser un número entero positivo.")
