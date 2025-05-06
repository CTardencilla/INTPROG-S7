M = int(input("Introduce un número entero positivo: "))


if M > 0:
    producto = 1     
    contador = 0    
    numero = 2       

    while contador < M:
        producto *= numero
        contador += 1
        numero += 2  

    print("El producto de los primeros", M, "números pares es:", producto)
else:
    print("El número debe ser un entero positivo.")
