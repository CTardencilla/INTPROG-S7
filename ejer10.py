
saldo = 1000  


contador_depositos = 0
contador_retiros = 0


while True:
    print("\n--- Cajero Automático ---")
    print(f"Saldo actual: ${saldo}")
    
    
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Salir")
    
    
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        
        deposito = float(input("Introduce la cantidad a depositar: "))
        saldo += deposito
        contador_depositos += 1
        print(f"Has depositado ${deposito}. Nuevo saldo: C${saldo}")
    
    elif opcion == '2':
        
        retiro = float(input("Introduce la cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            contador_retiros += 1
            print(f"Has retirado C${retiro}. Nuevo saldo: C${saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    
    elif opcion == '3':
        
        print(f"\nResumen final:")
        print(f"Total depósitos: {contador_depositos}")
        print(f"Total retiros: {contador_retiros}")
        print(f"Saldo final: C${saldo}")
        print("Gracias por usar el cajero automático.")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
