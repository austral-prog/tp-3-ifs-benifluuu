def even_odd():
    """
    Ejercicio 2 - Par o Impar
    Leer un número entero mediante input(). Determinar si el número es par o impar
    e imprimir el resultado correspondiente.
    """
    # 1. Leer la entrada y transformarla a entero
    numero = int(input())

    # 2. Verificar el resto de la división por 2
    if numero % 2 == 0:
        # Usamos f-string para garantizar el formato exacto del test
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")