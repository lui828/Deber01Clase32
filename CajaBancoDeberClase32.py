# Definir listas para almacenar los usuarios y sus saldos
usuarios = []
saldos = []

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya está registrado")
    else:
        usuarios.append(nombre)
        saldos.append(0.00)
        print(f"Usuario {nombre} agregado correctamente")

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        monto = float(input("Introduce el monto a depositar: "))
        saldos[indice] += monto
        print(f"Depósito realizado. Nuevo saldo: {saldos[indice]}")
    else:
        print(f"Usuario {nombre} no existe")

def retirar():
    nombre = input("Ingrese el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        retiro = float(input("Ingrese el monto de retiro: "))
        if retiro > saldos[indice]:
            print("Saldo insuficiente para retirar")
        else:
            saldos[indice] -= retiro
            print(f"Retiro realizado. Nuevo saldo: {saldos[indice]}")
    else:
        print("Usuario no existente en el sistema")

def consultar_saldo():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        print(f"El saldo actual de {nombre} es: {saldos[indice]}")
    else:
        print("Usuario no existente en el sistema")

def menu_principal():
    while True:
        print("\nMenú principal")
        print("1. Registrar usuario")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            consultar_saldo()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú principal
menu_principal()