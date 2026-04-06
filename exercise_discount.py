def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """

    precio_producto = float(input(""))
    cantidad_producto = int(input(""))
    Subtotal = precio_producto * cantidad_producto
    print("Subtotal:",Subtotal)

    if cantidad_producto >= 10:
        descuento = 0.20
        print("Descuento aplicado: 20%")

    elif cantidad_producto >= 5 and cantidad_producto <= 9:
        descuento = 0.10
        print("Descuento aplicado: 10%")

    else:
        descuento = 0.0
        print("0%")

    monto_descuento = Subtotal * descuento
    print("Monto descuento:",monto_descuento)

    Total_final = Subtotal - monto_descuento
    print("Total final:",Total_final)
    pass
#discount()