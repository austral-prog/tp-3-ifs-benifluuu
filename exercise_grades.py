def grades():
    """
    Ejercicio 5 - Clasificar Nota
    Leer una nota (0-10) mediante input(). Clasifica la nota de acuerdo a su rango
    e imprime el resultado correspondiente.
    """
    # 1. Leer la nota desde la entrada estándar y convertirla a entero
    nota = int(input())

    # 2. Estructura condicional múltiple evaluando los rangos pedidos
    if nota >= 9 and nota <= 10:
        print("Excelente")
        
    elif nota >= 7 and nota <= 8:
        print("Bueno")
        
    elif nota >= 5 and nota <= 6:
        print("Regular")
        
    else:
        print("Insuficiente")