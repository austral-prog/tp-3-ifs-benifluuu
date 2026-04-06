def even_odd():
    """
    Ejercicio 2 - Par o Impar

    Leer un número entero mediante input(). Determinar si el número es par o impar
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "8", la salida esperada es:
        El numero 8 es par

        Para la entrada "7", la salida esperada es:
        El numero 7 es impar
    """


    Numero = int(input())

    if Numero % 2 == 0:
        print("El numero",Numero,"es par")

    else:
        print(f"El numero {Numero} es impar")


    pass
#even_odd()