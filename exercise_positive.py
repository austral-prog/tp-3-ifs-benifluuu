def positive():
    """
    Ejercicio 1 - Clasificar Número
    Leer un número entero mediante input(). Determinar si es positivo, negativo o cero
    e imprimir el resultado correspondiente.
    """
    # 1. Leer la entrada y convertirla a un número entero
    numero = int(input())

    # 2. Estructura condicional para evaluar el valor
    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")


