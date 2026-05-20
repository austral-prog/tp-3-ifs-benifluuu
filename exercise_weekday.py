def weekday():
    """
    Ejercicio 7 - Día Hábil o Fin de Semana
    Leer un día de la semana mediante input() en minúsculas. Determinar si es un
    día hábil o fin de semana usando obligatoriamente el operador lógico 'not'.
    """
    # 1. Leer el día ingresado por el usuario
    dia = input()

    # 2. Verificar usando 'not' que no sea sábado ni domingo
    if not (dia == "sabado") and not (dia == "domingo"):
        print("Dia habil")
    else:
        print("Fin de semana")