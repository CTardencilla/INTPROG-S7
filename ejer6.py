frase = input("Introduce una frase: ")


en_palabra = False
contador = 0


for caracter in frase:
    if caracter != ' ' and not en_palabra:
        
        en_palabra = True
        contador += 1
    elif caracter == ' ':
        
        en_palabra = False


print(f"La frase contiene {contador} palabras.")
