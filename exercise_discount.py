def discount():
    """
    Ejercicio 10 - Sistema de Descuentos por Cantidad
    Lee el precio unitario y la cantidad de unidades, determina el descuento aplicable,
    realiza los cálculos matemáticos correspondientes e imprime la salida formateada.
    """
    # 1. Leer las dos entradas secuencialmente y realizar el casting al tipo correcto
    precio = float(input())
    cantidad = int(input())

    # 2. Calcular el subtotal inicial
    subtotal = precio * cantidad

    # 3. Estructura condicional para determinar el porcentaje de descuento según la cantidad
    if cantidad >= 10:
        porcentaje_str = "20%"
        monto_descuento = subtotal * 0.20
    elif cantidad >= 5: # Al fallar la anterior, ya sabemos que cantidad es menor a 10
        porcentaje_str = "10%"
        monto_descuento = subtotal * 0.10
    else:
        porcentaje_str = "0%"
        monto_descuento = 0.0

    # 4. Calcular el total final a pagar
    total_final = subtotal - monto_descuento

    # 5. Imprimir los resultados utilizando f-strings respetando el formato exacto
    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {porcentaje_str}")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total_final}")