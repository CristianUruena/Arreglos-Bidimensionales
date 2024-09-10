NUM_RENGLONES = 10  # 10 meses
NUM_COLUMNAS = 5    # 5 productos

VEN = [i * 10 for i in range(100, 150)]

def obtener_indice_unidimensional(renglon, columna, inicio_unidimensional, num_columnas):
    indice_unidimensional = num_columnas * (renglon - 1) + (columna - 1)
    posicion_real = indice_unidimensional + inicio_unidimensional
    return posicion_real

# a) Conocer las ventas del producto 4 durante el mes de marzo
renglon_marzo = 3 
columna_producto_4 = 4 
inicio_ventas = 100  
posicion_producto_4_marzo = obtener_indice_unidimensional(renglon_marzo, columna_producto_4, inicio_ventas, NUM_COLUMNAS)
ventas_producto_4_marzo = VEN[posicion_producto_4_marzo - inicio_ventas]
print(f"Ventas del producto 4 en durante el mes de marzo: {ventas_producto_4_marzo}")

# b) Calcular las ventas anuales del producto 1
columna_producto_1 = 1
ventas_anuales_producto_1 = sum(VEN[obtener_indice_unidimensional(renglon, columna_producto_1, inicio_ventas, NUM_COLUMNAS) - inicio_ventas] for renglon in range(1, NUM_RENGLONES + 1))
print(f"Ventas anuales del producto 1: {ventas_anuales_producto_1}")

# c) Obtener las ventas totales de todos los productos en el mes de julio
renglon_julio = 7
ventas_totales_julio = sum(VEN[obtener_indice_unidimensional(renglon_julio, columna, inicio_ventas, NUM_COLUMNAS) - inicio_ventas] for columna in range(1, NUM_COLUMNAS + 1))
print(f"Ventas totales de todos los productos en julio: {ventas_totales_julio}")
