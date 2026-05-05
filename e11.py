def procesar_inventario():
    productos = ["Monitor", "Teclado", "Mouse"]
    stock = [15, 8, 20]
    precios = [25000, 5000, 3500]
    
    ganancias_totales = 0 #agrego la variable ganancias_totales para acumular la ganancia de cada operación
    ventas_totales = 0 
    pedidos_pendientes = [10, 12, 5] 

    print("--- Sistema de Despacho de Almacén ---")

    for i in range(len(productos)):
        nombre = productos[i]
        cantidad_pedida = pedidos_pendientes[i]
        stock_actual = stock[i] 
        precio_unitario = precios[i]

        print(f"Analizando pedido de: {nombre}")

        if stock_actual > cantidad_pedida: #cambie el operador por '>', haciendo que si el stock actual es mayor que la cantidad pedida, se procese el pedido
            total_operacion = cantidad_pedida * precio_unitario
            ganancias_totales += total_operacion #acumulo la ganancia de la operación a la variable ganancias_totales
            ventas_totales += cantidad_pedida #acumulo la cantidad vendida a la variable ventas_totales
            stock[i] = stock_actual - cantidad_pedida
            print(f"Pedido procesado. Stock restante: {stock[i]}")
        else:
            print(f"Error: Stock insuficiente para {nombre}. Stock: {stock_actual}")

    print("---------------------------------------")
    print(f"Resumen del día. Ganancias totales: ${ganancias_totales}. Ventas totales: {ventas_totales}") # agrego ganancias totales y modifico el valor de ventas totales por la cantidad vendida
    print(f"\nEstado final del stock: {stock}")

procesar_inventario()