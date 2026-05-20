def age_check():
    """
    Ejercicio 3 - Control de Edad Variable
    Leer una edad y un límite de edad mediante input(). Verifica que sean válidos
    y determina si la persona es mayor o menor de edad comparándola con dicho límite.
    """
    # 1. Leer las dos entradas como texto y convertirlas a enteros
    edad = int(input())
    limite = int(input())

    # 2. Validación de entrada: Deben ser estrictamente positivos (mayores a cero)
    if edad <= 0 or limite <= 0:
        print("Entrada invalida")
    
    # 3. Si son válidos, se evalúa si cumple o supera el límite variable
    elif edad >= limite:
        print("Eres mayor de edad")
        
    else:
        print("Eres menor de edad")