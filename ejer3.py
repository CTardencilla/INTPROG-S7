
cadena = input("Introduce una cadena: ")


contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0


for caracter in cadena.lower():  
    if caracter == 'a':
        contador_a += 1
    elif caracter == 'e':
        contador_e += 1
    elif caracter == 'i':
        contador_i += 1
    elif caracter == 'o':
        contador_o += 1
    elif caracter == 'u':
        contador_u += 1


print("Cantidad de vocales encontradas:")
print("a:", contador_a)
print("e:", contador_e)
print("i:", contador_i)
print("o:", contador_o)
print("u:", contador_u)
