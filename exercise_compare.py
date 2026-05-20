def compare():
    """
    Ejercicio 4 - Comparar Dos Números
    Lee dos números enteros mediante input(), los compara e imprime 
    si el primero es mayor, menor o igual al segundo.
    """
    # 1. Leer los dos números secuencialmente desde la entrada estándar
    num1 = int(input())
    num2 = int(input())

    # 2. Evaluar las tres condiciones posibles e imprimir usando f-strings
    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
        
    elif num1 < num2:
        print(f"{num1} es menor que {num2}")
        
    else:
        print(f"{num1} es igual a {num2}")