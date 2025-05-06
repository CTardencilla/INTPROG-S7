#leer una palabra diferente a fin y cinvertirla a mayuscula

palabra= input('Dime la palabra: ')

while palabra != "fin":
    print(palabra.upper())
    palabra=input('dime la palabra: ')
else:
    print("adios...")