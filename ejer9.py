
numero = int(input("Introduce un número entero: "))


frecuencia = {}


while numero > 0:
    digito = numero % 10          
    if digito in frecuencia:      
        frecuencia[digito] += 1
    else:
        frecuencia[digito] = 1     
    numero = numero // 10         


print("Frecuencia de cada dígito:")
for i in range(10):
    if i in frecuencia:
        print(f"Dígito {i}: {frecuencia[i]} veces")
    else:
        print(f"Dígito {i}: 0 veces")
