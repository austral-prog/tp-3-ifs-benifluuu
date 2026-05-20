def calculator():
    """
    Ejercicio 8 - Calculadora Básica
    Leer dos números flotantes y un operador (+, -, *, /) mediante input().
    Realiza la operación correspondiente aplicando las validaciones requeridas.
    """
    # 1. Leer las tres entradas secuencialmente
    num1 = float(input())
    num2 = float(input())
    operacion = input()

    # 2. Estructura condicional para evaluar la operación y realizar validaciones
    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
        
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
        
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
        
    elif operacion == "/":
        # Validación crítica: evitar la división por cero
        if num2 == 0:
            print("Error: division por cero")
        else:
            print(f"Resultado: {num1 / num2}")
            
    else:
        # Validación: cualquier otro símbolo es una operación inválida
        print("Operacion invalida")