def password():
    """
    Ejercicio 11 - Validar Contraseña
    Lee una contraseña mediante input() y verifica de forma independiente 
    si cumple con la longitud mínima y si contiene al menos un número.
    """
    # 1. Leer la contraseña
    contrasena = input()

    # 2. Inicializar banderas de control
    tiene_largo_valido = True
    tiene_numero = False

    # 3. Validar requisito de longitud
    if len(contrasena) < 8:
        tiene_largo_valido = False

    # 4. Validar requisito de contener al menos un número (0 al 9)
    # Si cualquiera de estos caracteres está en la contraseña, la bandera pasa a True
    if ("0" in contrasena or "1" in contrasena or "2" in contrasena or 
        "3" in contrasena or "4" in contrasena or "5" in contrasena or 
        "6" in contrasena or "7" in contrasena or "8" in contrasena or 
        "9" in contrasena):
        tiene_numero = True

    # 5. Evaluar los resultados y emitir los mensajes correspondientes
    if tiene_largo_valido and tiene_numero:
        print("Contraseña valida")
    else:
        # Usamos ifs independientes para que se puedan imprimir ambos errores si es necesario
        if not tiene_largo_valido:
            print("Contraseña muy corta")
        if not tiene_numero:
            print("Debe contener un numero")