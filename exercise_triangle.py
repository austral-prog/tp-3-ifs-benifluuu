def triangle():
    """
    Ejercicio 9 - Validar Triángulo
    Leer tres números flotantes mediante input(). Determina si pueden formar
    un triángulo válido aplicando la desigualdad triangular.
    """
    # 1. Leer los tres lados de forma secuencial
    a = float(input())
    b = float(input())
    c = float(input())

    # 2. Verificar las tres condiciones de la desigualdad triangular usando 'and'
    condicion1 = (a + b) > c
    condicion2 = (a + c) > b
    condicion3 = (b + c) > a

    # 3. Evaluar si se cumplen todas simultáneamente
    if condicion1 and condicion2 and condicion3:
        print("Los lados forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")