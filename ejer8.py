
N = int(input("¿Cuántos números vas a ingresar?: "))


numero = float(input("Introduce el número #1: "))
mayor = numero
menor = numero


for i in range(1, N):
    numero = float(input(f"Introduce el número #{i + 1}: "))
    
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero


print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
