NUM_RENGLONES = 8
NUM_COLUMNAS = 5

# a) posición del elemento B[6, 4] en el arreglo unidimensional ordenado por renglones
def obtener_posicion_por_renglones(renglon, columna, inicio_unidimensional, num_columnas):
    # se convierte la posición bidimensional a un índice unidimensional ordenado por renglones
    indice_unidimensional = num_columnas * (renglon - 1) + (columna - 1)
    posicion_real = indice_unidimensional + inicio_unidimensional
    return posicion_real

# b) posición del elemento B[7, 2] en el arreglo unidimensional ordenado por columnas
def obtener_posicion_por_columnas(renglon, columna, inicio_unidimensional, num_renglones):
    indice_unidimensional = num_renglones * (columna - 1) + (renglon - 1)
    posicion_real = indice_unidimensional + inicio_unidimensional
    return posicion_real

# a: B[6, 4] en arreglo ordenado por renglones
renglon_a = 6
columna_a = 4
inicio_renglones = 10
posicion_a = obtener_posicion_por_renglones(renglon_a, columna_a, inicio_renglones, NUM_COLUMNAS)
print(f"Posición de B[6, 4] en el arreglo ordenado por renglones: {posicion_a}")

# b: B[7, 2] en arreglo ordenado por columnas
renglon_b = 7
columna_b = 2
inicio_columnas = 30
posicion_b = obtener_posicion_por_columnas(renglon_b, columna_b, inicio_columnas, NUM_RENGLONES)
print(f"Posición de B[7, 2] en el arreglo ordenado por columnas: {posicion_b}")
