def leap_year():
    """
    Ejercicio 6 - Año Bisiesto
    Leer un año mediante input(). Determina si es bisiesto o no 
    utilizando operadores lógicos compuestos e imprime el resultado.
    """
    # 1. Leer el año desde la entrada estándar y pasarlo a entero
    anio = int(input())

    # 2. Aplicar la condición compuesta utilizando paréntesis para ordenar la prioridad
    if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")